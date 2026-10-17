import json
import re

with open("data.json", "r", encoding="utf-8") as f:
    app_data = json.load(f)

# Flatten indicators
indicators = []
for area in app_data["areas"]:
    # Pemenuhan
    for grp in area["pemenuhan"]["groups"]:
        for itm in grp["items"]:
            indicators.append({
                "areaNum": area["number"],
                "areaTitle": area["title"],
                "aspect": "Pemenuhan",
                "groupName": grp["name"],
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
            })
    # Reform
    for grp in area["reform"]["groups"]:
        for itm in grp["items"]:
            indicators.append({
                "areaNum": area["number"],
                "areaTitle": area["title"],
                "aspect": "Reform",
                "groupName": grp["name"],
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
            })

# Verify stats
total_indicators = len(indicators)
complete_indicators = sum(1 for x in indicators if x["status"] == "complete" and x["nilai"] in ["1.00", "1", "300.00%", "100.00%", "105.74%"])
attention_indicators = total_indicators - complete_indicators
print(f"Total: {total_indicators}, Complete: {complete_indicators}, Attention: {attention_indicators}")

# Count per area
area_counts = {}
for i in range(1, 7):
    area_counts[i] = {
        "total": sum(1 for x in indicators if x["areaNum"] == i),
        "complete": sum(1 for x in indicators if x["areaNum"] == i and x["status"] == "complete" and x["nilai"] in ["1.00", "1", "300.00%", "100.00%", "105.74%"]),
        "attention": sum(1 for x in indicators if x["areaNum"] == i and not (x["status"] == "complete" and x["nilai"] in ["1.00", "1", "300.00%", "100.00%", "105.74%"]))
    }
print("Area counts:", area_counts)

# Now generate index.html cleanly
data_json_str = json.dumps(indicators, ensure_ascii=False)

html_content = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panduan Bukti Dukung ZI WBK 2025 | BPS Kabupaten Kepulauan Selayar</title>
  <meta name="description" content="Sistem Panduan dan Kendali Bukti Dukung Lembar Kerja Evaluasi (LKE) Pembangunan Zona Integritas BPS Kabupaten Kepulauan Selayar.">
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

    /* FILTER BAR */
    .filter-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 14px;
      margin-bottom: 16px;
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

    .filter-row {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .filter-label {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-right: 4px;
      flex-shrink: 0;
    }
    .chip {
      padding: 5px 12px;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 600;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }
    .chip:hover {
      border-color: var(--text-muted);
      color: var(--text);
    }
    .chip.active {
      background: var(--primary);
      border-color: var(--primary);
      color: #ffffff;
    }
    .chip-warning.active {
      background: var(--warning);
      border-color: var(--warning);
      color: #ffffff;
    }
    .chip-success.active {
      background: var(--success);
      border-color: var(--success);
      color: #ffffff;
    }
    .btn-reset-checks {
      margin-left: auto;
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

    /* RESULT BAR */
    .result-info {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      font-size: 0.8rem;
      color: var(--text-muted);
      padding: 0 2px;
    }

    /* INDICATOR CARD */
    .ind-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      margin-bottom: 12px;
      transition: border-color 0.15s ease;
    }
    .ind-card:hover {
      border-color: #cbd5e1;
    }
    .ind-card.state-missing {
      border-left: 4px solid var(--danger);
    }
    .ind-card.state-partial {
      border-left: 4px solid var(--warning);
    }
    .ind-card.state-complete {
      border-left: 4px solid var(--success);
    }

    .ind-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 8px;
      flex-wrap: wrap;
    }
    .ind-tags {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .code-tag {
      font-size: 0.75rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      background: var(--bg);
      color: var(--text);
      border: 1px solid var(--border);
    }
    .area-tag {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    .badge-status {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      white-space: nowrap;
    }
    .badge-state-complete {
      background: var(--success-light);
      color: var(--success);
      border: 1px solid var(--success-border);
    }
    .badge-state-missing {
      background: var(--danger-light);
      color: var(--danger);
      border: 1px solid var(--danger-border);
    }
    .badge-state-partial {
      background: var(--warning-light);
      color: var(--warning);
      border: 1px solid var(--warning-border);
    }

    .ind-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text);
      line-height: 1.4;
      margin-bottom: 12px;
    }

    /* BUKTI LIST */
    .ind-bukti-box {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 12px;
      margin-bottom: 12px;
    }
    .ind-bukti-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }
    .ind-bukti-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .ind-bukti-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.82rem;
      color: var(--text);
      line-height: 1.4;
    }
    .ind-check {
      cursor: pointer;
      margin-top: 2px;
      width: 16px;
      height: 16px;
      accent-color: var(--success);
      flex-shrink: 0;
    }
    .ind-bukti-item.checked label {
      text-decoration: line-through;
      color: var(--text-muted);
    }

    /* NOTES BOX */
    .note-alert {
      font-size: 0.78rem;
      padding: 9px 12px;
      border-radius: var(--radius-sm);
      margin-bottom: 12px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
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

    /* ACTION BUTTONS */
    .ind-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      padding-top: 10px;
      border-top: 1px solid var(--border);
    }
    .ind-btn-group {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .btn-action {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.76rem;
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
    .btn-detail-link {
      background: transparent;
      border: none;
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      padding: 6px 8px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .btn-detail-link:hover {
      color: var(--text);
    }

    /* ACCORDION DETAIL */
    .ind-detail {
      display: none;
      margin-top: 12px;
      padding-top: 12px;
      border-top: 1px dashed var(--border);
      font-size: 0.8rem;
      color: var(--text-muted);
    }
    .ind-detail.open {
      display: block;
    }
    .detail-section {
      margin-bottom: 8px;
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
    .text-right { text-align: right; }

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
      .filter-row { gap: 4px; }
      .chip { font-size: 0.74rem; padding: 4px 10px; }
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
      <p class="hero-desc">Pusat kendali, format dokumen baku, dan kontrol kelengkapan LKE 2025 BPS Kabupaten Kepulauan Selayar.</p>

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
          <div class="stat-label">Indikator Lengkap</div>
          <div class="stat-num-row">
            <span class="stat-num" style="color: var(--success);" id="topStatComplete">75</span>
            <span class="stat-note">dari 110 indikator</span>
          </div>
          <div class="stat-bar-bg">
            <div class="stat-bar-fill" style="width: 68.2%; background: var(--success);"></div>
          </div>
        </div>

        <!-- Perlu Dilengkapi -->
        <div class="stat-box">
          <div class="stat-label">Perlu Dilengkapi</div>
          <div class="stat-num-row">
            <span class="stat-num" style="color: var(--warning);" id="topStatAttention">35</span>
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
        <button type="button" class="tab-btn active" data-tab="bukti" onclick="switchTab('bukti')">📑 Bukti Dukung (110)</button>
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

        <!-- Area Filter -->
        <div class="filter-row">
          <span class="filter-label">Area:</span>
          <button type="button" class="chip active" data-area="all" onclick="setArea('all')">Semua (110)</button>
          <button type="button" class="chip" data-area="1" onclick="setArea('1')">1. Perubahan (16)</button>
          <button type="button" class="chip" data-area="2" onclick="setArea('2')">2. Tatalaksana (15)</button>
          <button type="button" class="chip" data-area="3" onclick="setArea('3')">3. SDM (21)</button>
          <button type="button" class="chip" data-area="4" onclick="setArea('4')">4. Akuntabilitas (14)</button>
          <button type="button" class="chip" data-area="5" onclick="setArea('5')">5. Pengawasan (22)</button>
          <button type="button" class="chip" data-area="6" onclick="setArea('6')">6. Pelayanan (22)</button>
        </div>

        <!-- Status Filter -->
        <div class="filter-row">
          <span class="filter-label">Status:</span>
          <button type="button" class="chip active" data-status="all" onclick="setStatus('all')">Semua Status</button>
          <button type="button" class="chip chip-warning" data-status="attention" onclick="setStatus('attention')">⚠️ Perlu Dilengkapi (35)</button>
          <button type="button" class="chip chip-success" data-status="complete" onclick="setStatus('complete')">✅ Lengkap (75)</button>
          <button type="button" class="btn-reset-checks" onclick="resetChecks()" title="Reset semua tanda centang verifikasi checklist">🔄 Reset Centang</button>
        </div>
      </div>

      <!-- Result Info -->
      <div class="result-info">
        <span id="resultCount">Menampilkan 110 indikator</span>
        <span id="checkedCount">0 berkas dicentang</span>
      </div>

      <!-- Indicators List -->
      <div id="indicatorsContainer"></div>
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
                <th>Area Perubahan</th>
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
                <td><strong>Manajemen Perubahan</strong></td>
                <td class="text-center">8.00</td>
                <td class="text-center">2.54</td>
                <td class="text-center">4.00</td>
                <td class="text-center"><strong>6.54</strong></td>
                <td class="text-center" style="color: var(--success); font-weight: 700;">81.75%</td>
              </tr>
              <tr>
                <td class="text-center">2</td>
                <td><strong>Penataan Tatalaksana</strong></td>
                <td class="text-center">7.00</td>
                <td class="text-center">3.38</td>
                <td class="text-center">3.50</td>
                <td class="text-center"><strong>6.88</strong></td>
                <td class="text-center" style="color: var(--success); font-weight: 700;">98.29%</td>
              </tr>
              <tr>
                <td class="text-center">3</td>
                <td><strong>Penataan Sistem Manajemen SDM</strong></td>
                <td class="text-center">10.00</td>
                <td class="text-center">3.96</td>
                <td class="text-center">3.50</td>
                <td class="text-center"><strong>7.46</strong></td>
                <td class="text-center" style="color: var(--warning); font-weight: 700;">74.60%</td>
              </tr>
              <tr>
                <td class="text-center">4</td>
                <td><strong>Penguatan Akuntabilitas Kinerja</strong></td>
                <td class="text-center">10.00</td>
                <td class="text-center">5.00</td>
                <td class="text-center">3.50</td>
                <td class="text-center"><strong>8.50</strong></td>
                <td class="text-center" style="color: var(--success); font-weight: 700;">85.00%</td>
              </tr>
              <tr>
                <td class="text-center">5</td>
                <td><strong>Penguatan Pengawasan</strong></td>
                <td class="text-center">15.00</td>
                <td class="text-center">3.38</td>
                <td class="text-center">7.50</td>
                <td class="text-center"><strong>10.88</strong></td>
                <td class="text-center" style="color: var(--warning); font-weight: 700;">72.53%</td>
              </tr>
              <tr>
                <td class="text-center">6</td>
                <td><strong>Peningkatan Kualitas Pelayanan Publik</strong></td>
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

        <div class="drive-code-block">📁 [ROOT] Bukti Dukung ZI 2025 BPS Kab. Kepulauan Selayar
│
├── 📁 01_Manajemen_Perubahan/
│   ├── 📁 Pemenuhan/ (SK Tim, Prosedur Pemilihan, Rencana Kerja, Monev TW)
│   └── 📁 Reform/ (Inovasi Agen Perubahan, Budaya Kerja BerAKHLAK)
│
├── 📁 02_Penataan_Tatalaksana/
│   ├── 📁 Pemenuhan/ (SOP Administrasi, Pemanfaatan TI, Layanan Publik)
│   └── 📁 Reform/ (Peta Proses Bisnis, Transformasi SPBE, Inovasi Digital)
│
├── 📁 03_Manajemen_SDM/
│   ├── 📁 Pemenuhan/ (Peta Jabatan ABK, Pola Mutasi, TNA Diklat 20JP, Reward)
│   └── 📁 Reform/ (SKP Berorientasi Outcome, Penurunan Pelanggaran Disiplin)
│
├── 📁 04_Penguatan_Akuntabilitas/
│   ├── 📁 Pemenuhan/ (Keterlibatan Pimpinan, Indikator SMART, LAKIN Tepat Waktu)
│   └── 📁 Reform/ (Peningkatan IKU, Penghargaan Akuntabilitas Kinerja)
│
├── 📁 05_Penguatan_Pengawasan/
│   ├── 📁 Pemenuhan/ (SPIP Risiko, Penanganan Pengaduan, Benturan Kepentingan)
│   └── 📁 Reform/ (WBS, Kepatuhan LHKPN & LHKASN 100%, Nihil Gratifikasi)
│
└── 📁 06_Peningkatan_Pelayanan_Publik/
    ├── 📁 Pemenuhan/ (Standar Pelayanan, FKP, Reward PST, SIPPN, SKD TW4)
    └── 📁 Reform/ (Dampak Inovasi PST, Integrasi SP4N-LAPOR, Survei Kepuasan)</div>
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
    // Flat dataset
    const DATA = ''' + data_json_str + ''';

    // State
    let activeArea = 'all';
    let activeStatus = 'all';
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

    // Filters
    function setArea(num) {
      activeArea = num;
      document.querySelectorAll('[data-area]').forEach(el => {
        el.classList.toggle('active', el.getAttribute('data-area') === num);
      });
      renderList();
    }

    function setStatus(st) {
      activeStatus = st;
      document.querySelectorAll('[data-status]').forEach(el => {
        el.classList.toggle('active', el.getAttribute('data-status') === st);
      });
      renderList();
    }

    function onSearchChange(val) {
      searchQuery = (val || '').toLowerCase().trim();
      renderList();
    }

    // Toggle Checklist
    function toggleCheck(id) {
      const cb = document.getElementById(id);
      if (cb) {
        checks[id] = cb.checked;
        localStorage.setItem('zi_checks_selayar', JSON.stringify(checks));
        const item = cb.closest('.ind-bukti-item');
        if (item) item.classList.toggle('checked', cb.checked);
        updateCheckedCounter();
      }
    }

    function resetChecks() {
      if (confirm('Hapus semua tanda centang verifikasi checklist bukti dukung?')) {
        checks = {};
        localStorage.removeItem('zi_checks_selayar');
        renderList();
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
      const itm = DATA.find(x => x.code === code);
      if (!itm) return;
      const lines = ['Bukti Dukung Indikator ' + code + ' (' + itm.question + ') - BPS Selayar:'];
      (itm.bukti || []).forEach(b => lines.push('• ' + b));
      navigator.clipboard.writeText(lines.join('\\n')).then(() => {
        showToast('Daftar berkas ' + code + ' disalin ke clipboard');
      }).catch(() => {
        showToast('Gagal menyalin');
      });
    }

    // Toggle Detail
    function toggleDetail(code) {
      const safe = code.replace(/[^a-zA-Z0-9]/g, '_');
      const detail = document.getElementById('detail-' + safe);
      const btn = document.getElementById('btn-detail-' + safe);
      if (detail && btn) {
        const isOpen = detail.classList.contains('open');
        detail.classList.toggle('open');
        btn.innerHTML = isOpen ? '<span>ℹ️</span> Kriteria &amp; Narasi' : '<span>✕</span> Tutup';
      }
    }

    // Render list
    function renderList() {
      const container = document.getElementById('indicatorsContainer');
      if (!container) return;

      const filtered = DATA.filter(itm => {
        // Area filter
        if (activeArea !== 'all' && String(itm.areaNum) !== activeArea) return false;

        // Status filter
        const isComp = itm.status === 'complete' && ['1.00', '1', '300.00%', '100.00%', '105.74%'].includes(itm.nilai);
        if (activeStatus === 'complete' && !isComp) return false;
        if (activeStatus === 'attention' && isComp) return false;

        // Search
        if (searchQuery) {
          const text = [
            itm.code,
            itm.question,
            itm.areaTitle,
            itm.catatan,
            itm.narasi,
            ...(itm.bukti || [])
          ].join(' ').toLowerCase();
          if (!text.includes(searchQuery)) return false;
        }

        return true;
      });

      // Update result count text
      document.getElementById('resultCount').textContent = 'Menampilkan ' + filtered.length + ' dari ' + DATA.length + ' indikator';
      updateCheckedCounter();

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="empty-box">
            <div style="font-size: 1.8rem; margin-bottom: 6px;">🔍</div>
            <div style="font-weight: 700; color: var(--text); margin-bottom: 4px;">Tidak ada indikator yang sesuai</div>
            <div style="font-size: 0.8rem;">Coba ubah kata kunci pencarian atau sesuaikan filter status/area.</div>
          </div>
        `;
        return;
      }

      let html = '';
      filtered.forEach(itm => {
        const safe = itm.code.replace(/[^a-zA-Z0-9]/g, '_');
        const isComp = itm.status === 'complete' && ['1.00', '1', '300.00%', '100.00%', '105.74%'].includes(itm.nilai);
        const isMiss = itm.status === 'missing' || itm.nilai === '0.00';

        const cardState = isMiss ? 'state-missing' : (isComp ? 'state-complete' : 'state-partial');
        const badgeState = isMiss ? 'badge-state-missing' : (isComp ? 'badge-state-complete' : 'badge-state-partial');

        let badgeText = isMiss ? '⚠️ Perlu Dilengkapi (0.00)' : (isComp ? '✅ Lengkap (1.00)' : '🟡 Sebagian (' + itm.nilai + ')');
        if (itm.nilai === '105.74%') badgeText = '✅ Capaian 105.74%';
        if (itm.nilai === '300.00%') badgeText = '✅ Capaian 300%';

        // Bukti items
        let buktiRows = '';
        if (itm.bukti && itm.bukti.length > 0) {
          buktiRows = itm.bukti.map((b, idx) => {
            const checkId = 'chk_' + itm.areaNum + '_' + safe + '_' + idx;
            const checked = !!checks[checkId];
            return `
              <li class="ind-bukti-item ${checked ? 'checked' : ''}">
                <input type="checkbox" id="${checkId}" class="ind-check" ${checked ? 'checked' : ''} onchange="toggleCheck('${checkId}')">
                <label for="${checkId}" style="cursor: pointer; flex: 1;">${b}</label>
              </li>
            `;
          }).join('');
        } else {
          buktiRows = '<li class="ind-bukti-item" style="color: var(--text-muted); font-style: italic;">Tidak ada dokumen khusus tercatat</li>';
        }

        // Catatan box
        let noteHtml = '';
        if (itm.catatan) {
          const isDanger = itm.nilai === '0.00';
          noteHtml = `
            <div class="note-alert ${isDanger ? 'note-alert-danger' : 'note-alert-warning'}">
              <span>⚠️</span>
              <div>${itm.catatan}</div>
            </div>
          `;
        }

        // Link contoh
        let linkContohBtn = '';
        if (itm.link_contoh) {
          linkContohBtn = `
            <a href="${itm.link_contoh}" target="_blank" rel="noopener noreferrer" class="btn-action btn-action-primary" title="Lihat contoh format resmi BPS Pusat">
              <span>🔗</span><span>Contoh Pusat</span>
            </a>
          `;
        }

        html += `
          <div class="ind-card ${cardState}">
            <div class="ind-header">
              <div class="ind-tags">
                <span class="code-tag">${itm.code}</span>
                <span class="area-tag">Area ${itm.areaNum}: ${itm.areaTitle} • ${itm.aspect}</span>
              </div>
              <span class="badge-status ${badgeState}">${badgeText}</span>
            </div>

            <h3 class="ind-title">${itm.question}</h3>

            <div class="ind-bukti-box">
              <div class="ind-bukti-top">
                <span>Bukti Dukung yang Wajib Diunggah:</span>
                <span style="font-size: 0.68rem; text-transform: none;">centang jika siap</span>
              </div>
              <ul class="ind-bukti-list">
                ${buktiRows}
              </ul>
            </div>

            ${noteHtml}

            <div class="ind-actions">
              <div class="ind-btn-group">
                <a href="https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-action" title="Folder Drive: ${itm.drive_folder || 'Root'}">
                  <span>📁</span><span>Folder Drive</span>
                </a>
                ${linkContohBtn}
                <button type="button" class="btn-action" onclick="copyBukti('${itm.code}')">
                  <span>📋</span><span>Salin Berkas</span>
                </button>
              </div>

              <button type="button" class="btn-detail-link" id="btn-detail-${safe}" onclick="toggleDetail('${itm.code}')">
                <span>ℹ️</span><span>Kriteria &amp; Narasi</span>
              </button>
            </div>

            <div class="ind-detail" id="detail-${safe}">
              <div class="detail-section">
                <div class="detail-section-title">Kriteria Penilaian:</div>
                <div style="white-space: pre-line;">${itm.kriteria || '-'}</div>
              </div>
              <div class="detail-section">
                <div class="detail-section-title">Jawaban &amp; Nilai Satker:</div>
                <div>Jawaban: <strong>${itm.jawaban || '-'}</strong> (Nilai: <strong>${itm.nilai}</strong>)</div>
              </div>
              ${itm.narasi ? `
                <div class="detail-section">
                  <div class="detail-section-title">Narasi / Catatan Satker:</div>
                  <div style="font-style: italic; background: var(--bg); padding: 8px 10px; border-radius: var(--radius-sm); border-left: 2px solid var(--border);">${itm.narasi}</div>
                </div>
              ` : ''}
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Init
    document.addEventListener('DOMContentLoaded', () => {
      renderList();
    });
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html successfully updated!")
