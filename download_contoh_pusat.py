import os
import re
import json
import time
import shutil
import urllib.request
import urllib.parse
import http.cookiejar
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "Contoh_Bukti_Dukung_Pusat")
GDRIVE_DIR = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ridsonalfarizal15@gmail.com/My Drive/ZI/Contoh_Bukti_Dukung_Pusat")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(BASE_DIR, "data.json"), "r", encoding="utf-8") as f:
    app_data = json.load(f)

tasks = []
for area in app_data["areas"]:
    pilar_num = area["number"]
    pilar_name = f"Pilar_{pilar_num}_{area['title'].replace(' ', '_')}"
    for aspect in ["pemenuhan", "reform"]:
        asp_label = "Pemenuhan" if aspect == "pemenuhan" else "Reform"
        for grp in area[aspect]["groups"]:
            for itm in grp["items"]:
                code = itm["code"]
                link = itm.get("link_contoh", "")
                q = itm.get("question", "")
                drive_folder = itm.get("drive_folder", "")
                if link:
                    tasks.append({
                        "pilar_num": pilar_num,
                        "pilar_name": pilar_name,
                        "aspect": asp_label,
                        "code": code,
                        "link": link,
                        "question": q,
                        "drive_folder": drive_folder
                    })

print(f"Total indicators with link_contoh: {len(tasks)}")

def process_item(item):
    code = item["code"]
    link = item["link"]
    safe_code = code.replace(".", "_")
    target_dir = os.path.join(OUTPUT_DIR, item["pilar_name"], item["aspect"], f"Point_{safe_code}")
    os.makedirs(target_dir, exist_ok=True)
    
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36")]

    retries = 3
    for attempt in range(retries):
        try:
            resp = opener.open(link, timeout=15)
            final_url = resp.geturl()
            html = resp.read().decode("utf-8", errors="ignore")
            
            parsed = urllib.parse.urlparse(final_url)
            qs = urllib.parse.parse_qs(parsed.query)
            folder_id = qs.get("id", [""])[0]
            
            drive_url_m = re.search(r'\"\.driveUrl\":\"([^\"]+)\"', html)
            token_m = re.search(r'\"\.driveAccessToken\":\"([^\"]+)\"', html)
            
            if not (drive_url_m and token_m and folder_id):
                return {"code": code, "status": "no_token_or_folder", "files": [], "error": "SharePoint token/folder not found"}
            
            drive_url = drive_url_m.group(1)
            token = token_m.group(1).replace("access_token=", "")
            rel_path = folder_id.split("/Documents/")[-1]
            
            # Recursive fetch helper
            def fetch_children(path, sub_folder_name=""):
                req_url = f"{drive_url}/root:/{urllib.parse.quote(path)}:/children"
                req = urllib.request.Request(req_url)
                req.add_header("Authorization", f"Bearer {token}")
                req.add_header("Accept", "application/json")
                api_resp = opener.open(req, timeout=15)
                data = json.loads(api_resp.read().decode("utf-8"))
                
                results = []
                for fi in data.get("value", []):
                    if "folder" in fi:
                        sub_path = f"{path}/{fi['name']}"
                        results.extend(fetch_children(sub_path, sub_folder_name=fi["name"]))
                    else:
                        name = fi.get("name")
                        dl_url = fi.get("@content.downloadUrl") or fi.get("@microsoft.graph.downloadUrl")
                        size = fi.get("size", 0)
                        if name and dl_url:
                            results.append({
                                "name": name,
                                "size": size,
                                "dl_url": dl_url,
                                "sub_folder": sub_folder_name
                            })
                return results

            all_file_items = fetch_children(rel_path)
            
            downloaded = []
            for fi in all_file_items:
                name = fi["name"]
                dl_url = fi["dl_url"]
                size = fi["size"]
                sub = fi["sub_folder"]
                
                if sub:
                    dest_dir = os.path.join(target_dir, sub.replace("/", "_"))
                    os.makedirs(dest_dir, exist_ok=True)
                else:
                    dest_dir = target_dir
                    
                dest_file = os.path.join(dest_dir, name)
                
                # Check if already downloaded and valid
                if not os.path.exists(dest_file) or os.path.getsize(dest_file) == 0:
                    dl_req = urllib.request.Request(dl_url)
                    dl_resp = opener.open(dl_req, timeout=40)
                    with open(dest_file, "wb") as out_f:
                        out_f.write(dl_resp.read())
                
                actual_size = os.path.getsize(dest_file)
                downloaded.append({
                    "name": name,
                    "sub_folder": sub,
                    "size": actual_size,
                    "rel_path": os.path.relpath(dest_file, OUTPUT_DIR)
                })
                
            return {"code": code, "status": "ok", "files": downloaded, "dir": target_dir}
        except Exception as e:
            if attempt == retries - 1:
                return {"code": code, "status": "error", "files": [], "error": str(e)}
            time.sleep(1)

results = []
downloaded_count = 0
total_bytes = 0

print("Starting recursive download with 6 workers...")
with ThreadPoolExecutor(max_workers=6) as executor:
    futures = {executor.submit(process_item, task): task for task in tasks}
    for fut in as_completed(futures):
        res = fut.result()
        results.append(res)
        n_files = len(res["files"])
        downloaded_count += n_files
        b_sum = sum(f["size"] for f in res["files"])
        total_bytes += b_sum
        if res["status"] == "ok":
            print(f"[{res['code']}] OK - {n_files} file(s) ({round(b_sum/1024, 1)} KB)")
        else:
            print(f"[{res['code']}] {res['status']}: {res.get('error', '')}")

# Save index manifest
manifest_path = os.path.join(OUTPUT_DIR, "manifest_contoh_pusat.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n==========================================")
print(f"SELESAI REKURSIF! Total files: {downloaded_count}")
print(f"Total size: {round(total_bytes / (1024*1024), 2)} MB")
print(f"Manifest: {manifest_path}")

if os.path.exists(os.path.dirname(GDRIVE_DIR)):
    print(f"Syncing all to Google Drive: {GDRIVE_DIR} ...")
    shutil.copytree(OUTPUT_DIR, GDRIVE_DIR, dirs_exist_ok=True)
    print("Google Drive sync complete!")
