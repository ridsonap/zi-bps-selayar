import json

with open("data.json", "r", encoding="utf-8") as f:
    app_data = json.load(f)

# Score data
scores = {
    1: {"pemenuhan": 2.54, "reform": 4.00, "total": 6.54, "bobot": 8.00, "pct": "81.75%"},
    2: {"pemenuhan": 3.38, "reform": 3.50, "total": 6.88, "bobot": 7.00, "pct": "98.29%"},
    3: {"pemenuhan": 3.96, "reform": 3.50, "total": 7.46, "bobot": 10.00, "pct": "74.60%"},
    4: {"pemenuhan": 5.00, "reform": 3.50, "total": 8.50, "bobot": 10.00, "pct": "85.00%"},
    5: {"pemenuhan": 3.38, "reform": 7.50, "total": 10.88, "bobot": 15.00, "pct": "72.53%"},
    6: {"pemenuhan": 3.95, "reform": 2.50, "total": 6.45, "bobot": 10.00, "pct": "64.50%"},
}

pilars_data = []
all_points_flat = []

for area in app_data["areas"]:
    pilar_num = area["number"]
    pilar_title = area["title"]
    sc = scores.get(pilar_num, {"total": 0, "bobot": 0, "pct": "0%"})
    
    subpilars = []
    
    # Pemenuhan
    for g_idx, grp in enumerate(area["pemenuhan"]["groups"]):
        sp_id = f"sp_{pilar_num}_p_{g_idx}"
        points = []
        for itm in grp["items"]:
            pt_obj = {
                "pilarNum": pilar_num,
                "pilarTitle": pilar_title,
                "aspect": "Pemenuhan",
                "subPilarId": sp_id,
                "subPilarName": grp["name"],
                "code": itm["code"],
                "question": itm["question"],
                "tipe": itm.get("tipe", ""),
                "kriteria": itm.get("kriteria", ""),
                "jawaban": itm.get("jawaban", ""),
                "nilai": str(itm.get("nilai", "0.00")),
                "status": itm.get("status", "missing"),
                "badge": itm.get("badge", ""),
                "narasi": itm.get("narasi", ""),
                "catatan": itm.get("catatan", ""),
                "bukti": itm.get("bukti", []),
                "link_contoh": itm.get("link_contoh", ""),
                "drive_folder": itm.get("drive_folder", "")
            }
            points.append(pt_obj)
            all_points_flat.append(pt_obj)
            
        subpilars.append({
            "id": sp_id,
            "aspect": "Pemenuhan",
            "name": grp["name"],
            "points": points
        })
        
    # Reform
    for g_idx, grp in enumerate(area["reform"]["groups"]):
        sp_id = f"sp_{pilar_num}_r_{g_idx}"
        points = []
        for itm in grp["items"]:
            pt_obj = {
                "pilarNum": pilar_num,
                "pilarTitle": pilar_title,
                "aspect": "Reform",
                "subPilarId": sp_id,
                "subPilarName": grp["name"],
                "code": itm["code"],
                "question": itm["question"],
                "tipe": itm.get("tipe", ""),
                "kriteria": itm.get("kriteria", ""),
                "jawaban": itm.get("jawaban", ""),
                "nilai": str(itm.get("nilai", "0.00")),
                "status": itm.get("status", "missing"),
                "badge": itm.get("badge", ""),
                "narasi": itm.get("narasi", ""),
                "catatan": itm.get("catatan", ""),
                "bukti": itm.get("bukti", []),
                "link_contoh": itm.get("link_contoh", ""),
                "drive_folder": itm.get("drive_folder", "")
            }
            points.append(pt_obj)
            all_points_flat.append(pt_obj)
            
        subpilars.append({
            "id": sp_id,
            "aspect": "Reform",
            "name": grp["name"],
            "points": points
        })
        
    all_pts = [p for sp in subpilars for p in sp["points"]]
    comp_pts = sum(1 for p in all_pts if p["status"] == "complete" and p["nilai"] in ["1.00", "1", "300.00%", "100.00%", "105.74%"])
    att_pts = len(all_pts) - comp_pts
    
    pilars_data.append({
        "number": pilar_num,
        "title": pilar_title,
        "scorePct": sc["pct"],
        "totalScore": sc["total"],
        "maxScore": sc["bobot"],
        "totalPoints": len(all_pts),
        "completePoints": comp_pts,
        "attentionPoints": att_pts,
        "subpilars": subpilars
    })

print(f"Hierarchical structure built: {len(pilars_data)} pilars, {sum(len(p['subpilars']) for p in pilars_data)} subpilars, {len(all_points_flat)} points.")

pilars_json_str = json.dumps(pilars_data, ensure_ascii=False)
flat_points_json_str = json.dumps(all_points_flat, ensure_ascii=False)

html_template = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panduan Bukti Dukung ZI WBK 2025 | BPS Kabupaten Kepulauan Selayar</title>
  <meta name="description" content="Sistem Panduan Bukti Dukung Zona Integritas BPS Kabupaten Kepulauan Selayar dengan Struktur Hirarki Dropdown Pilar, Sub Pilar, dan Point Indikator.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>">
  <style>
    :root {
      --bg: #f8fafc;
      --surface: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --border-focus: #3b82f6;

      --primary: #1e3a8a;
      --primary-light: #eff6ff;
      --primary-border: #bfdbfe;

      --success: #15803d;
      --success-light: #f0fdf4;
      --success-border: #bbf7d0;

      --warning: #b45309;
      --warning-light: #fffbeb;
      --warning-border: #fde68a;

      --danger: #b91c1c;
      --danger-light: #fef2f2;
      --danger-border: #fecaca;

      --radius: 10px;
      --radius-sm: 6px;
      --radius-full: 9999px;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }

    a { color: var(--primary); text-decoration: none; }
    button { font-family: inherit; }

    .container {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 16px;
    }

    /* TOP NAVBAR */
    .top-header {
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
    }
    .top-header-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 60px;
      gap: 12px;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      min-width: 0;
    }
    .brand-icon {
      font-size: 1.5rem;
      flex-shrink: 0;
    }
    .brand-text {
      min-width: 0;
    }
    .brand-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      line-height: 1.2;
    }
    .brand-sub {
      font-size: 0.75rem;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .btn-header-drive {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--primary);
      color: #ffffff;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 600;
      white-space: nowrap;
      transition: opacity 0.15s ease;
      flex-shrink: 0;
    }
    .btn-header-drive:hover {
      opacity: 0.9;
    }

    /* HERO SUMMARY */
    .hero {
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 24px 0 20px 0;
    }
    .hero-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 4px;
      letter-spacing: -0.3px;
    }
    .hero-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 18px;
    }

    /* STATS ROW */
    .stats-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 10px;
    }
    .stat-box {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .stat-label {
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .stat-num-row {
      display: flex;
      align-items: baseline;
      gap: 6px;
      margin: 4px 0 6px 0;
    }
    .stat-num {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--text);
    }
    .stat-note {
      font-size: 0.75rem;
      color: var(--text-muted);
    }
    .stat-bar-bg {
      height: 5px;
      background: var(--border);
      border-radius: var(--radius-full);
      overflow: hidden;
    }
    .stat-bar-fill {
      height: 100%;
      border-radius: var(--radius-full);
    }

    /* NAVIGATION TABS */
    .tabs-nav {
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 60px;
      z-index: 40;
    }
    .tabs-scroll {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding: 8px 0;
      scrollbar-width: none;
    }
    .tabs-scroll::-webkit-scrollbar { display: none; }

    .tab-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 600;
      background: transparent;
      color: var(--text-muted);
      border: 1px solid transparent;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }
    .tab-btn:hover {
      background: var(--bg);
      color: var(--text);
    }
    .tab-btn.active {
      background: var(--text);
      color: #ffffff;
    }

    /* MAIN CONTAINER */
    .main-wrap {
      padding: 20px 0 60px 0;
    }
    .tab-content {
      display: none;
    }
    .tab-content.active {
      display: block;
    }

    /* FILTER BAR & CASCADING DROPDOWNS */
    .filter-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      margin-bottom: 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .search-box {
      position: relative;
      width: 100%;
    }
    .search-input {
      width: 100%;
      padding: 9px 12px 9px 36px;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      color: var(--text);
      background: #ffffff;
      outline: none;
      transition: border-color 0.15s;
    }
    .search-input:focus {
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
    }
    .search-icon {
      position: absolute;
      left: 11px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.85rem;
      color: var(--text-muted);
      pointer-events: none;
    }

    /* DROPDOWN SELECTS ROW */
    .dropdown-selects-grid {
      display: grid;
      grid-template-columns: 1.5fr 1.5fr 1fr;
      gap: 10px;
    }
    .select-wrap {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .select-label {
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .select-input {
      width: 100%;
      padding: 8px 10px;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      background: #ffffff;
      color: var(--text);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      outline: none;
      transition: all 0.15s ease;
    }
    .select-input:focus {
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
    }

    .filter-actions-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: wrap;
      padding-top: 10px;
      border-top: 1px dashed var(--border);
    }
    .btn-toggle-tree {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text);
      background: var(--bg);
      border: 1px solid var(--border);
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.15s;
    }
    .btn-toggle-tree:hover {
      background: #e2e8f0;
    }
    .btn-reset-checks {
      font-size: 0.74rem;
      font-weight: 600;
      color: var(--danger);
      background: transparent;
      border: 1px solid var(--danger-border);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      cursor: pointer;
    }
    .btn-reset-checks:hover {
      background: var(--danger-light);
    }

    /* RESULT INFO */
    .result-info {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      font-size: 0.8rem;
      color: var(--text-muted);
      padding: 0 2px;
    }

    /* ======================================================== */
    /* 3-TIER ACCORDION DROPDOWNS: PILAR -> SUB PILAR -> POINT   */
    /* ======================================================== */

    .tree-container {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    /* LEVEL 1: PILAR DROPDOWN */
    .pilar-dropdown {
      background: var(--surface);
      border: 1px solid var(--border);
      border-left: 5px solid var(--primary);
      border-radius: var(--radius);
      overflow: hidden;
      transition: border-color 0.15s, box-shadow 0.15s;
    }
    .pilar-dropdown:hover {
      border-color: #cbd5e1;
    }
    .pilar-dropdown[open] {
      box-shadow: var(--shadow-sm);
      border-color: #94a3b8;
    }

    .pilar-summary {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 18px;
      cursor: pointer;
      user-select: none;
      list-style: none;
      gap: 12px;
      background: #ffffff;
      transition: background 0.15s;
    }
    .pilar-summary::-webkit-details-marker { display: none; }
    .pilar-summary:hover {
      background: #f8fafc;
    }
    .pilar-summary-left {
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 0;
      flex: 1;
    }
    .pilar-badge {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: var(--radius-sm);
      background: var(--primary-light);
      color: var(--primary);
      border: 1px solid var(--primary-border);
      white-space: nowrap;
      flex-shrink: 0;
    }
    .pilar-title {
      font-size: 1rem;
      font-weight: 800;
      color: var(--text);
      line-height: 1.25;
    }
    .pilar-sub {
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 2px;
    }
    .pilar-summary-right {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }
    .pilar-stat-pill {
      font-size: 0.7rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      white-space: nowrap;
    }
    .stat-complete { background: var(--success-light); color: var(--success); }
    .stat-attention { background: var(--warning-light); color: var(--warning); }
    .pilar-score-pill {
      font-size: 0.76rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: var(--radius-full);
      background: var(--primary);
      color: #ffffff;
      white-space: nowrap;
    }

    .pilar-body {
      padding: 6px 14px 14px 14px;
      background: #f8fafc;
      border-top: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    /* LEVEL 2: SUB PILAR DROPDOWN */
    .subpilar-dropdown {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      overflow: hidden;
      transition: all 0.15s ease;
    }
    .subpilar-dropdown[open] {
      border-color: #cbd5e1;
    }
    .subpilar-summary {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 14px;
      cursor: pointer;
      user-select: none;
      list-style: none;
      gap: 10px;
      background: #f1f5f9;
      transition: background 0.15s;
    }
    .subpilar-summary::-webkit-details-marker { display: none; }
    .subpilar-summary:hover {
      background: #e2e8f0;
    }
    .subpilar-summary-left {
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 0;
      flex: 1;
    }
    .aspect-badge {
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      white-space: nowrap;
      flex-shrink: 0;
    }
    .aspect-pemenuhan {
      background: #dbeafe;
      color: #1e40af;
    }
    .aspect-reform {
      background: #f3e8ff;
      color: #6b21a8;
    }
    .subpilar-title {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text);
      line-height: 1.3;
    }
    .subpilar-summary-right {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }
    .subpilar-count {
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    .subpilar-body {
      padding: 8px 10px 10px 10px;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    /* LEVEL 3: POINT-POINT INDIKATOR DROPDOWN */
    .point-dropdown {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      overflow: hidden;
      transition: all 0.15s ease;
    }
    .point-dropdown.state-complete {
      border-left: 3.5px solid var(--success);
    }
    .point-dropdown.state-missing {
      border-left: 3.5px solid var(--danger);
    }
    .point-dropdown.state-partial {
      border-left: 3.5px solid var(--warning);
    }
    .point-dropdown[open] {
      border-color: #94a3b8;
    }

    .point-summary {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 9px 12px;
      cursor: pointer;
      user-select: none;
      list-style: none;
      gap: 10px;
      background: #ffffff;
      transition: background 0.15s;
    }
    .point-summary::-webkit-details-marker { display: none; }
    .point-summary:hover {
      background: #f8fafc;
    }
    .point-summary-left {
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 0;
      flex: 1;
    }
    .point-code {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: var(--radius-sm);
      background: var(--bg);
      color: var(--text);
      border: 1px solid var(--border);
      white-space: nowrap;
      flex-shrink: 0;
    }
    .point-question {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text);
      line-height: 1.35;
    }
    .point-summary-right {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }
    .badge-status {
      display: inline-flex;
      align-items: center;
      font-size: 0.7rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      white-space: nowrap;
    }
    .badge-state-complete {
      background: var(--success-light);
      color: var(--success);
    }
    .badge-state-missing {
      background: var(--danger-light);
      color: var(--danger);
    }
    .badge-state-partial {
      background: var(--warning-light);
      color: var(--warning);
    }

    .chevron-icon {
      font-size: 0.7rem;
      color: var(--text-muted);
      transition: transform 0.2s ease;
      display: inline-block;
    }
    details[open] > summary .chevron-icon {
      transform: rotate(180deg);
    }

    /* POINT BODY CONTENT */
    .point-body {
      padding: 10px 14px 14px 14px;
      border-top: 1px dashed var(--border);
      background: #ffffff;
    }

    .point-bukti-box {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      margin-bottom: 10px;
    }
    .point-bukti-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }
    .point-bukti-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .point-bukti-item {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 0.8rem;
      line-height: 1.35;
    }
    .point-check {
      cursor: pointer;
      margin-top: 2px;
      width: 15px;
      height: 15px;
      accent-color: var(--success);
      flex-shrink: 0;
    }
    .point-bukti-item.checked label {
      text-decoration: line-through;
      color: var(--text-muted);
    }

    .note-alert {
      font-size: 0.76rem;
      padding: 8px 10px;
      border-radius: var(--radius-sm);
      margin-bottom: 10px;
      display: flex;
      align-items: flex-start;
      gap: 6px;
      line-height: 1.4;
    }
    .note-alert-danger {
      background: var(--danger-light);
      color: var(--danger);
      border: 1px solid var(--danger-border);
    }
    .note-alert-warning {
      background: var(--warning-light);
      color: var(--warning);
      border: 1px solid var(--warning-border);
    }

    .point-actions {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }
    .btn-action {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 5px 9px;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 600;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
      cursor: pointer;
      text-decoration: none;
      transition: background 0.15s ease;
    }
    .btn-action:hover {
      background: var(--bg);
    }
    .btn-action-primary {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary-border);
    }
    .btn-action-primary:hover {
      background: var(--primary);
      color: #ffffff;
    }

    .detail-section {
      font-size: 0.78rem;
      line-height: 1.4;
      color: var(--text-muted);
    }
    .detail-section-title {
      font-weight: 700;
      color: var(--text);
      margin-bottom: 2px;
    }

    /* TEMPLATE CARDS */
    .template-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 12px;
    }
    .tpl-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .tpl-card:hover {
      border-color: #cbd5e1;
    }
    .tpl-tag {
      display: inline-block;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      margin-bottom: 8px;
    }
    .tpl-tag-word { background: #dbeafe; color: #1e40af; }
    .tpl-tag-excel { background: #dcfce7; color: #166534; }
    .tpl-tag-danger { background: #fee2e2; color: #b91c1c; }
    .tpl-tag-warning { background: #fef3c7; color: #b45309; }

    .tpl-name {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 4px;
      line-height: 1.3;
    }
    .tpl-desc {
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 14px;
      line-height: 1.4;
    }
    .btn-download-tpl {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      width: 100%;
      padding: 8px 14px;
      background: var(--text);
      color: #ffffff;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 600;
      border: none;
      cursor: pointer;
      text-decoration: none;
      transition: background 0.15s;
    }
    .btn-download-tpl:hover {
      background: var(--primary);
    }

    /* DRIVE TREE CARD */
    .drive-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
    }
    .drive-code-block {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 16px;
      font-family: monospace;
      font-size: 0.82rem;
      line-height: 1.6;
      color: var(--text);
      overflow-x: auto;
      white-space: pre;
      margin-top: 14px;
    }

    /* REKAP TABLE */
    .table-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 18px;
    }
    .rekap-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
      margin-top: 12px;
    }
    .rekap-table th, .rekap-table td {
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
    }
    .rekap-table th {
      background: var(--bg);
      text-align: left;
      font-weight: 700;
      color: var(--text);
    }
    .text-center { text-align: center; }

    /* EMPTY STATE */
    .empty-box {
      text-align: center;
      padding: 40px 16px;
      color: var(--text-muted);
      background: var(--surface);
      border: 1px dashed var(--border);
      border-radius: var(--radius);
    }

    /* TOAST */
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--text);
      color: #ffffff;
      padding: 10px 18px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 600;
      z-index: 100;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.2s ease;
      pointer-events: none;
    }
    .toast.show {
      transform: translateY(0);
      opacity: 1;
    }

    /* FOOTER */
    .footer {
      border-top: 1px solid var(--border);
      background: var(--surface);
      padding: 24px 0;
      font-size: 0.8rem;
      color: var(--text-muted);
      text-align: center;
    }

    /* RESPONSIVE */
    @media (max-width: 768px) {
      .top-header-inner { height: auto; padding: 10px 0; }
      .brand-title { font-size: 0.88rem; }
      .hero-title { font-size: 1.15rem; }
      .stats-row { grid-template-columns: 1fr 1fr; }
      .tabs-nav { top: 0; }
      .dropdown-selects-grid { grid-template-columns: 1fr; }
      .pilar-summary { flex-direction: column; align-items: flex-start; gap: 8px; }
      .pilar-summary-right { width: 100%; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 6px; }
      .subpilar-summary { flex-direction: column; align-items: flex-start; gap: 6px; }
      .subpilar-summary-right { width: 100%; justify-content: space-between; }
      .point-summary { flex-direction: column; align-items: flex-start; gap: 6px; }
      .point-summary-right { width: 100%; justify-content: space-between; border-top: 1px dashed var(--border); padding-top: 4px; }
    }
    @media (max-width: 480px) {
      .stats-row { grid-template-columns: 1fr; }
      .btn-header-drive span:last-child { display: none; }
    }
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header class="top-header">
    <div class="container top-header-inner">
      <a href="#" class="brand">
        <span class="brand-icon">🏛️</span>
        <div class="brand-text">
          <div class="brand-title">BPS Kab. Kepulauan Selayar</div>
          <div class="brand-sub">Panduan Bukti Dukung ZI Menuju WBK 2025</div>
        </div>
      </a>
      <a href="https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-header-drive" title="Buka Root Google Drive Bukti Dukung">
        <span>📁</span>
        <span>Google Drive</span>
      </a>
    </div>
  </header>

  <!-- HERO & SUMMARY METRICS -->
  <section class="hero">
    <div class="container">
      <h1 class="hero-title">Panduan Penyusunan Bukti Dukung Zona Integritas</h1>
      <p class="hero-desc">Pusat kendali bukti dukung LKE 2025 BPS Kabupaten Kepulauan Selayar terstruktur: <strong>Pilar &rarr; Sub Pilar &rarr; Point-point Indikator</strong>.</p>

      <div class="stats-row">
        <!-- Skor Mandiri -->
        <div class="stat-box">
          <div class="stat-label">Nilai Evaluasi Mandiri</div>
          <div class="stat-num-row">
            <span class="stat-num" style="color: var(--primary);">46.70</span>
            <span class="stat-note">/ 100.00</span>
          </div>
          <div class="stat-bar-bg">
            <div class="stat-bar-fill" style="width: 46.7%; background: var(--primary);"></div>
          </div>
        </div>

        <!-- Komponen Pengungkit -->
        <div class="stat-box">
          <div class="stat-label">Komponen Pengungkit</div>
          <div class="stat-num-row">
            <span class="stat-num" style="color: var(--success);">46.70</span>
            <span class="stat-note">/ 60.00 (77.8%)</span>
          </div>
          <div class="stat-bar-bg">
            <div class="stat-bar-fill" style="width: 77.8%; background: var(--success);"></div>
          </div>
        </div>

        <!-- Indikator Lengkap -->
        <div class="stat-box">
          <div class="stat-label">Point Lengkap</div>
          <div class="stat-num-row">
            <span class="stat-num" style="color: var(--success);">75</span>
            <span class="stat-note">dari 110 point</span>
          </div>
          <div class="stat-bar-bg">
            <div class="stat-bar-fill" style="width: 68.2%; background: var(--success);"></div>
          </div>
        </div>

        <!-- Perlu Dilengkapi -->
        <div class="stat-box">
          <div class="stat-label">Perlu Dilengkapi</div>
          <div class="stat-num-row">
            <span class="stat-num" style="color: var(--warning);">35</span>
            <span class="stat-note">prioritas tindak lanjut</span>
          </div>
          <div class="stat-bar-bg">
            <div class="stat-bar-fill" style="width: 31.8%; background: var(--warning);"></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- NAVIGATION TABS -->
  <div class="tabs-nav">
    <div class="container">
      <nav class="tabs-scroll" aria-label="Navigasi Utama">
        <button type="button" class="tab-btn active" data-tab="bukti" onclick="switchTab('bukti')">📑 Bukti Dukung (6 Pilar)</button>
        <button type="button" class="tab-btn" data-tab="template" onclick="switchTab('template')">📥 Format &amp; Template (11)</button>
        <button type="button" class="tab-btn" data-tab="rekap" onclick="switchTab('rekap')">📊 Rekap Nilai LKE</button>
        <button type="button" class="tab-btn" data-tab="drive" onclick="switchTab('drive')">📁 Struktur Google Drive</button>
      </nav>
    </div>
  </div>

  <!-- MAIN WRAP -->
  <main class="container main-wrap">

    <!-- TAB 1: BUKTI DUKUNG -->
    <div id="tab-bukti" class="tab-content active">
      <!-- Filter Bar -->
      <div class="filter-card">
        <!-- Search Input -->
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" id="searchInput" class="search-input" placeholder="Cari bukti dukung, SOP, SK, notula, kode (misal: 1.a), atau kata kunci..." oninput="onSearchChange(this.value)">
        </div>

        <!-- Cascading Select Dropdowns: Pilar -> Sub Pilar -> Status -->
        <div class="dropdown-selects-grid">
          <div class="select-wrap">
            <label for="selectPilar" class="select-label">1. Pilih Pilar (Area):</label>
            <select id="selectPilar" class="select-input" onchange="onPilarSelect(this.value)">
              <option value="all">🏢 Semua Pilar (1 s/d 6)</option>
              <option value="1">Pilar 1: Manajemen Perubahan (16 Point)</option>
              <option value="2">Pilar 2: Penataan Tatalaksana (15 Point)</option>
              <option value="3">Pilar 3: Penataan Sistem Manajemen SDM (21 Point)</option>
              <option value="4">Pilar 4: Penguatan Akuntabilitas Kinerja (14 Point)</option>
              <option value="5">Pilar 5: Penguatan Pengawasan (22 Point)</option>
              <option value="6">Pilar 6: Peningkatan Kualitas Pelayanan Publik (22 Point)</option>
            </select>
          </div>

          <div class="select-wrap">
            <label for="selectSubPilar" class="select-label">2. Pilih Sub Pilar:</label>
            <select id="selectSubPilar" class="select-input" onchange="onSubPilarSelect(this.value)">
              <option value="all">📁 Semua Sub Pilar</option>
            </select>
          </div>

          <div class="select-wrap">
            <label for="selectStatus" class="select-label">3. Status Point:</label>
            <select id="selectStatus" class="select-input" onchange="onStatusSelect(this.value)">
              <option value="all">🔍 Semua Status</option>
              <option value="attention">⚠️ Perlu Dilengkapi (35 Point)</option>
              <option value="complete">✅ Lengkap (75 Point)</option>
            </select>
          </div>
        </div>

        <div class="filter-actions-row">
          <div style="display: flex; gap: 6px; flex-wrap: wrap;">
            <button type="button" class="btn-toggle-tree" onclick="toggleAllLevels(true)" title="Buka seluruh pilar, sub pilar, dan point">▼ Buka Semua</button>
            <button type="button" class="btn-toggle-tree" onclick="toggleAllLevels(false)" title="Tutup semua dropdown ke tingkat terluar">▲ Tutup Semua</button>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 0.74rem; color: var(--text-muted);" id="checkedCount">0 berkas dicentang</span>
            <button type="button" class="btn-reset-checks" onclick="resetChecks()" title="Reset semua tanda centang verifikasi checklist">🔄 Reset Centang</button>
          </div>
        </div>
      </div>

      <!-- Result Info -->
      <div class="result-info">
        <span id="resultCount">Menampilkan 6 Pilar, 42 Sub Pilar, 110 Point</span>
        <span style="font-size: 0.74rem; color: var(--text-muted);">💡 Klik baris untuk membuka dropdown hirarki</span>
      </div>

      <!-- 3-TIER HIERARCHICAL TREE CONTAINER -->
      <div id="treeContainer" class="tree-container"></div>
    </div>

    <!-- TAB 2: FORMAT & TEMPLATE -->
    <div id="tab-template" class="tab-content">
      <div style="margin-bottom: 14px;">
        <h2 style="font-size: 1.15rem; font-weight: 800; color: var(--text);">📥 Format &amp; Template Resmi Siap Pakai</h2>
        <p style="font-size: 0.82rem; color: var(--text-muted);">Format dokumen baku bertuliskan kop resmi <strong>Badan Pusat Statistik Kabupaten Kepulauan Selayar</strong> untuk memenuhi bukti dukung LKE 2025.</p>
      </div>

      <!-- Banner Download Semua -->
      <div style="background: var(--primary-light); border: 1px solid var(--primary-border); border-radius: var(--radius); padding: 16px; margin-bottom: 16px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
        <div>
          <div style="font-size: 0.95rem; font-weight: 800; color: var(--primary);">📦 Paket Lengkap Bukti Dukung 6 Area (ZIP)</div>
          <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 2px;">Memuat seluruh 110 folder indikator, 119 dokumen Word (.docx), master checklist Excel, dan panduan resmi pemetaan BPS RI.</div>
        </div>
        <a href="templates/Bukti_Dukung_ZI_BPS_Kepulauan_Selayar_2025_LENGKAP.zip" download class="btn-download-tpl" style="width: auto; padding: 10px 18px; background: var(--primary);">
          <span>⚡</span><span>Unduh Paket Lengkap .ZIP (5 MB)</span>
        </a>
      </div>

      <div class="template-grid">
        <!-- Template 0: Master Checklist Excel -->
        <div class="tpl-card" style="border-left: 4px solid var(--success);">
          <div>
            <span class="tpl-tag tpl-tag-excel">EXCEL (.XLSX) • MASTER CHECKLIST</span>
            <div class="tpl-name">📊 Master Checklist &amp; Nilai LKE 2025</div>
            <div class="tpl-desc">Buku kerja Excel berisi lembar Ringkasan Nilai 6 Area dan lembar Checklist 110 indikator bukti dukung lengkap dengan formula capaian.</div>
          </div>
          <a href="templates/Checklist_Bukti_Dukung_ZI_BPS_Kepulauan_Selayar_2025.xlsx" download class="btn-download-tpl" style="background: var(--success);">
            <span>⬇️</span><span>Unduh Excel (.xlsx)</span>
          </a>
        </div>

        <!-- Template 1: SK Tim Kerja ZI -->
        <div class="tpl-card">
          <div>
            <span class="tpl-tag tpl-tag-word">AREA 1 • WORD (.DOCX)</span>
            <div class="tpl-name">Format 01: SK Tim Pembangunan ZI 2025</div>
            <div class="tpl-desc">Keputusan Kepala BPS Kab. Kepulauan Selayar tentang Pembentukan Tim Kerja ZI Menuju WBK/WBBM beserta lampiran koordinator 6 Area.</div>
          </div>
          <a href="templates/Format_01_SK_Tim_Pembangunan_ZI_2025_BPS_Selayar.docx" download class="btn-download-tpl">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 2: Notula Rapat Pembentukan Tim -->
        <div class="tpl-card">
          <div>
            <span class="tpl-tag tpl-tag-word">AREA 1 • WORD (.DOCX)</span>
            <div class="tpl-name">Format 02: Notula Pemilihan Anggota Tim</div>
            <div class="tpl-desc">Risalah rapat pembentukan tim, kriteria objektif pemilihan, dan mekanisme penunjukan anggota yang mewakili seluruh fungsi.</div>
          </div>
          <a href="templates/Format_02_Notula_Rapat_Pembentukan_Tim_ZI_BPS_Selayar.docx" download class="btn-download-tpl">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 3: Benturan Kepentingan -->
        <div class="tpl-card" style="border-left: 4px solid var(--danger);">
          <div>
            <span class="tpl-tag tpl-tag-danger">AREA 5 • PRIORITAS KRITIS</span>
            <div class="tpl-name">Format 03: Pernyataan Bebas Benturan Kepentingan</div>
            <div class="tpl-desc">Sesuai Perka BPS No. 36/2023. Wajib ditandatangani PPK, Pejabat Pengadaan, Panitia Rekrutmen Mitra, dan Pimpinan.</div>
          </div>
          <a href="templates/Format_03_Surat_Pernyataan_Bebas_Benturan_Kepentingan_BPS_Selayar.docx" download class="btn-download-tpl" style="background: var(--danger);">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 4: Laporan Monev ZI -->
        <div class="tpl-card">
          <div>
            <span class="tpl-tag tpl-tag-word">AREA 1 • WORD (.DOCX)</span>
            <div class="tpl-name">Format 04: Laporan Monev ZI Triwulanan</div>
            <div class="tpl-desc">Laporan monitoring berkala per triwulan yang memuat analisa kendala, capaian matriks aksi, dan arahan tindak lanjut pimpinan.</div>
          </div>
          <a href="templates/Format_04_Laporan_Monev_ZI_Triwulan_BPS_Selayar.docx" download class="btn-download-tpl">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 5: Pakta Integritas -->
        <div class="tpl-card">
          <div>
            <span class="tpl-tag tpl-tag-word">AREA 1 &amp; 5 • WORD (.DOCX)</span>
            <div class="tpl-name">Format 05: Pakta Integritas Pegawai ZI 2025</div>
            <div class="tpl-desc">Komitmen bersama pencegahan KKN, penolakan suap/gratifikasi, dan kepatuhan Core Values BerAKHLAK seluruh pegawai Selayar.</div>
          </div>
          <a href="templates/Format_05_Pakta_Integritas_Pegawai_BPS_Selayar.docx" download class="btn-download-tpl">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 6: Reward Punishment PST -->
        <div class="tpl-card" style="border-left: 4px solid var(--warning);">
          <div>
            <span class="tpl-tag tpl-tag-warning">AREA 6 • PRIORITAS</span>
            <div class="tpl-name">Format 06: Reward &amp; Punishment Petugas Layanan</div>
            <div class="tpl-desc">Pedoman penilaian berkala petugas loket Pelayanan Statistik Terpadu (PST) berdasarkan kepuasan tamu dan disiplin.</div>
          </div>
          <a href="templates/Format_06_Pedoman_Reward_Punishment_Petugas_Layanan_BPS_Selayar.docx" download class="btn-download-tpl" style="background: var(--warning);">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 7: Role Model Pimpinan -->
        <div class="tpl-card">
          <div>
            <span class="tpl-tag tpl-tag-word">AREA 1 • WORD (.DOCX)</span>
            <div class="tpl-name">Format 07: Laporan Penerapan Role Model Pimpinan</div>
            <div class="tpl-desc">Dokumentasi keteladanan pimpinan satker dalam penerapan nilai BerAKHLAK, kehadiran apel pagi, dan kepatuhan LHKPN.</div>
          </div>
          <a href="templates/Format_07_Laporan_Penerapan_Role_Model_Pimpinan_BPS_Selayar.docx" download class="btn-download-tpl">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 8: Agen Perubahan -->
        <div class="tpl-card">
          <div>
            <span class="tpl-tag tpl-tag-word">AREA 1 • WORD (.DOCX)</span>
            <div class="tpl-name">Format 08: Laporan Agen Perubahan (Change Agent)</div>
            <div class="tpl-desc">Laporan hasil inovasi nyata agen perubahan yang terintegrasi ke dalam sistem operasional BPS Kab. Kepulauan Selayar.</div>
          </div>
          <a href="templates/Format_08_Laporan_Agen_Perubahan_BPS_Selayar.docx" download class="btn-download-tpl">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 9: Evaluasi SOP -->
        <div class="tpl-card">
          <div>
            <span class="tpl-tag tpl-tag-word">AREA 2 • WORD (.DOCX)</span>
            <div class="tpl-name">Format 09: Kertas Kerja Evaluasi &amp; Reviu SOP</div>
            <div class="tpl-desc">Format kertas kerja evaluasi tahunan SOP administrasi pemerintahan sesuai Perka BPS No. 19 Tahun 2013.</div>
          </div>
          <a href="templates/Format_09_Kertas_Kerja_Evaluasi_SOP_BPS_Selayar.docx" download class="btn-download-tpl">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>

        <!-- Template 10: Pengaduan & WBS -->
        <div class="tpl-card" style="border-left: 4px solid var(--danger);">
          <div>
            <span class="tpl-tag tpl-tag-danger">AREA 5 • PRIORITAS KRITIS</span>
            <div class="tpl-name">Format 10: Laporan Pengaduan Masyarakat &amp; WBS</div>
            <div class="tpl-desc">Laporan pengelolaan saluran aduan SP4N-LAPOR!, kotak aduan, dan WBS (termasuk format Surat Keterangan Nihil Aduan).</div>
          </div>
          <a href="templates/Format_10_Laporan_Pengelolaan_Pengaduan_dan_WBS_BPS_Selayar.docx" download class="btn-download-tpl" style="background: var(--danger);">
            <span>⬇️</span><span>Unduh Word (.docx)</span>
          </a>
        </div>
      </div>
    </div>

    <!-- TAB 3: REKAP NILAI LKE -->
    <div id="tab-rekap" class="tab-content">
      <div class="table-card">
        <h2 style="font-size: 1.15rem; font-weight: 800; color: var(--text); margin-bottom: 4px;">📊 Rekapitulasi Nilai LKE Zona Integritas 2025</h2>
        <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 14px;">Evaluasi mandiri komponen pengungkit dan hasil BPS Kabupaten Kepulauan Selayar.</p>

        <div style="overflow-x: auto;">
          <table class="rekap-table">
            <thead>
              <tr>
                <th style="width: 40px;" class="text-center">No</th>
                <th>Pilar / Area Perubahan</th>
                <th style="width: 80px;" class="text-center">Bobot</th>
                <th style="width: 100px;" class="text-center">Pemenuhan</th>
                <th style="width: 90px;" class="text-center">Reform</th>
                <th style="width: 90px;" class="text-center">Total</th>
                <th style="width: 90px;" class="text-center">% Capaian</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-center">1</td>
                <td><strong>Pilar 1: Manajemen Perubahan</strong></td>
                <td class="text-center">8.00</td>
                <td class="text-center">2.54</td>
                <td class="text-center">4.00</td>
                <td class="text-center"><strong>6.54</strong></td>
                <td class="text-center" style="color: var(--success); font-weight: 700;">81.75%</td>
              </tr>
              <tr>
                <td class="text-center">2</td>
                <td><strong>Pilar 2: Penataan Tatalaksana</strong></td>
                <td class="text-center">7.00</td>
                <td class="text-center">3.38</td>
                <td class="text-center">3.50</td>
                <td class="text-center"><strong>6.88</strong></td>
                <td class="text-center" style="color: var(--success); font-weight: 700;">98.29%</td>
              </tr>
              <tr>
                <td class="text-center">3</td>
                <td><strong>Pilar 3: Penataan Sistem Manajemen SDM</strong></td>
                <td class="text-center">10.00</td>
                <td class="text-center">3.96</td>
                <td class="text-center">3.50</td>
                <td class="text-center"><strong>7.46</strong></td>
                <td class="text-center" style="color: var(--warning); font-weight: 700;">74.60%</td>
              </tr>
              <tr>
                <td class="text-center">4</td>
                <td><strong>Pilar 4: Penguatan Akuntabilitas Kinerja</strong></td>
                <td class="text-center">10.00</td>
                <td class="text-center">5.00</td>
                <td class="text-center">3.50</td>
                <td class="text-center"><strong>8.50</strong></td>
                <td class="text-center" style="color: var(--success); font-weight: 700;">85.00%</td>
              </tr>
              <tr>
                <td class="text-center">5</td>
                <td><strong>Pilar 5: Penguatan Pengawasan</strong></td>
                <td class="text-center">15.00</td>
                <td class="text-center">3.38</td>
                <td class="text-center">7.50</td>
                <td class="text-center"><strong>10.88</strong></td>
                <td class="text-center" style="color: var(--warning); font-weight: 700;">72.53%</td>
              </tr>
              <tr>
                <td class="text-center">6</td>
                <td><strong>Pilar 6: Peningkatan Kualitas Pelayanan Publik</strong></td>
                <td class="text-center">10.00</td>
                <td class="text-center">3.95</td>
                <td class="text-center">2.50</td>
                <td class="text-center"><strong>6.45</strong></td>
                <td class="text-center" style="color: var(--warning); font-weight: 700;">64.50%</td>
              </tr>
              <tr style="background: var(--bg); font-weight: 700;">
                <td colspan="2">A. TOTAL KOMPONEN PENGUNGKIT</td>
                <td class="text-center">60.00</td>
                <td class="text-center">22.20</td>
                <td class="text-center">24.50</td>
                <td class="text-center" style="color: var(--success);">46.70</td>
                <td class="text-center" style="color: var(--success);">77.83%</td>
              </tr>
              <tr style="color: var(--text-muted);">
                <td colspan="2">B. KOMPONEN HASIL (Menunggu Survei Eksternal IPAK &amp; IPKP)</td>
                <td class="text-center">40.00</td>
                <td class="text-center">0.00</td>
                <td class="text-center">0.00</td>
                <td class="text-center">0.00</td>
                <td class="text-center">0.00%</td>
              </tr>
              <tr style="background: var(--text); color: #ffffff; font-weight: 800;">
                <td colspan="2">TOTAL EVALUASI MANDIRI SATKER</td>
                <td class="text-center">100.00</td>
                <td class="text-center">22.20</td>
                <td class="text-center">24.50</td>
                <td class="text-center" style="color: #fde68a;">46.70</td>
                <td class="text-center" style="color: #fde68a;">46.70%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 4: STRUKTUR GOOGLE DRIVE -->
    <div id="tab-drive" class="tab-content">
      <div class="drive-card">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
          <div>
            <h2 style="font-size: 1.15rem; font-weight: 800; color: var(--text);">📁 Struktur Standar Folder Google Drive</h2>
            <p style="font-size: 0.82rem; color: var(--text-muted);">Struktur folder baku untuk mempermudah pemeriksaan oleh TPI BPS dan TPN KemenPAN-RB.</p>
          </div>
          <a href="https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-action btn-action-primary">
            <span>↗️</span><span>Buka Root Drive Selayar</span>
          </a>
        </div>

        <div class="drive-code-block">📁 [ROOT] ZI / Bukti Dukung ZI 2025 BPS Kab. Kepulauan Selayar
│
├── 📁 Bukti_Dukung_Selayar_2025/ (Template Dokumen Resmi Selayar)
│   ├── 📁 01_Manajemen_Perubahan/ (SK Tim, Prosedur Pemilihan, Rencana Kerja, Monev TW)
│   ├── 📁 02_Penataan_Tatalaksana/ (SOP Administrasi, Pemanfaatan TI, SPBE)
│   ├── 📁 03_Penataan_Sistem_Manajemen_SDM/ (ABK, Mutasi, Diklat 20JP, Reward)
│   ├── 📁 04_Penguatan_Akuntabilitas/ (SMART, LAKIN Tepat Waktu, IKU)
│   ├── 📁 05_Penguatan_Pengawasan/ (SPIP Risiko, Pengaduan, Benturan Kepentingan)
│   └── 📁 06_Peningkatan_Pelayanan_Publik/ (Standar Pelayanan, FKP, PST, SKD)
│
└── 📁 Contoh_Bukti_Dukung_Pusat/ (378 Berkas Dokumen Contoh Asli BPS Pusat - 1.1 GB)
    ├── 📁 Pilar_1_Manajemen_Perubahan/ (28 file - 44.9 MB)
    ├── 📁 Pilar_2_Penataan_Tatalaksana/ (109 file - 229.9 MB)
    ├── 📁 Pilar_3_Penataan_Sistem_Manajemen_SDM_Aparatur/ (99 file - 627.1 MB)
    ├── 📁 Pilar_4_Penguatan_Akuntabilitas/ (28 file - 24.4 MB)
    ├── 📁 Pilar_5_Penguatan_Pengawasan/ (49 file - 91.0 MB)
    └── 📁 Pilar_6_Peningkatan_Kualitas_Pelayanan_Publik/ (65 file - 86.2 MB)</div>
      </div>
    </div>

  </main>

  <!-- TOAST NOTIFICATION -->
  <div id="toast" class="toast">Daftar berkas disalin ke clipboard!</div>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <div><strong>Badan Pusat Statistik Kabupaten Kepulauan Selayar</strong></div>
      <div style="margin-top: 4px;">Jl. Ahmad Yani No. 12, Benteng, Kepulauan Selayar, Sulawesi Selatan 92812 • Telepon: (0414) 21102</div>
      <div style="margin-top: 4px; font-size: 0.74rem; color: #94a3b8;">Sistem Panduan Bukti Dukung ZI Menuju Wilayah Bebas dari Korupsi (WBK) 2025</div>
    </div>
  </footer>

  <script>
    // Hierarchical dataset: Pilar -> Sub Pilar -> Points
    const PILARS = ''' + pilars_json_str + ''';
    const ALL_POINTS = ''' + flat_points_json_str + ''';

    // State
    let selectedPilar = 'all';
    let selectedSubPilar = 'all';
    let selectedStatus = 'all';
    let searchQuery = '';
    let checks = JSON.parse(localStorage.getItem('zi_checks_selayar') || '{}');

    // Switch Tab
    function switchTab(name) {
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-tab') === name);
      });
      document.querySelectorAll('.tab-content').forEach(pane => {
        pane.classList.toggle('active', pane.id === 'tab-' + name);
      });
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Populate Sub Pilar options based on chosen Pilar
    function updateSubPilarOptions() {
      const spSelect = document.getElementById('selectSubPilar');
      if (!spSelect) return;

      spSelect.innerHTML = '<option value="all">📁 Semua Sub Pilar</option>';
      
      let candidateSubpilars = [];
      if (selectedPilar === 'all') {
        PILARS.forEach(p => {
          p.subpilars.forEach(sp => candidateSubpilars.push({ pilar: p.number, ...sp }));
        });
      } else {
        const p = PILARS.find(x => String(x.number) === selectedPilar);
        if (p) {
          p.subpilars.forEach(sp => candidateSubpilars.push({ pilar: p.number, ...sp }));
        }
      }

      candidateSubpilars.forEach(sp => {
        const opt = document.createElement('option');
        opt.value = sp.id;
        const prefix = selectedPilar === 'all' ? `[Pilar ${sp.pilar}] ` : '';
        opt.textContent = `${prefix}${sp.aspect}: ${sp.name} (${sp.points.length} pt)`;
        spSelect.appendChild(opt);
      });

      spSelect.value = selectedSubPilar;
      // If previous value no longer exists, reset to 'all'
      if (spSelect.value !== selectedSubPilar) {
        selectedSubPilar = 'all';
        spSelect.value = 'all';
      }
    }

    // Filter handlers
    function onPilarSelect(pNum) {
      selectedPilar = pNum;
      selectedSubPilar = 'all';
      updateSubPilarOptions();
      renderTree();
    }

    function onSubPilarSelect(spId) {
      selectedSubPilar = spId;
      renderTree();
    }

    function onStatusSelect(st) {
      selectedStatus = st;
      renderTree();
    }

    function onSearchChange(val) {
      searchQuery = (val || '').toLowerCase().trim();
      renderTree();
    }

    // Toggle All Levels
    function toggleAllLevels(open) {
      document.querySelectorAll('.pilar-dropdown').forEach(d => d.open = open);
      document.querySelectorAll('.subpilar-dropdown').forEach(d => d.open = open);
      document.querySelectorAll('.point-dropdown').forEach(d => d.open = open);
    }

    // Checklist toggles
    function toggleCheck(id) {
      const cb = document.getElementById(id);
      if (cb) {
        checks[id] = cb.checked;
        localStorage.setItem('zi_checks_selayar', JSON.stringify(checks));
        const item = cb.closest('.point-bukti-item');
        if (item) item.classList.toggle('checked', cb.checked);
        updateCheckedCounter();
      }
    }

    function resetChecks() {
      if (confirm('Hapus semua tanda centang verifikasi checklist bukti dukung?')) {
        checks = {};
        localStorage.removeItem('zi_checks_selayar');
        renderTree();
        showToast('Semua centang verifikasi berhasil direset');
      }
    }

    function updateCheckedCounter() {
      const count = Object.values(checks).filter(Boolean).length;
      const el = document.getElementById('checkedCount');
      if (el) el.textContent = count + ' berkas dicentang';
    }

    // Toast
    function showToast(msg) {
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2500);
    }

    // Copy Bukti
    function copyBukti(code) {
      const itm = ALL_POINTS.find(x => x.code === code);
      if (!itm) return;
      const lines = ['Bukti Dukung Indikator ' + code + ' (' + itm.question + ') - BPS Selayar:'];
      (itm.bukti || []).forEach(b => lines.push('• ' + b));
      navigator.clipboard.writeText(lines.join('\\n')).then(() => {
        showToast('Daftar berkas ' + code + ' disalin ke clipboard');
      }).catch(() => {
        showToast('Gagal menyalin');
      });
    }

    // Render 3-Tier Tree
    function renderTree() {
      const container = document.getElementById('treeContainer');
      if (!container) return;

      const hasSearch = searchQuery.length > 0;
      let totalVisiblePoints = 0;
      let totalVisibleSubpilars = 0;
      let totalVisiblePilars = 0;

      let html = '';

      PILARS.forEach(pilar => {
        // Filter Pilar
        if (selectedPilar !== 'all' && String(pilar.number) !== selectedPilar) {
          return;
        }

        let pilarPointsCount = 0;
        let subpilarsHtml = '';

        pilar.subpilars.forEach(sp => {
          // Filter Sub Pilar
          if (selectedSubPilar !== 'all' && sp.id !== selectedSubPilar) {
            return;
          }

          // Filter Points inside Sub Pilar
          const filteredPoints = sp.points.filter(pt => {
            // Status filter
            const isComp = pt.status === 'complete' && ['1.00', '1', '300.00%', '100.00%', '105.74%'].includes(pt.nilai);
            if (selectedStatus === 'complete' && !isComp) return false;
            if (selectedStatus === 'attention' && isComp) return false;

            // Search filter
            if (hasSearch) {
              const text = [
                pt.code,
                pt.question,
                pt.subPilarName,
                pt.pilarTitle,
                pt.catatan,
                pt.narasi,
                ...(pt.bukti || [])
              ].join(' ').toLowerCase();
              if (!text.includes(searchQuery)) return false;
            }

            return true;
          });

          if (filteredPoints.length === 0) return;

          pilarPointsCount += filteredPoints.length;
          totalVisiblePoints += filteredPoints.length;
          totalVisibleSubpilars++;

          // Build Points HTML (Level 3)
          let pointsHtml = '';
          filteredPoints.forEach(pt => {
            const safe = pt.code.replace(/[^a-zA-Z0-9]/g, '_');
            const isComp = pt.status === 'complete' && ['1.00', '1', '300.00%', '100.00%', '105.74%'].includes(pt.nilai);
            const isMiss = pt.status === 'missing' || pt.nilai === '0.00';

            const cardState = isMiss ? 'state-missing' : (isComp ? 'state-complete' : 'state-partial');
            const badgeState = isMiss ? 'badge-state-missing' : (isComp ? 'badge-state-complete' : 'badge-state-partial');

            let badgeText = isMiss ? '⚠️ Perlu Dilengkapi (0.00)' : (isComp ? '✅ Lengkap (1.00)' : '🟡 Sebagian (' + pt.nilai + ')');
            if (pt.nilai === '105.74%') badgeText = '✅ Capaian 105.74%';
            if (pt.nilai === '300.00%') badgeText = '✅ Capaian 300%';

            // Bukti list
            let buktiRows = '';
            if (pt.bukti && pt.bukti.length > 0) {
              buktiRows = pt.bukti.map((b, idx) => {
                const checkId = 'chk_' + pt.pilarNum + '_' + safe + '_' + idx;
                const checked = !!checks[checkId];
                return `
                  <li class="point-bukti-item ${checked ? 'checked' : ''}">
                    <input type="checkbox" id="${checkId}" class="point-check" ${checked ? 'checked' : ''} onchange="toggleCheck('${checkId}')">
                    <label for="${checkId}" style="cursor: pointer; flex: 1;">${b}</label>
                  </li>
                `;
              }).join('');
            } else {
              buktiRows = '<li class="point-bukti-item" style="color: var(--text-muted); font-style: italic;">Tidak ada dokumen khusus tercatat</li>';
            }

            // Note alert
            let noteHtml = '';
            if (pt.catatan) {
              const isDanger = pt.nilai === '0.00';
              noteHtml = `
                <div class="note-alert ${isDanger ? 'note-alert-danger' : 'note-alert-warning'}">
                  <span>⚠️</span>
                  <div>${pt.catatan}</div>
                </div>
              `;
            }

            // Link contoh
            let linkContohBtn = '';
            if (pt.link_contoh) {
              linkContohBtn = `
                <a href="${pt.link_contoh}" target="_blank" rel="noopener noreferrer" class="btn-action btn-action-primary" title="Lihat contoh format resmi BPS Pusat">
                  <span>🔗</span><span>Contoh Pusat</span>
                </a>
              `;
            }

            // Open point if searching
            const isPointOpen = hasSearch;

            pointsHtml += `
              <details class="point-dropdown ${cardState}" id="point-${safe}" ${isPointOpen ? 'open' : ''}>
                <summary class="point-summary">
                  <div class="point-summary-left">
                    <span class="point-code">${pt.code}</span>
                    <span class="point-question">${pt.question}</span>
                  </div>
                  <div class="point-summary-right">
                    <span class="badge-status ${badgeState}">${badgeText}</span>
                    <span style="font-size: 0.72rem; color: var(--text-muted); font-weight: 600;">${(pt.bukti || []).length} berkas</span>
                    <span class="chevron-icon">▼</span>
                  </div>
                </summary>

                <div class="point-body">
                  <div class="point-bukti-box">
                    <div class="point-bukti-top">
                      <span>Daftar Bukti Dukung yang Wajib Diunggah:</span>
                      <span style="font-size: 0.68rem; text-transform: none;">centang jika siap</span>
                    </div>
                    <ul class="point-bukti-list">
                      ${buktiRows}
                    </ul>
                  </div>

                  ${noteHtml}

                  <div class="point-actions">
                    <a href="https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-action" title="Folder Drive: ${pt.drive_folder || 'Root'}">
                      <span>📁</span><span>Folder Drive</span>
                    </a>
                    ${linkContohBtn}
                    <button type="button" class="btn-action" onclick="copyBukti('${pt.code}')">
                      <span>📋</span><span>Salin Berkas</span>
                    </button>
                  </div>

                  <div class="detail-section">
                    <div class="detail-section-title">Kriteria Penilaian:</div>
                    <div style="white-space: pre-line;">${pt.kriteria || '-'}</div>
                  </div>
                  <div class="detail-section" style="margin-top: 6px;">
                    <span class="detail-section-title">Jawaban &amp; Nilai Satker:</span>
                    <span>Jawaban: <strong>${pt.jawaban || '-'}</strong> (Nilai: <strong>${pt.nilai}</strong>)</span>
                  </div>
                  ${pt.narasi ? `
                    <div class="detail-section" style="margin-top: 6px;">
                      <div class="detail-section-title">Narasi / Catatan Satker:</div>
                      <div style="font-style: italic; background: var(--bg); padding: 6px 10px; border-radius: var(--radius-sm); border-left: 2px solid var(--border);">${pt.narasi}</div>
                    </div>
                  ` : ''}
                </div>
              </details>
            `;
          });

          // Open subpilar if search or specific subpilar chosen
          const isSubPilarOpen = hasSearch || selectedSubPilar !== 'all';
          const aspectClass = sp.aspect === 'Pemenuhan' ? 'aspect-pemenuhan' : 'aspect-reform';

          subpilarsHtml += `
            <details class="subpilar-dropdown" id="subpilar-${sp.id}" ${isSubPilarOpen ? 'open' : ''}>
              <summary class="subpilar-summary">
                <div class="subpilar-summary-left">
                  <span class="aspect-badge ${aspectClass}">${sp.aspect}</span>
                  <span class="subpilar-title">${sp.name}</span>
                </div>
                <div class="subpilar-summary-right">
                  <span class="subpilar-count">${filteredPoints.length} Point</span>
                  <span class="chevron-icon">▼</span>
                </div>
              </summary>
              <div class="subpilar-body">
                ${pointsHtml}
              </div>
            </details>
          `;
        });

        if (pilarPointsCount === 0) return;

        totalVisiblePilars++;

        // Open pilar if search or specific pilar chosen
        const isPilarOpen = hasSearch || selectedPilar !== 'all';

        html += `
          <details class="pilar-dropdown" id="pilar-${pilar.number}" ${isPilarOpen ? 'open' : ''}>
            <summary class="pilar-summary">
              <div class="pilar-summary-left">
                <span class="pilar-badge">PILAR ${pilar.number}</span>
                <div>
                  <div class="pilar-title">${pilar.title}</div>
                  <div class="pilar-sub">${pilar.subpilars.length} Sub Pilar • ${pilar.totalPoints} Point Bukti Dukung</div>
                </div>
              </div>
              <div class="pilar-summary-right">
                <span class="pilar-stat-pill stat-complete">${pilar.completePoints} Lengkap</span>
                <span class="pilar-stat-pill stat-attention">${pilar.attentionPoints} Perlu Dilengkapi</span>
                <span class="pilar-score-pill">${pilar.scorePct}</span>
                <span class="chevron-icon">▼</span>
              </div>
            </summary>
            <div class="pilar-body">
              ${subpilarsHtml}
            </div>
          </details>
        `;
      });

      // Update counter
      document.getElementById('resultCount').textContent = `Menampilkan ${totalVisiblePilars} Pilar, ${totalVisibleSubpilars} Sub Pilar, ${totalVisiblePoints} Point Indikator`;
      updateCheckedCounter();

      if (totalVisiblePoints === 0) {
        container.innerHTML = `
          <div class="empty-box">
            <div style="font-size: 1.8rem; margin-bottom: 6px;">🔍</div>
            <div style="font-weight: 700; color: var(--text); margin-bottom: 4px;">Tidak ada point indikator yang cocok</div>
            <div style="font-size: 0.8rem;">Coba sesuaikan kata kunci pencarian atau ubah filter pilar/status.</div>
          </div>
        `;
        return;
      }

      container.innerHTML = html;
    }

    // Prevent nested <details> toggle conflict: clicking a child summary
    // must not bubble up and toggle parent details elements.
    document.addEventListener('click', (e) => {
      if (e.target.matches('summary') || e.target.closest('summary')) {
        e.stopPropagation();
      }
    });

    // Init
    document.addEventListener('DOMContentLoaded', () => {
      updateSubPilarOptions();
      renderTree();
    });
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("index.html updated to 3-tier hierarchy: Pilar -> Sub Pilar -> Point!")
