# -*- coding: utf-8 -*-
import json
import re

with open('/tmp/zi_data.json', 'r') as f:
    data = json.load(f)

# Drive root
DRIVE_ROOT = "https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing"

def escape_html(text):
    if not text:
        return ""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# Build the complete HTML
html_parts = []

html_parts.append("""<!DOCTYPE html>
<html lang="id">
<head>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Panduan Lengkap Penyusunan Bukti Dukung Zona Integritas (ZI) Menuju WBK/WBBM 2025 - BPS Kabupaten Kepulauan Selayar">
  <title>Panduan Bukti Dukung Zona Integritas | BPS Kab. Kepulauan Selayar</title>
  <style>
    /* ==========================================================================
       RESET & ROOT VARIABLES
       ========================================================================== */
    :root {
      --primary: #1a365d;        /* BPS Navy Blue */
      --primary-light: #2b6cb0;
      --primary-dark: #0f243e;
      --primary-soft: #ebf8ff;
      --gold: #c6953b;           /* ZI Gold */
      --gold-dark: #975a16;
      --gold-light: #f6e05e;
      --gold-soft: #fefcbf;
      --gold-bg: #fffaf0;
      
      --success: #16a34a;        /* Green */
      --success-light: #dcfce7;
      --success-border: #86efac;
      --success-dark: #15803d;
      
      --warning: #d97706;        /* Orange / Amber */
      --warning-light: #fef3c7;
      --warning-border: #fcd34d;
      --warning-dark: #b45309;
      
      --danger: #dc2626;         /* Red */
      --danger-light: #fee2e2;
      --danger-border: #fca5a5;
      --danger-dark: #b91c1c;

      --gray-50: #f8fafc;
      --gray-100: #f1f5f9;
      --gray-200: #e2e8f0;
      --gray-300: #cbd5e1;
      --gray-400: #94a3b8;
      --gray-500: #64748b;
      --gray-600: #475569;
      --gray-700: #334155;
      --gray-800: #1e293b;
      --gray-900: #0f172a;

      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
      --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.12), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
      
      --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
    }

    body {
      font-family: var(--font-sans);
      background-color: var(--gray-50);
      color: var(--gray-800);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }

    a {
      color: var(--primary-light);
      text-decoration: none;
      transition: var(--transition);
    }

    a:hover {
      color: var(--primary);
      text-decoration: underline;
    }

    /* Container */
    .container {
      width: 100%;
      max-width: 1240px;
      margin-left: auto;
      margin-right: auto;
      padding-left: 20px;
      padding-right: 20px;
    }

    /* ==========================================================================
       STICKY TOP NAVIGATION BAR
       ========================================================================== */
    .sticky-navbar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(26, 54, 93, 0.96);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border-bottom: 2px solid var(--gold);
      box-shadow: var(--shadow-md);
      transition: var(--transition);
    }

    .nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 64px;
      gap: 16px;
    }

    .brand-logo {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #ffffff;
      font-weight: 700;
      font-size: 1.1rem;
      text-decoration: none;
      letter-spacing: -0.02em;
      white-space: nowrap;
    }

    .brand-logo .brand-badge {
      background: linear-gradient(135deg, var(--gold), #d4af37);
      color: #0f172a;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 6px;
      list-style: none;
      overflow-x: auto;
      padding-bottom: 2px;
      -ms-overflow-style: none;
      scrollbar-width: none;
    }

    .nav-links::-webkit-scrollbar {
      display: none;
    }

    .nav-item-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 12px;
      font-size: 0.85rem;
      font-weight: 600;
      color: #e2e8f0;
      border-radius: var(--radius-sm);
      background: transparent;
      border: 1px solid transparent;
      cursor: pointer;
      white-space: nowrap;
      transition: var(--transition);
    }

    .nav-item-btn:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
      text-decoration: none;
    }

    .nav-item-btn.active {
      background: var(--gold);
      color: #0f172a;
      font-weight: 700;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    .btn-filter-warning {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #dc2626;
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      border: none;
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(220, 38, 38, 0.3);
      transition: var(--transition);
    }

    .btn-filter-warning:hover {
      background: #b91c1c;
      transform: translateY(-1px);
    }

    .btn-filter-warning.is-filtering {
      background: #15803d;
      box-shadow: 0 2px 4px rgba(21, 128, 61, 0.3);
    }

    .btn-drive-top {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: linear-gradient(135deg, var(--gold), #d4af37);
      color: #0f172a;
      font-size: 0.82rem;
      font-weight: 700;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      border: none;
      cursor: pointer;
      text-decoration: none;
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
    }

    .btn-drive-top:hover {
      background: #e2b34a;
      transform: translateY(-1px);
      text-decoration: none;
      box-shadow: var(--shadow-md);
    }

    /* ==========================================================================
       HERO SECTION
       ========================================================================== */
    .hero-section {
      background: linear-gradient(135deg, #0f233d 0%, #1a365d 65%, #234e82 100%);
      color: #ffffff;
      padding: 56px 0 48px;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid var(--gold);
    }

    .hero-section::before {
      content: "";
      position: absolute;
      top: -50%;
      right: -20%;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, rgba(198, 149, 59, 0.15) 0%, rgba(26, 54, 93, 0) 70%);
      border-radius: 50%;
      pointer-events: none;
    }

    .hero-content {
      position: relative;
      z-index: 1;
      max-width: 960px;
    }

    .hero-badge-top {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(198, 149, 59, 0.2);
      border: 1px solid rgba(198, 149, 59, 0.4);
      color: var(--gold-soft);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 16px;
    }

    .hero-title {
      font-size: 2.35rem;
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: -0.02em;
      margin-bottom: 12px;
      color: #ffffff;
    }

    .hero-title span {
      background: linear-gradient(90deg, #fef3c7, var(--gold-light));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
      font-size: 1.15rem;
      color: #cbd5e1;
      margin-bottom: 24px;
      font-weight: 400;
      max-width: 800px;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 14px;
      margin-top: 24px;
    }

    .hero-btn-primary {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(135deg, var(--gold), #d4af37);
      color: #0f172a;
      font-size: 0.95rem;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: var(--radius-md);
      box-shadow: 0 4px 14px rgba(198, 149, 59, 0.4);
      transition: var(--transition);
      text-decoration: none;
    }

    .hero-btn-primary:hover {
      background: #dfb249;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(198, 149, 59, 0.5);
      text-decoration: none;
    }

    .hero-btn-secondary {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.25);
      font-size: 0.95rem;
      font-weight: 600;
      padding: 12px 22px;
      border-radius: var(--radius-md);
      transition: var(--transition);
      cursor: pointer;
      text-decoration: none;
    }

    .hero-btn-secondary:hover {
      background: rgba(255, 255, 255, 0.22);
      transform: translateY(-2px);
      text-decoration: none;
      color: #ffffff;
    }

    /* Live Search & Quick Filter Bar */
    .search-filter-card {
      margin-top: -30px;
      position: relative;
      z-index: 10;
      background: #ffffff;
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-xl);
      padding: 20px 24px;
      border: 1px solid var(--gray-200);
    }

    .search-filter-flex {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 16px;
    }

    .search-input-wrapper {
      flex: 1;
      min-width: 280px;
      position: relative;
    }

    .search-input-wrapper input {
      width: 100%;
      padding: 12px 16px 12px 42px;
      font-size: 0.95rem;
      border: 2px solid var(--gray-200);
      border-radius: var(--radius-md);
      outline: none;
      transition: var(--transition);
      background: #ffffff;
    }

    .search-input-wrapper input:focus {
      border-color: var(--primary-light);
      box-shadow: 0 0 0 3px rgba(43, 108, 176, 0.15);
    }

    .search-icon {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.1rem;
      color: var(--gray-400);
    }

    .filter-pills-group {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }

    .pill-filter-btn {
      padding: 8px 14px;
      font-size: 0.85rem;
      font-weight: 600;
      border-radius: var(--radius-full);
      border: 1px solid var(--gray-200);
      background: var(--gray-100);
      color: var(--gray-700);
      cursor: pointer;
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .pill-filter-btn:hover {
      background: var(--gray-200);
    }

    .pill-filter-btn.active {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }

    .pill-filter-btn.active-warning {
      background: var(--danger);
      color: #ffffff;
      border-color: var(--danger);
    }

    /* ==========================================================================
       DASHBOARD SUMMARY SECTION
       ========================================================================== */
    .dashboard-section {
      padding: 48px 0 32px;
    }

    .section-header {
      margin-bottom: 28px;
    }

    .section-title-wrap {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }

    .section-title {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .section-desc {
      font-size: 0.95rem;
      color: var(--gray-500);
      margin-top: 4px;
    }

    /* Dashboard Top 3 Cards Grid */
    .summary-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
      margin-bottom: 32px;
    }

    .summary-card {
      background: #ffffff;
      border-radius: var(--radius-lg);
      padding: 24px;
      border: 1px solid var(--gray-200);
      box-shadow: var(--shadow-md);
      transition: var(--transition);
      position: relative;
      overflow: hidden;
    }

    .summary-card:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg);
    }

    .summary-card.primary {
      border-top: 5px solid var(--gold);
    }

    .summary-card.accent {
      border-top: 5px solid var(--primary-light);
    }

    .summary-card.neutral {
      border-top: 5px solid var(--gray-400);
      background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    }

    .card-header-flex {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }

    .card-label {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--gray-500);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .card-badge {
      padding: 3px 10px;
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      font-weight: 700;
    }

    .badge-gold {
      background: var(--gold-soft);
      color: var(--gold-dark);
      border: 1px solid var(--gold-light);
    }

    .badge-blue {
      background: var(--primary-soft);
      color: var(--primary);
      border: 1px solid #bfdbfe;
    }

    .badge-gray {
      background: var(--gray-100);
      color: var(--gray-600);
      border: 1px solid var(--gray-300);
    }

    .card-score-big {
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-bottom: 12px;
    }

    .score-main {
      font-size: 2.6rem;
      font-weight: 900;
      color: var(--primary);
      line-height: 1;
    }

    .score-max {
      font-size: 1.15rem;
      font-weight: 600;
      color: var(--gray-400);
    }

    .score-pct-badge {
      font-size: 0.95rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      margin-left: auto;
    }

    /* Progress bar */
    .progress-track {
      width: 100%;
      height: 10px;
      background-color: var(--gray-200);
      border-radius: var(--radius-full);
      overflow: hidden;
      margin-bottom: 16px;
    }

    .progress-fill {
      height: 100%;
      border-radius: var(--radius-full);
      transition: width 0.8s ease;
    }

    .fill-gold {
      background: linear-gradient(90deg, #d4af37, var(--gold));
    }

    .fill-green {
      background: linear-gradient(90deg, #22c55e, #16a34a);
    }

    .fill-yellow {
      background: linear-gradient(90deg, #f59e0b, #d97706);
    }

    .fill-red {
      background: linear-gradient(90deg, #f87171, #dc2626);
    }

    .fill-blue {
      background: linear-gradient(90deg, #60a5fa, #2563eb);
    }

    .sub-progress-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
      border-top: 1px solid var(--gray-100);
      padding-top: 14px;
    }

    .sub-progress-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.85rem;
    }

    .sub-progress-name {
      color: var(--gray-600);
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .sub-progress-val {
      font-weight: 700;
      color: var(--gray-800);
    }

    /* Area Cards 6-Grid */
    .areas-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 20px;
    }

    .area-summary-card {
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--gray-200);
      padding: 22px;
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
      cursor: pointer;
      display: flex;
      flex-direction: column;
    }

    .area-summary-card:hover {
      border-color: var(--primary-light);
      box-shadow: var(--shadow-lg);
      transform: translateY(-3px);
    }

    .area-card-head {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 14px;
    }

    .area-icon-box {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      background: var(--primary-soft);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      flex-shrink: 0;
    }

    .area-card-title-wrap {
      flex: 1;
    }

    .area-number-label {
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--gold-dark);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .area-card-name {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary);
      line-height: 1.3;
    }

    .area-status-pill {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      white-space: nowrap;
    }

    .status-green {
      background: var(--success-light);
      color: var(--success-dark);
      border: 1px solid var(--success-border);
    }

    .status-yellow {
      background: var(--warning-light);
      color: var(--warning-dark);
      border: 1px solid var(--warning-border);
    }

    .status-red {
      background: var(--danger-light);
      color: var(--danger-dark);
      border: 1px solid var(--danger-border);
    }

    .area-scores-box {
      background: var(--gray-50);
      border-radius: var(--radius-md);
      padding: 12px 14px;
      margin-bottom: 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .score-row-mini {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.85rem;
    }

    .score-row-mini .row-label {
      color: var(--gray-600);
      font-weight: 500;
    }

    .score-row-mini .row-score {
      font-weight: 700;
      color: var(--gray-800);
    }

    .area-card-footer {
      margin-top: auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 12px;
      border-top: 1px solid var(--gray-100);
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--primary-light);
    }

    .area-card-footer:hover {
      color: var(--primary);
    }

    /* ==========================================================================
       TAB NAVIGATION & AREA CONTENT SECTION
       ========================================================================== */
    .content-section {
      padding: 32px 0 64px;
    }

    .area-tabs-nav {
      display: flex;
      gap: 8px;
      border-bottom: 2px solid var(--gray-200);
      margin-bottom: 32px;
      overflow-x: auto;
      padding-bottom: 4px;
      -ms-overflow-style: none;
      scrollbar-width: none;
    }

    .area-tabs-nav::-webkit-scrollbar {
      display: none;
    }

    .area-tab-button {
      padding: 12px 18px;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--gray-600);
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      margin-bottom: -6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      transition: var(--transition);
      border-radius: var(--radius-sm) var(--radius-sm) 0 0;
    }

    .area-tab-button:hover {
      color: var(--primary);
      background: var(--gray-100);
    }

    .area-tab-button.active {
      color: var(--primary);
      border-bottom-color: var(--gold);
      background: #ffffff;
      box-shadow: 0 -2px 6px rgba(0, 0, 0, 0.04);
    }

    .tab-badge-count {
      font-size: 0.72rem;
      padding: 2px 6px;
      border-radius: var(--radius-full);
      background: var(--danger-light);
      color: var(--danger-dark);
      font-weight: 800;
    }

    /* Area Pane View */
    .area-pane {
      display: none;
    }

    .area-pane.active {
      display: block;
      animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .area-hero-banner {
      background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
      border: 1px solid var(--gray-200);
      border-left: 6px solid var(--primary);
      border-radius: var(--radius-lg);
      padding: 24px 28px;
      margin-bottom: 32px;
      box-shadow: var(--shadow-sm);
    }

    .area-banner-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 12px;
    }

    .area-banner-title {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .area-banner-stats {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .stat-pill-banner {
      background: #ffffff;
      border: 1px solid var(--gray-200);
      border-radius: var(--radius-md);
      padding: 8px 14px;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: var(--shadow-sm);
    }

    .stat-pill-banner strong {
      color: var(--primary);
      font-size: 1rem;
    }

    .area-banner-desc {
      font-size: 0.95rem;
      color: var(--gray-600);
      line-height: 1.6;
      max-width: 900px;
    }

    /* Section Aspect (Pemenuhan & Reform) */
    .aspect-section {
      margin-bottom: 40px;
    }

    .aspect-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
      background: #ffffff;
      padding: 16px 20px;
      border-radius: var(--radius-md);
      border: 1px solid var(--gray-200);
      border-left: 5px solid var(--gold);
      margin-bottom: 20px;
      box-shadow: var(--shadow-sm);
    }

    .aspect-title-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .aspect-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
    }

    .aspect-score-badge {
      font-size: 0.85rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      background: var(--gold-soft);
      color: var(--gold-dark);
      border: 1px solid var(--gold-light);
    }

    .aspect-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .btn-toggle-all {
      font-size: 0.8rem;
      font-weight: 600;
      background: var(--gray-100);
      color: var(--gray-700);
      border: 1px solid var(--gray-300);
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: var(--transition);
    }

    .btn-toggle-all:hover {
      background: var(--gray-200);
    }

    /* Sub-Group Section */
    .subgroup-block {
      margin-bottom: 24px;
    }

    .subgroup-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--gray-800);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      background: var(--gray-100);
      border-radius: var(--radius-sm);
      border-left: 3px solid var(--primary-light);
    }

    .subgroup-score {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--primary-light);
    }

    /* Indicator Accordion Card */
    .indicator-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--gray-200);
      margin-bottom: 12px;
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      transition: var(--transition);
    }

    .indicator-card:hover {
      border-color: var(--gray-300);
      box-shadow: var(--shadow-md);
    }

    .indicator-card.status-border-green {
      border-left: 4px solid var(--success);
    }

    .indicator-card.status-border-yellow {
      border-left: 4px solid var(--warning);
    }

    .indicator-card.status-border-red {
      border-left: 4px solid var(--danger);
    }

    /* Card Header */
    .indicator-header {
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      cursor: pointer;
      user-select: none;
      background: #ffffff;
      transition: var(--transition);
    }

    .indicator-header:hover {
      background: var(--gray-50);
    }

    .indicator-left {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      flex: 1;
    }

    .indicator-code-badge {
      font-size: 0.8rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      background: var(--primary-soft);
      color: var(--primary);
      white-space: nowrap;
      flex-shrink: 0;
      border: 1px solid #bfdbfe;
    }

    .indicator-question {
      font-size: 0.98rem;
      font-weight: 700;
      color: var(--gray-900);
      line-height: 1.45;
    }

    .indicator-right {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }

    .badge-answer {
      font-size: 0.8rem;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      display: inline-flex;
      align-items: center;
      gap: 5px;
      white-space: nowrap;
    }

    .badge-answer.good {
      background: var(--success-light);
      color: var(--success-dark);
      border: 1px solid var(--success-border);
    }

    .badge-answer.warn {
      background: var(--warning-light);
      color: var(--warning-dark);
      border: 1px solid var(--warning-border);
    }

    .badge-answer.bad {
      background: var(--danger-light);
      color: var(--danger-dark);
      border: 1px solid var(--danger-border);
    }

    .indicator-score-box {
      font-size: 0.9rem;
      font-weight: 800;
      color: var(--gray-700);
      background: var(--gray-100);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      white-space: nowrap;
    }

    .accordion-chevron {
      font-size: 0.85rem;
      color: var(--gray-400);
      transition: transform 0.25s ease;
    }

    .indicator-card.open .accordion-chevron {
      transform: rotate(180deg);
    }

    /* Card Body (Collapsible) */
    .indicator-body {
      display: none;
      padding: 0 20px 20px;
      border-top: 1px solid var(--gray-100);
      background: #ffffff;
      animation: expandContent 0.2s ease;
    }

    .indicator-card.open .indicator-body {
      display: block;
    }

    @keyframes expandContent {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    .indicator-body-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
      padding-top: 16px;
    }

    /* Indicator Meta Boxes */
    .info-box {
      background: var(--gray-50);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      border: 1px solid var(--gray-200);
    }

    .info-box-title {
      font-size: 0.8rem;
      font-weight: 800;
      color: var(--gray-500);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .criteria-box {
      background: #faf5ff;
      border-color: #e9d5ff;
    }

    .criteria-box .info-box-title {
      color: #7e22ce;
    }

    .criteria-text {
      font-size: 0.88rem;
      color: #3b0764;
      white-space: pre-line;
      line-height: 1.5;
    }

    .narrative-box {
      background: #f0fdf4;
      border-color: #bbf7d0;
    }

    .narrative-box .info-box-title {
      color: #15803d;
    }

    .narrative-text {
      font-size: 0.9rem;
      color: #14532d;
      line-height: 1.55;
      font-style: italic;
    }

    .notes-box {
      background: #fffbeb;
      border-color: #fde68a;
    }

    .notes-box .info-box-title {
      color: #b45309;
    }

    .notes-text {
      font-size: 0.9rem;
      color: #92400e;
      font-weight: 600;
      line-height: 1.5;
    }

    /* Required Evidence List */
    .evidence-section {
      margin-top: 6px;
    }

    .evidence-title {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .evidence-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .evidence-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 10px 14px;
      background: #ffffff;
      border: 1px solid var(--gray-200);
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      color: var(--gray-800);
      transition: var(--transition);
    }

    .evidence-item:hover {
      background: var(--gray-50);
      border-color: var(--gray-300);
    }

    .evidence-bullet {
      color: var(--gold);
      font-size: 1.1rem;
      line-height: 1.2;
      flex-shrink: 0;
    }

    .evidence-text {
      flex: 1;
    }

    /* Indicator Action Buttons */
    .indicator-action-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      padding-top: 14px;
      border-top: 1px dashed var(--gray-200);
      margin-top: 10px;
    }

    .btn-link-action {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      text-decoration: none;
      transition: var(--transition);
      cursor: pointer;
    }

    .btn-example-link {
      background: var(--primary-soft);
      color: var(--primary);
      border: 1px solid #bfdbfe;
    }

    .btn-example-link:hover {
      background: #dbeafe;
      color: var(--primary-dark);
      text-decoration: none;
    }

    .btn-drive-folder {
      background: var(--gold-bg);
      color: var(--gold-dark);
      border: 1px solid var(--gold-light);
    }

    .btn-drive-folder:hover {
      background: var(--gold-soft);
      text-decoration: none;
    }

    .btn-copy-evidence {
      background: var(--gray-100);
      color: var(--gray-700);
      border: 1px solid var(--gray-300);
    }

    .btn-copy-evidence:hover {
      background: var(--gray-200);
      color: var(--gray-900);
    }

    /* ==========================================================================
       KOMPONEN HASIL SECTION
       ========================================================================== */
    .hasil-card-wrapper {
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--gray-200);
      padding: 32px;
      box-shadow: var(--shadow-md);
      margin-bottom: 32px;
    }

    .hasil-notice {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-left: 5px solid var(--primary-light);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      margin-bottom: 24px;
      font-size: 0.95rem;
      color: #1e3a8a;
      line-height: 1.6;
    }

    .hasil-sub-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
    }

    .hasil-sub-card {
      background: var(--gray-50);
      border: 1px solid var(--gray-200);
      border-radius: var(--radius-md);
      padding: 20px;
    }

    .hasil-sub-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--primary);
      margin-bottom: 8px;
    }

    .hasil-sub-bobot {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--gold-dark);
      margin-bottom: 16px;
    }

    .hasil-item-card {
      background: #ffffff;
      border: 1px solid var(--gray-200);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      margin-bottom: 12px;
    }

    .hasil-item-name {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--gray-900);
      margin-bottom: 4px;
    }

    .hasil-item-desc {
      font-size: 0.85rem;
      color: var(--gray-600);
      margin-bottom: 8px;
    }

    .hasil-item-target {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-soft);
      display: inline-block;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }

    /* ==========================================================================
       CHECKLIST GENERATOR & TRACKER SECTION
       ========================================================================== */
    .checklist-section {
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--gray-200);
      padding: 32px;
      box-shadow: var(--shadow-md);
      margin-bottom: 40px;
    }

    .checklist-controls {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--gray-200);
      margin-bottom: 20px;
    }

    .checklist-stats {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--gray-700);
    }

    .checklist-actions-btns {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .btn-action-primary {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      border-radius: var(--radius-sm);
      border: none;
      cursor: pointer;
      transition: var(--transition);
    }

    .btn-action-primary:hover {
      background: var(--primary-light);
    }

    .btn-action-outline {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      background: transparent;
      color: var(--gray-700);
      font-size: 0.85rem;
      font-weight: 700;
      border-radius: var(--radius-sm);
      border: 1px solid var(--gray-300);
      cursor: pointer;
      transition: var(--transition);
    }

    .btn-action-outline:hover {
      background: var(--gray-100);
      color: var(--gray-900);
    }

    /* Checklist Table */
    .table-responsive {
      overflow-x: auto;
    }

    .checklist-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }

    .checklist-table th {
      background: var(--primary);
      color: #ffffff;
      padding: 12px 14px;
      text-align: left;
      font-weight: 700;
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .checklist-table td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--gray-200);
      vertical-align: top;
    }

    .checklist-table tr:hover td {
      background: var(--gray-50);
    }

    .checklist-table .chk-col {
      width: 44px;
      text-align: center;
    }

    .checklist-table input[type="checkbox"] {
      width: 18px;
      height: 18px;
      accent-color: var(--success);
      cursor: pointer;
    }

    /* ==========================================================================
       GOOGLE DRIVE STRUCTURE GUIDE
       ========================================================================== */
    .drive-guide-card {
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--gray-200);
      padding: 32px;
      box-shadow: var(--shadow-md);
      margin-bottom: 40px;
    }

    .drive-tree-view {
      background: #0f172a;
      color: #94a3b8;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 0.88rem;
      padding: 24px;
      border-radius: var(--radius-md);
      line-height: 1.7;
      overflow-x: auto;
      margin: 20px 0;
      border: 1px solid #1e293b;
      white-space: pre;
    }

    .drive-tree-view .folder-root {
      color: #fde047;
      font-weight: bold;
    }

    .drive-tree-view .folder-area {
      color: #60a5fa;
      font-weight: bold;
    }

    .drive-tree-view .folder-sub {
      color: #34d399;
    }

    .drive-tree-view .folder-item {
      color: #e2e8f0;
    }

    /* ==========================================================================
       FOOTER
       ========================================================================== */
    .site-footer {
      background: var(--primary-dark);
      color: #94a3b8;
      padding: 48px 0 28px;
      border-top: 3px solid var(--gold);
      font-size: 0.9rem;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 32px;
      margin-bottom: 36px;
    }

    .footer-brand-title {
      color: #ffffff;
      font-size: 1.2rem;
      font-weight: 800;
      margin-bottom: 8px;
    }

    .footer-brand-desc {
      line-height: 1.6;
      max-width: 480px;
      font-size: 0.88rem;
    }

    .footer-heading {
      color: #ffffff;
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 14px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .footer-links {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .footer-links a {
      color: #cbd5e1;
      font-size: 0.88rem;
    }

    .footer-links a:hover {
      color: var(--gold-light);
      text-decoration: none;
    }

    .footer-bottom {
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding-top: 20px;
      text-align: center;
      font-size: 0.82rem;
      color: #64748b;
    }

    /* ==========================================================================
       TOAST NOTIFICATION
       ========================================================================== */
    .toast-container {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
      pointer-events: none;
    }

    .toast {
      background: #1e293b;
      color: #ffffff;
      padding: 12px 20px;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-xl);
      font-size: 0.88rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 8px;
      border-left: 4px solid var(--gold);
      animation: slideInToast 0.25s ease forwards;
    }

    @keyframes slideInToast {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ==========================================================================
       PRINT STYLES
       ========================================================================== */
    @media print {
      .sticky-navbar,
      .hero-actions,
      .search-filter-card,
      .area-tabs-nav,
      .aspect-actions,
      .indicator-action-bar,
      .checklist-actions-btns,
      .toast-container,
      .btn-drive-top {
        display: none !important;
      }

      body {
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 11pt;
      }

      .container {
        max-width: 100% !important;
        padding: 0 !important;
      }

      .hero-section {
        background: none !important;
        color: #000000 !important;
        padding: 20px 0 !important;
        border-bottom: 2px solid #000000 !important;
      }

      .hero-title {
        color: #000000 !important;
        font-size: 18pt !important;
      }

      .hero-title span {
        -webkit-text-fill-color: initial !important;
        color: #000000 !important;
      }

      .area-pane {
        display: block !important;
        page-break-before: always;
      }

      .indicator-body {
        display: block !important;
      }

      .indicator-card {
        border: 1px solid #cccccc !important;
        box-shadow: none !important;
        page-break-inside: avoid;
        margin-bottom: 12px !important;
      }

      .summary-card, .area-summary-card {
        box-shadow: none !important;
        border: 1px solid #cccccc !important;
      }

      .site-footer {
        background: none !important;
        color: #000000 !important;
        border-top: 1px solid #cccccc !important;
      }
    }

    /* Responsive */
    @media (max-width: 900px) {
      .footer-grid {
        grid-template-columns: 1fr;
      }
      .nav-links {
        display: none;
      }
      .hero-title {
        font-size: 1.8rem;
      }
    }
  </style>
</head>
<body>

  <!-- ========================================================================
       TOP STICKY NAVBAR
       ======================================================================== -->
  <header class="sticky-navbar">
    <div class="container nav-inner">
      <a href="#dashboard" class="brand-logo" title="BPS Kabupaten Kepulauan Selayar">
        <span>🏛️ BPS Kab. Kepulauan Selayar</span>
        <span class="brand-badge">ZI WBK/WBBM</span>
      </a>

      <nav class="nav-links" aria-label="Navigasi Area">
        <button type="button" class="nav-item-btn active" onclick="switchNavTab('dashboard')">📊 Ringkasan</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('area1')">1. Manajemen Perubahan</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('area2')">2. Tatalaksana</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('area3')">3. SDM</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('area4')">4. Akuntabilitas</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('area5')">5. Pengawasan</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('area6')">6. Pelayanan Publik</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('hasil')">🏆 Hasil</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('checklist')">📋 Checklist</button>
        <button type="button" class="nav-item-btn" onclick="switchNavTab('drive')">📁 Folder Drive</button>
      </nav>

      <div class="nav-actions">
        <button type="button" id="topFilterWarningBtn" class="btn-filter-warning" onclick="toggleAttentionFilter()">
          <span>⚠️</span>
          <span id="filterWarningText">Perlu Perhatian (25)</span>
        </button>
        <a href="https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-drive-top" title="Buka Folder Google Drive Utama">
          <span>📁</span>
          <span>Google Drive</span>
        </a>
      </div>
    </div>
  </header>

  <!-- ========================================================================
       HERO SECTION
       ======================================================================== -->
  <section class="hero-section">
    <div class="container hero-content">
      <div class="hero-badge-top">
        <span>LEMBAR KERJA EVALUASI (LKE) PEMBANGUNAN ZONA INTEGRITAS 2025</span>
      </div>
      <h1 class="hero-title">
        Panduan Penyusunan Bukti Dukung <span>Zona Integritas</span>
      </h1>
      <p class="hero-subtitle">
        BPS Kabupaten Kepulauan Selayar — Akselerasi Penyiapan Bukti Dukung Menuju Predikat Wilayah Bebas dari Korupsi (WBK) &amp; Wilayah Birokrasi Bersih dan Melayani (WBBM) 2025.
      </p>

      <div class="hero-actions">
        <a href="https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing" target="_blank" rel="noopener noreferrer" class="hero-btn-primary">
          <span>📂</span>
          <span>Buka Google Drive Bukti Dukung</span>
        </a>
        <button type="button" class="hero-btn-secondary" onclick="switchNavTab('checklist')">
          <span>📋</span>
          <span>Checklist &amp; Export Dokumen</span>
        </button>
        <button type="button" class="hero-btn-secondary" onclick="window.print()">
          <span>🖨️</span>
          <span>Cetak Panduan (PDF)</span>
        </button>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       SEARCH & QUICK FILTER FLOATING CARD
       ======================================================================== -->
  <div class="container">
    <div class="search-filter-card">
      <div class="search-filter-flex">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" id="liveSearchInput" placeholder="Ketik kata kunci indikator, dokumen bukti dukung, SK, laporan..." oninput="handleLiveSearch(this.value)">
        </div>
        <div class="filter-pills-group">
          <button type="button" class="pill-filter-btn active" id="filterPillAll" onclick="setQuickFilter('all')">
            <span>Semua Indikator</span>
          </button>
          <button type="button" class="pill-filter-btn" id="filterPillAttention" onclick="setQuickFilter('attention')">
            <span>⚠️ Perlu Dilengkapi (<span id="countAttentionPill">25</span>)</span>
          </button>
          <button type="button" class="pill-filter-btn" id="filterPillComplete" onclick="setQuickFilter('complete')">
            <span>✅ Lengkap (37)</span>
          </button>
          <button type="button" class="pill-filter-btn" onclick="expandAllIndicators(true)">
            <span>➕ Buka Semua</span>
          </button>
          <button type="button" class="pill-filter-btn" onclick="expandAllIndicators(false)">
            <span>➖ Tutup Semua</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <main class="container content-section">
""")

# Dashboard Pane
html_parts.append("""
    <!-- ======================================================================
         PANE: DASHBOARD
         ====================================================================== -->
    <div id="pane-dashboard" class="area-pane active">
      <div class="dashboard-section">
        <div class="section-header">
          <div class="section-title-wrap">
            <h2 class="section-title"><span>📊</span> Ringkasan Penilaian Mandiri ZI</h2>
            <div class="section-desc">Status capaian indikator Lembar Kerja Evaluasi (LKE) terkini BPS Kabupaten Kepulauan Selayar</div>
          </div>
        </div>

        <!-- 3 Big Cards Summary -->
        <div class="summary-cards-grid">
          <!-- Total Score Card -->
          <div class="summary-card primary">
            <div class="card-header-flex">
              <span class="card-label">Total Skor Penilaian Mandiri</span>
              <span class="card-badge badge-gold">Target WBK: &ge; 75.00</span>
            </div>
            <div class="card-score-big">
              <span class="score-main">46.70</span>
              <span class="score-max">/ 100.00</span>
              <span class="score-pct-badge status-yellow">46.70%</span>
            </div>
            <div class="progress-track" title="Total Progres 46.70%">
              <div class="progress-fill fill-yellow" style="width: 46.70%;"></div>
            </div>
            <div class="sub-progress-list">
              <div class="sub-progress-item">
                <span class="sub-progress-name">⚙️ Komponen Pengungkit (60%)</span>
                <span class="sub-progress-val">46.70 / 60.00 (77.83%)</span>
              </div>
              <div class="sub-progress-item">
                <span class="sub-progress-name">🏆 Komponen Hasil (40%)</span>
                <span class="sub-progress-val">0.00 / 40.00 (0.00%)</span>
              </div>
            </div>
          </div>

          <!-- Pengungkit Card -->
          <div class="summary-card accent">
            <div class="card-header-flex">
              <span class="card-label">Komponen Pengungkit</span>
              <span class="card-badge badge-blue">Capaian: 77.83%</span>
            </div>
            <div class="card-score-big">
              <span class="score-main">46.70</span>
              <span class="score-max">/ 60.00</span>
              <span class="score-pct-badge status-yellow">77.83%</span>
            </div>
            <div class="progress-track" title="Pengungkit 77.83%">
              <div class="progress-fill fill-green" style="width: 77.83%;"></div>
            </div>
            <div class="sub-progress-list">
              <div class="sub-progress-item">
                <span class="sub-progress-name">📋 Aspek Pemenuhan</span>
                <span class="sub-progress-val">22.20 / 30.00 (73.98%)</span>
              </div>
              <div class="sub-progress-item">
                <span class="sub-progress-name">🚀 Aspek Reform</span>
                <span class="sub-progress-val">24.50 / 30.00 (81.67%)</span>
              </div>
            </div>
          </div>

          <!-- Hasil Card -->
          <div class="summary-card neutral">
            <div class="card-header-flex">
              <span class="card-label">Komponen Hasil</span>
              <span class="card-badge badge-gray">Menunggu Survei</span>
            </div>
            <div class="card-score-big">
              <span class="score-main" style="color: var(--gray-400);">0.00</span>
              <span class="score-max">/ 40.00</span>
              <span class="score-pct-badge badge-gray">0.00%</span>
            </div>
            <div class="progress-track" title="Komponen Hasil 0.00%">
              <div class="progress-fill fill-blue" style="width: 0%;"></div>
            </div>
            <div class="sub-progress-list">
              <div class="sub-progress-item">
                <span class="sub-progress-name">🛡️ Bebas KKN / IPAK (17.50)</span>
                <span class="sub-progress-val" style="color: var(--gray-500);">Menunggu Survei</span>
              </div>
              <div class="sub-progress-item">
                <span class="sub-progress-name">⭐ Pelayanan Publik / IPKP (17.50)</span>
                <span class="sub-progress-val" style="color: var(--gray-500);">Menunggu Survei</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 6 Area Breakdown Grid -->
        <div class="section-header" style="margin-top: 40px;">
          <div class="section-title-wrap">
            <h3 class="section-title" style="font-size: 1.35rem;"><span>📂</span> Rincian Capaian 6 Area Perubahan (Pengungkit)</h3>
            <span class="section-desc">Klik kartu area mana pun untuk langsung membuka panduan indikator dan daftar bukti dukung terkait</span>
          </div>
        </div>

        <div class="areas-grid">
""")

# Render 6 Area Summary Cards
area_stats = [
    {
        "id": "area1",
        "num": "Area 1",
        "name": "Manajemen Perubahan",
        "icon": "🔄",
        "pem_val": "2.54 / 4.00",
        "pem_pct": "63.54%",
        "ref_val": "4.00 / 4.00",
        "ref_pct": "100.00%",
        "tot_val": "6.54 / 8.00",
        "tot_pct": "81.75%",
        "status_class": "status-green",
        "status_text": "Baik (81.75%)",
        "fill_class": "fill-green",
        "attention_count": 5
    },
    {
        "id": "area2",
        "num": "Area 2",
        "name": "Penataan Tatalaksana",
        "icon": "⚙️",
        "pem_val": "3.38 / 3.50",
        "pem_pct": "96.43%",
        "ref_val": "3.50 / 3.50",
        "ref_pct": "100.00%",
        "tot_val": "6.88 / 7.00",
        "tot_pct": "98.29%",
        "status_class": "status-green",
        "status_text": "Sangat Baik (98.29%)",
        "fill_class": "fill-green",
        "attention_count": 2
    },
    {
        "id": "area3",
        "num": "Area 3",
        "name": "Manajemen SDM Aparatur",
        "icon": "👥",
        "pem_val": "3.96 / 5.00",
        "pem_pct": "79.17%",
        "ref_val": "3.50 / 5.00",
        "ref_pct": "70.00%",
        "tot_val": "7.46 / 10.00",
        "tot_pct": "74.60%",
        "status_class": "status-yellow",
        "status_text": "Cukup (74.60%)",
        "fill_class": "fill-yellow",
        "attention_count": 7
    },
    {
        "id": "area4",
        "num": "Area 4",
        "name": "Penguatan Akuntabilitas",
        "icon": "📊",
        "pem_val": "5.00 / 5.00",
        "pem_pct": "100.00%",
        "ref_val": "3.50 / 5.00",
        "ref_pct": "70.00%",
        "tot_val": "8.50 / 10.00",
        "tot_pct": "85.00%",
        "status_class": "status-green",
        "status_text": "Baik (85.00%)",
        "fill_class": "fill-green",
        "attention_count": 1
    },
    {
        "id": "area5",
        "num": "Area 5",
        "name": "Penguatan Pengawasan",
        "icon": "🛡️",
        "pem_val": "3.38 / 7.50",
        "pem_pct": "45.00%",
        "ref_val": "7.50 / 7.50",
        "ref_pct": "100.00%",
        "tot_val": "10.88 / 15.00",
        "tot_pct": "72.53%",
        "status_class": "status-yellow",
        "status_text": "Perlu Ditingkatkan",
        "fill_class": "fill-yellow",
        "attention_count": 12
    },
    {
        "id": "area6",
        "num": "Area 6",
        "name": "Pelayanan Publik",
        "icon": "⭐",
        "pem_val": "3.95 / 5.00",
        "pem_pct": "78.90%",
        "ref_val": "2.50 / 5.00",
        "ref_pct": "50.00%",
        "tot_val": "6.45 / 10.00",
        "tot_pct": "64.50%",
        "status_class": "status-yellow",
        "status_text": "Cukup (64.50%)",
        "fill_class": "fill-yellow",
        "attention_count": 8
    }
]

for st in area_stats:
    html_parts.append(f"""
          <div class="area-summary-card" onclick="switchNavTab('{st['id']}')">
            <div class="area-card-head">
              <div class="area-icon-box">{st['icon']}</div>
              <div class="area-card-title-wrap">
                <span class="area-number-label">{st['num']}</span>
                <h4 class="area-card-name">{st['name']}</h4>
              </div>
              <span class="area-status-pill {st['status_class']}">{st['status_text']}</span>
            </div>

            <div class="progress-track" style="margin-bottom: 12px;">
              <div class="progress-fill {st['fill_class']}" style="width: {st['tot_pct']};"></div>
            </div>

            <div class="area-scores-box">
              <div class="score-row-mini">
                <span class="row-label">📋 Pemenuhan:</span>
                <span class="row-score">{st['pem_val']} ({st['pem_pct']})</span>
              </div>
              <div class="score-row-mini">
                <span class="row-label">🚀 Reform:</span>
                <span class="row-score">{st['ref_val']} ({st['ref_pct']})</span>
              </div>
              <div class="score-row-mini" style="border-top: 1px dashed var(--gray-300); padding-top: 4px; font-weight: 800;">
                <span class="row-label" style="color: var(--primary);">Total Nilai Area:</span>
                <span class="row-score" style="color: var(--primary);">{st['tot_val']}</span>
              </div>
            </div>

            <div class="area-card-footer">
              <span style="display: inline-flex; align-items: center; gap: 4px; color: { 'var(--danger)' if st['attention_count'] > 0 else 'var(--success)' }; font-size: 0.8rem;">
                {'⚠️ ' + str(st['attention_count']) + ' item perlu perhatian' if st['attention_count'] > 0 else '✅ Semua indikator optimal'}
              </span>
              <span>Buka Panduan &rarr;</span>
            </div>
          </div>
    """)

html_parts.append("""
        </div>
      </div>
    </div>
""")

# Render Area Panes (Area 1 - Area 6)
for area in data["areas"]:
    area_id = area["id"]
    html_parts.append(f"""
    <!-- ======================================================================
         PANE: {area['title'].upper()} ({area_id})
         ====================================================================== -->
    <div id="pane-{area_id}" class="area-pane">
      <!-- Area Hero Banner -->
      <div class="area-hero-banner">
        <div class="area-banner-top">
          <div>
            <span class="area-number-label">AREA {area['number']} PENGUNGKIT ZI</span>
            <h2 class="area-banner-title">
              <span>{area['icon']}</span>
              <span>{escape_html(area['title'])}</span>
            </h2>
          </div>
          <div class="area-banner-stats">
            <div class="stat-pill-banner">
              <span>📋 Pemenuhan:</span>
              <strong>{area['pemenuhan']['score']} / {area['pemenuhan']['max']} ({area['pemenuhan']['pct']})</strong>
            </div>
            <div class="stat-pill-banner">
              <span>🚀 Reform:</span>
              <strong>{area['reform']['score']} / {area['reform']['max']} ({area['reform']['pct']})</strong>
            </div>
          </div>
        </div>
        <p class="area-banner-desc">{escape_html(area['desc'])}</p>
      </div>
    """)

    # --- ASPEK PEMENUHAN ---
    pem = area["pemenuhan"]
    html_parts.append(f"""
      <section class="aspect-section">
        <div class="aspect-header">
          <div class="aspect-title-wrap">
            <h3 class="aspect-title">📋 Aspek Pemenuhan</h3>
            <span class="aspect-score-badge">Skor: {pem['score']} / {pem['max']} ({pem['pct']})</span>
          </div>
          <div class="aspect-actions">
            <button type="button" class="btn-toggle-all" onclick="toggleAspectCards('{area_id}-pem', true)">Buka Semua</button>
            <button type="button" class="btn-toggle-all" onclick="toggleAspectCards('{area_id}-pem', false)">Tutup Semua</button>
          </div>
        </div>
        <div id="{area_id}-pem-container">
    """)

    for grp in pem["groups"]:
        html_parts.append(f"""
          <div class="subgroup-block">
            <div class="subgroup-title">
              <span>{escape_html(grp['name'])}</span>
              <span class="subgroup-score">{grp['score']}</span>
            </div>
        """)

        for item in grp["items"]:
            status_border = "status-border-green" if item["status"] == "complete" else ("status-border-yellow" if item["status"] == "partial" else "status-border-red")
            badge_class = "good" if item["status"] == "complete" else ("warn" if item["status"] == "partial" else "bad")
            status_icon = "✅" if item["status"] == "complete" else ("⚠️" if item["status"] == "partial" else "❌")

            html_parts.append(f"""
            <div class="indicator-card {status_border}" data-status="{item['status']}" data-code="{item['code']}" data-area="{area_id}">
              <div class="indicator-header" onclick="toggleCard(this)">
                <div class="indicator-left">
                  <span class="indicator-code-badge">{item['code']}</span>
                  <div class="indicator-question">{escape_html(item['question'])}</div>
                </div>
                <div class="indicator-right">
                  <span class="badge-answer {badge_class}">
                    <span>{status_icon}</span>
                    <span>{escape_html(item['jawaban'])}</span>
                  </span>
                  <span class="indicator-score-box">Nilai: {item['nilai']}</span>
                  <span class="accordion-chevron">▼</span>
                </div>
              </div>

              <div class="indicator-body">
                <div class="indicator-body-grid">
            """)

            # Kriteria Nilai
            if item.get("kriteria"):
                html_parts.append(f"""
                  <div class="info-box criteria-box">
                    <div class="info-box-title">⚖️ Kriteria Penilaian</div>
                    <div class="criteria-text">{escape_html(item['kriteria'])}</div>
                  </div>
                """)

            # Narasi Satker
            if item.get("narasi"):
                html_parts.append(f"""
                  <div class="info-box narrative-box">
                    <div class="info-box-title">📝 Narasi Satker BPS Kepulauan Selayar</div>
                    <div class="narrative-text">"{escape_html(item['narasi'])}"</div>
                  </div>
                """)

            # Catatan Khusus jika ada
            if item.get("catatan"):
                html_parts.append(f"""
                  <div class="info-box notes-box">
                    <div class="info-box-title">⚠️ Catatan &amp; Arahan Penyelesaian</div>
                    <div class="notes-text">{escape_html(item['catatan'])}</div>
                  </div>
                """)

            # Bukti Dukung yang Diperlukan
            if item.get("bukti"):
                html_parts.append(f"""
                  <div class="evidence-section">
                    <div class="evidence-title">📑 Daftar Bukti Dukung yang Harus Disiapkan:</div>
                    <ul class="evidence-list">
                """)
                for b in item["bukti"]:
                    html_parts.append(f"""
                      <li class="evidence-item">
                        <span class="evidence-bullet">📌</span>
                        <span class="evidence-text">{escape_html(b)}</span>
                      </li>
                    """)
                html_parts.append("""
                    </ul>
                  </div>
                """)

            # Action Buttons
            html_parts.append(f"""
                  <div class="indicator-action-bar">
            """)

            if item.get("link_contoh"):
                html_parts.append(f"""
                    <a href="{item['link_contoh']}" target="_blank" rel="noopener noreferrer" class="btn-link-action btn-example-link" title="Buka tautan contoh bukti dukung resmi dari BPS Pusat">
                      <span>🔗</span>
                      <span>Contoh BPS Pusat</span>
                    </a>
                """)

            # Direct Drive button
            folder_title = item.get("drive_folder", f"Area_{area['number']}_{item['code']}")
            html_parts.append(f"""
                    <a href="{DRIVE_ROOT}" target="_blank" rel="noopener noreferrer" class="btn-link-action btn-drive-folder" title="Buka Folder Penyimpanan Google Drive">
                      <span>📁</span>
                      <span>Drive: {escape_html(folder_title)}</span>
                    </a>
                    <button type="button" class="btn-link-action btn-copy-evidence" onclick="copyEvidenceList('{escape_html(item['code'])}', this)" data-list='{json.dumps(item.get("bukti", []), ensure_ascii=False)}'>
                      <span>📋</span>
                      <span>Salin Bukti Dukung</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
            """)

        html_parts.append("""
          </div>
        """)

    html_parts.append("""
        </div>
      </section>
    """)

    # --- ASPEK REFORM ---
    ref = area["reform"]
    html_parts.append(f"""
      <section class="aspect-section">
        <div class="aspect-header" style="border-left-color: var(--primary);">
          <div class="aspect-title-wrap">
            <h3 class="aspect-title">🚀 Aspek Reform</h3>
            <span class="aspect-score-badge" style="background: var(--primary-soft); color: var(--primary); border-color: #bfdbfe;">Skor: {ref['score']} / {ref['max']} ({ref['pct']})</span>
          </div>
          <div class="aspect-actions">
            <button type="button" class="btn-toggle-all" onclick="toggleAspectCards('{area_id}-ref', true)">Buka Semua</button>
            <button type="button" class="btn-toggle-all" onclick="toggleAspectCards('{area_id}-ref', false)">Tutup Semua</button>
          </div>
        </div>
        <div id="{area_id}-ref-container">
    """)

    for grp in ref["groups"]:
        html_parts.append(f"""
          <div class="subgroup-block">
            <div class="subgroup-title" style="border-left-color: var(--gold);">
              <span>{escape_html(grp['name'])}</span>
              <span class="subgroup-score" style="color: var(--gold-dark);">{grp['score']}</span>
            </div>
        """)

        for item in grp["items"]:
            status_border = "status-border-green" if item["status"] == "complete" else ("status-border-yellow" if item["status"] == "partial" else "status-border-red")
            badge_class = "good" if item["status"] == "complete" else ("warn" if item["status"] == "partial" else "bad")
            status_icon = "✅" if item["status"] == "complete" else ("⚠️" if item["status"] == "partial" else "❌")

            html_parts.append(f"""
            <div class="indicator-card {status_border}" data-status="{item['status']}" data-code="{item['code']}" data-area="{area_id}">
              <div class="indicator-header" onclick="toggleCard(this)">
                <div class="indicator-left">
                  <span class="indicator-code-badge" style="background: var(--gold-soft); color: var(--gold-dark); border-color: var(--gold-light);">{item['code']}</span>
                  <div class="indicator-question">{escape_html(item['question'])}</div>
                </div>
                <div class="indicator-right">
                  <span class="badge-answer {badge_class}">
                    <span>{status_icon}</span>
                    <span>{escape_html(item['jawaban'])}</span>
                  </span>
                  <span class="indicator-score-box">Nilai: {item['nilai']}</span>
                  <span class="accordion-chevron">▼</span>
                </div>
              </div>

              <div class="indicator-body">
                <div class="indicator-body-grid">
            """)

            # Kriteria Nilai
            if item.get("kriteria"):
                html_parts.append(f"""
                  <div class="info-box criteria-box">
                    <div class="info-box-title">⚖️ Kriteria Penilaian</div>
                    <div class="criteria-text">{escape_html(item['kriteria'])}</div>
                  </div>
                """)

            # Narasi Satker
            if item.get("narasi"):
                html_parts.append(f"""
                  <div class="info-box narrative-box">
                    <div class="info-box-title">📝 Narasi Satker BPS Kepulauan Selayar</div>
                    <div class="narrative-text">"{escape_html(item['narasi'])}"</div>
                  </div>
                """)

            # Catatan Khusus
            if item.get("catatan"):
                html_parts.append(f"""
                  <div class="info-box notes-box">
                    <div class="info-box-title">⚠️ Catatan &amp; Arahan Penyelesaian</div>
                    <div class="notes-text">{escape_html(item['catatan'])}</div>
                  </div>
                """)

            # Bukti Dukung
            if item.get("bukti"):
                html_parts.append(f"""
                  <div class="evidence-section">
                    <div class="evidence-title">📑 Daftar Bukti Dukung yang Harus Disiapkan:</div>
                    <ul class="evidence-list">
                """)
                for b in item["bukti"]:
                    html_parts.append(f"""
                      <li class="evidence-item">
                        <span class="evidence-bullet">📌</span>
                        <span class="evidence-text">{escape_html(b)}</span>
                      </li>
                    """)
                html_parts.append("""
                    </ul>
                  </div>
                """)

            # Action Buttons
            html_parts.append(f"""
                  <div class="indicator-action-bar">
            """)

            if item.get("link_contoh"):
                html_parts.append(f"""
                    <a href="{item['link_contoh']}" target="_blank" rel="noopener noreferrer" class="btn-link-action btn-example-link" title="Buka tautan contoh bukti dukung resmi dari BPS Pusat">
                      <span>🔗</span>
                      <span>Contoh BPS Pusat</span>
                    </a>
                """)

            folder_title = item.get("drive_folder", f"Reform_{area['number']}_{item['code']}")
            html_parts.append(f"""
                    <a href="{DRIVE_ROOT}" target="_blank" rel="noopener noreferrer" class="btn-link-action btn-drive-folder" title="Buka Folder Penyimpanan Google Drive">
                      <span>📁</span>
                      <span>Drive: {escape_html(folder_title)}</span>
                    </a>
                    <button type="button" class="btn-link-action btn-copy-evidence" onclick="copyEvidenceList('{escape_html(item['code'])}', this)" data-list='{json.dumps(item.get("bukti", []), ensure_ascii=False)}'>
                      <span>📋</span>
                      <span>Salin Bukti Dukung</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
            """)

        html_parts.append("""
          </div>
        """)

    html_parts.append("""
        </div>
      </section>
    </div>
    """)

# Pane Komponen Hasil
hasil = data["hasil"]
html_parts.append(f"""
    <!-- ======================================================================
         PANE: KOMPONEN HASIL (B)
         ====================================================================== -->
    <div id="pane-hasil" class="area-pane">
      <div class="hasil-card-wrapper">
        <div class="section-header">
          <div class="section-title-wrap">
            <h2 class="section-title"><span>🏆</span> Komponen Hasil Evaluasi (Bobot 40.00)</h2>
            <span class="card-badge badge-gray" style="font-size: 0.9rem; padding: 6px 14px;">Status: Menunggu Survei Eksternal</span>
          </div>
        </div>

        <div class="hasil-notice">
          <strong>ℹ️ Informasi Penting Komponen Hasil:</strong><br>
          {escape_html(hasil['desc'])} Penilaian akan dilakukan melalui Survei Persepsi Korupsi (IPAK) dan Survei Kualitas Pelayanan (IPKP) kepada pengguna data dan pemangku kepentingan di Kabupaten Kepulauan Selayar.
        </div>

        <div class="hasil-sub-grid">
""")

for sub in hasil["sub"]:
    html_parts.append(f"""
          <div class="hasil-sub-card">
            <h3 class="hasil-sub-title">{escape_html(sub['title'])}</h3>
            <div class="hasil-sub-bobot">Bobot Komponen: {sub['bobot']} Poin</div>
    """)

    for itm in sub["items"]:
        html_parts.append(f"""
            <div class="hasil-item-card">
              <h4 class="hasil-item-name">{escape_html(itm['name'])}</h4>
              <div class="hasil-item-desc">{escape_html(itm['desc'])}</div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
                <span class="hasil-item-target">Target: {escape_html(itm['target'])}</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--gray-500);">{escape_html(itm['status'])}</span>
              </div>
            </div>
        """)

    html_parts.append("""
          </div>
    """)

html_parts.append("""
        </div>
      </div>
    </div>
""")

# Pane Checklist & Export Tracker
html_parts.append("""
    <!-- ======================================================================
         PANE: CHECKLIST & EXPORT TRACKER
         ====================================================================== -->
    <div id="pane-checklist" class="area-pane">
      <div class="checklist-section">
        <div class="section-header">
          <div class="section-title-wrap">
            <h2 class="section-title"><span>📋</span> Checklist Pemenuhan Bukti Dukung ZI</h2>
            <span class="section-desc">Gunakan checklist interaktif ini untuk melacak dan memverifikasi dokumen fisik/digital yang telah diunggah ke Google Drive</span>
          </div>
        </div>

        <div class="checklist-controls">
          <div class="checklist-stats">
            Status: <span id="chkCountVerified" style="color: var(--success); font-weight: 900;">0</span> dari <span id="chkCountTotal" style="font-weight: 900;">0</span> Bukti Dukung Terverifikasi (<span id="chkPctVerified">0%</span>)
          </div>
          <div class="checklist-actions-btns">
            <button type="button" class="btn-action-primary" onclick="exportChecklistCSV()">
              <span>📥</span>
              <span>Export ke CSV / Excel</span>
            </button>
            <button type="button" class="btn-action-outline" onclick="window.print()">
              <span>🖨️</span>
              <span>Cetak Checklist</span>
            </button>
            <button type="button" class="btn-action-outline" onclick="resetChecklistStorage()" style="color: var(--danger); border-color: var(--danger-border);">
              <span>🔄</span>
              <span>Reset Checklist</span>
            </button>
          </div>
        </div>

        <div class="table-responsive">
          <table class="checklist-table" id="checklistTable">
            <thead>
              <tr>
                <th class="chk-col">Cek</th>
                <th style="width: 100px;">Area</th>
                <th style="width: 90px;">Kode</th>
                <th style="width: 35%;">Pertanyaan Indikator</th>
                <th>Dokumen Bukti Dukung yang Diperlukan</th>
                <th style="width: 130px;">Status LKE</th>
              </tr>
            </thead>
            <tbody id="checklistTableBody">
              <!-- Dynamically populated via JavaScript -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
""")

# Pane Google Drive Guide
html_parts.append("""
    <!-- ======================================================================
         PANE: STRUKTUR GOOGLE DRIVE
         ====================================================================== -->
    <div id="pane-drive" class="area-pane">
      <div class="drive-guide-card">
        <div class="section-header">
          <div class="section-title-wrap">
            <h2 class="section-title"><span>📁</span> Rekomendasi Struktur Folder Google Drive</h2>
            <a href="https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-action-primary">
              <span>↗️</span>
              <span>Buka Google Drive ZI Selayar</span>
            </a>
          </div>
          <p class="section-desc" style="margin-top: 8px;">
            Struktur folder standar untuk mempermudah Tim Penilai Internal (TPI) dan Tim Penilai Nasional (TPN) memeriksa kelengkapan bukti dukung BPS Kabupaten Kepulauan Selayar:
          </p>
        </div>

        <div class="drive-tree-view">
<span class="folder-root">📁 [ROOT] Bukti Dukung ZI 2025 BPS Kab. Kepulauan Selayar</span>
│
├── <span class="folder-area">📁 01_Manajemen_Perubahan/</span>
│   ├── <span class="folder-sub">📁 Pemenuhan/</span>
│   │   ├── <span class="folder-item">📁 1a_SK_Tim_Kerja_ZI/</span>
│   │   ├── <span class="folder-item">📁 1b_Prosedur_Pemilihan_Tim/</span>
│   │   ├── <span class="folder-item">📁 2a_Dokumen_Rencana_Kerja/</span>
│   │   ├── <span class="folder-item">📁 2b_Target_Prioritas/</span>
│   │   ├── <span class="folder-item">📁 2c_Sosialisasi_Pembangunan_ZI/</span>
│   │   ├── <span class="folder-item">📁 3a_Pelaksanaan_Sesuai_Rencana/</span>
│   │   ├── <span class="folder-item">📁 3b_Dokumen_Monev_Triwulanan/ (⚠️ Prioritas)</span>
│   │   ├── <span class="folder-item">📁 3c_Tindak_Lanjut_Monev/</span>
│   │   ├── <span class="folder-item">📁 4a_Pimpinan_Sebagai_Role_Model/ (⚠️ Prioritas)</span>
│   │   ├── <span class="folder-item">📁 4b_Laporan_Agen_Perubahan/ (⚠️ Prioritas)</span>
│   │   ├── <span class="folder-item">📁 4c_Budaya_Kerja_Pola_Pikir/ (⚠️ Prioritas)</span>
│   │   └── <span class="folder-item">📁 4d_Keterlibatan_Anggota_ZI/ (⚠️ Prioritas)</span>
│   └── <span class="folder-sub">📁 Reform/</span>
│       ├── <span class="folder-item">📁 R1a_Inovasi_Agen_Perubahan/</span>
│       ├── <span class="folder-item">📁 R1b_Integrasi_Sistem_Manajemen/</span>
│       ├── <span class="folder-item">📁 R2_Komitmen_Pimpinan/</span>
│       └── <span class="folder-item">📁 R3_Membangun_Budaya_Kerja/</span>
│
├── <span class="folder-area">📁 02_Penataan_Tatalaksana/</span>
│   ├── <span class="folder-sub">📁 Pemenuhan/</span>
│   │   ├── <span class="folder-item">📁 1a_SOP_Proses_Bisnis/</span>
│   │   ├── <span class="folder-item">📁 1b_Penerapan_SOP/</span>
│   │   ├── <span class="folder-item">📁 1c_Evaluasi_SOP/</span>
│   │   ├── <span class="folder-item">📁 2a_TI_Pengukuran_Kinerja/</span>
│   │   ├── <span class="folder-item">📁 2b_TI_Manajemen_SDM/</span>
│   │   ├── <span class="folder-item">📁 2c_TI_Pelayanan_Publik/</span>
│   │   ├── <span class="folder-item">📁 2d_Monev_Pemanfaatan_TI/ (⚠️ Notulen & Daftar Hadir)</span>
│   │   ├── <span class="folder-item">📁 3a_Kebijakan_KIP_PPID/</span>
│   │   └── <span class="folder-item">📁 3b_Monev_KIP_Laporan_Tahunan/ (⚠️ Prioritas)</span>
│   └── <span class="folder-sub">📁 Reform/</span>
│       ├── <span class="folder-item">📁 R1_Peta_Proses_Bisnis/</span>
│       ├── <span class="folder-item">📁 R2a_SPBE_Eksternal/</span>
│       ├── <span class="folder-item">📁 R2b_SPBE_Internal/</span>
│       └── <span class="folder-item">📁 R3_Transformasi_Digital_CAPI_BOS/</span>
│
├── <span class="folder-area">📁 03_Manajemen_SDM/</span>
│   ├── <span class="folder-sub">📁 Pemenuhan/</span>
│   │   ├── <span class="folder-item">📁 1a_Peta_Jabatan_ABK/</span>
│   │   ├── <span class="folder-item">📁 2a_Mutasi_Internal/</span>
│   │   ├── <span class="folder-item">📁 3a_Training_Need_Analysis/</span>
│   │   ├── <span class="folder-item">📁 3b_Rencana_Pengembangan_Kinerja/ (⚠️ Prioritas)</span>
│   │   ├── <span class="folder-item">📁 3c_Analisis_Kesenjangan_Kompetensi/ (⚠️ Prioritas)</span>
│   │   ├── <span class="folder-item">📁 3d_Kesempatan_Diklat_20JP/ (⚠️ Prioritas)</span>
│   │   ├── <span class="folder-item">📁 3e_Knowledge_Sharing_Internal/ (⚠️ Prioritas)</span>
│   │   ├── <span class="folder-item">📁 3f_Monev_Dampak_Pelatihan/ (⚠️ Prioritas)</span>
│   │   ├── <span class="folder-item">📁 4a_SKP_Cascading_KipApp/</span>
│   │   ├── <span class="folder-item">📁 4d_Reward_EOM/</span>
│   │   └── <span class="folder-item">📁 5a_Disiplin_SIMPEG_SPT/</span>
│   └── <span class="folder-sub">📁 Reform/</span>
│       ├── <span class="folder-item">📁 R1_SKP_Berorientasi_Outcome/ (⚠️ Prioritas)</span>
│       ├── <span class="folder-item">📁 R2_Pemanfaatan_Asesmen_Pegawai/ (⚠️ Prioritas)</span>
│       └── <span class="folder-item">📁 R3_Rekap_Pelanggaran_Disiplin_Nihil/</span>
│
├── <span class="folder-area">📁 04_Penguatan_Akuntabilitas/</span>
│   ├── <span class="folder-sub">📁 Pemenuhan/</span>
│   │   ├── <span class="folder-item">📁 1a_Keterlibatan_Pimpinan_Perencanaan/</span>
│   │   ├── <span class="folder-item">📁 1b_Penyusunan_PK_MPH/</span>
│   │   ├── <span class="folder-item">📁 1c_Monev_Kinerja_Triwulanan/</span>
│   │   ├── <span class="folder-item">📁 2a_Dokumen_Renstra_PK/</span>
│   │   ├── <span class="folder-item">📁 2d_LAKIN_SMART/</span>
│   │   └── <span class="folder-item">📁 2h_Peningkatan_Kapasitas_SAKIP/</span>
│   └── <span class="folder-sub">📁 Reform/</span>
│       ├── <span class="folder-item">📁 R1_Capaian_Kinerja_Melampaui_Target/</span>
│       ├── <span class="folder-item">📁 R2_Reward_Punishment_Capaian_PK/ (⚠️ Prioritas)</span>
│       └── <span class="folder-item">📁 R3_Kerangka_Logis_Cascading/</span>
│
├── <span class="folder-area">📁 05_Penguatan_Pengawasan/</span>
│   ├── <span class="folder-sub">📁 Pemenuhan/</span>
│   │   ├── <span class="folder-item">📁 1a_Public_Campaign_Gratifikasi/</span>
│   │   ├── <span class="folder-item">📁 1b_Laporan_Monev_UPG/</span>
│   │   ├── <span class="folder-item">📁 2a_SK_Sosialisasi_SPIP/</span>
│   │   ├── <span class="folder-item">📁 2b_Register_Manajemen_Risiko/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 2c_Rencana_Tindak_Pengendalian_RTP/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 2d_Komunikasi_SPIP_Notulen/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 3a_SOP_SK_Pengaduan_Masyarakat/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 3b_Register_Tindak_Lanjut_Aduan/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 3c_Monev_Pengaduan_Berkala/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 3d_Tindak_Lanjut_Evaluasi_Aduan/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 4a_SK_Kanal_Sosialisasi_WBS/</span>
│   │   ├── <span class="folder-item">📁 5a_Identifikasi_Benturan_Kepentingan/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 5b_Sosialisasi_Benturan_Kepentingan/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 5c_Pernyataan_Bebas_Benturan/ (⚠️ Prioritas Kritis)</span>
│   │   ├── <span class="folder-item">📁 5d_Evaluasi_Benturan_Kepentingan/ (⚠️ Prioritas Kritis)</span>
│   │   └── <span class="folder-item">📁 5e_Tindak_Lanjut_Evaluasi_Benturan/ (⚠️ Prioritas Kritis)</span>
│   └── <span class="folder-sub">📁 Reform/</span>
│       ├── <span class="folder-item">📁 R1_Supervisi_Pengendalian_Berjenjang/</span>
│       ├── <span class="folder-item">📁 R2_Penyelesaian_Pengaduan_100/</span>
│       └── <span class="folder-item">📁 R3_Tanda_Terima_LHKPN_SPT/</span>
│
└── <span class="folder-area">📁 06_Peningkatan_Pelayanan_Publik/</span>
    ├── <span class="folder-sub">📁 Pemenuhan/</span>
    │   ├── <span class="folder-item">📁 1a_SK_Standar_Pelayanan/</span>
    │   ├── <span class="folder-item">📁 1b_Maklumat_Pelayanan/</span>
    │   ├── <span class="folder-item">📁 1c_FKP_Reviu_Standar/</span>
    │   ├── <span class="folder-item">📁 2a_Pelatihan_Service_Excellence/</span>
    │   ├── <span class="folder-item">📁 2b_Profil_Layanan_SIPPN/ (⚠️ Update 2025)</span>
    │   ├── <span class="folder-item">📁 2c_Reward_Punishment_Petugas_PST/ (⚠️ Prioritas)</span>
    │   ├── <span class="folder-item">📁 2d_Kompensasi_Keterlambatan_Layanan/ (⚠️ Prioritas)</span>
    │   ├── <span class="folder-item">📁 2e_Sarana_Prasarana_PST/</span>
    │   ├── <span class="folder-item">📁 2f_Proposal_Laporan_Inovasi_Layanan/ (⚠️ Prioritas Kritis)</span>
    │   ├── <span class="folder-item">📁 3a_Integrasi_SP4N_LAPOR/</span>
    │   ├── <span class="folder-item">📁 3c_Evaluasi_Penanganan_Keluhan/ (⚠️ Prioritas)</span>
    │   ├── <span class="folder-item">📁 4a_Laporan_SKD_SKM_TW4/ (⚠️ Update TW4)</span>
    │   ├── <span class="folder-item">📁 4b_Publikasi_Hasil_SKD_Website/</span>
    │   ├── <span class="folder-item">📁 4c_Tindak_Lanjut_Rekomendasi_SKD/ (⚠️ Prioritas)</span>
    │   └── <span class="folder-item">📁 5a_PST_Online_Romantik_Silastik/</span>
    └── <span class="folder-sub">📁 Reform/</span>
        ├── <span class="folder-item">📁 R1a_Dampak_Inovasi_Pelayanan/</span>
        ├── <span class="folder-item">📁 R1b_Penyederhanaan_Alur_Layanan/</span>
        └── <span class="folder-item">📁 R2_Monev_Pengaduan_Multi_Kanal/ (⚠️ Prioritas)</span>
        </div>
      </div>
    </div>
""")

# Footer & Toast Notification
html_parts.append(f"""
  </main>

  <!-- ========================================================================
       FOOTER
       ======================================================================== -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <div class="footer-brand-title">BPS KABUPATEN KEPULAUAN SELAYAR</div>
        <p class="footer-brand-desc">
          Panduan resmi pendataan dan penyusunan bukti dukung Zona Integritas (ZI) menuju predikat Wilayah Bebas dari Korupsi (WBK) dan Wilayah Birokrasi Bersih dan Melayani (WBBM) Tahun 2025.
        </p>
        <p style="margin-top: 12px; font-size: 0.8rem; color: #94a3b8;">
          📍 Jl. Kihajar Dewantara No. 1, Benteng, Kepulauan Selayar, Sulawesi Selatan 92812
        </p>
      </div>

      <div>
        <div class="footer-heading">Navigasi Area</div>
        <ul class="footer-links">
          <li><a href="javascript:void(0)" onclick="switchNavTab('dashboard')">📊 Ringkasan Nilai</a></li>
          <li><a href="javascript:void(0)" onclick="switchNavTab('area1')">1. Manajemen Perubahan</a></li>
          <li><a href="javascript:void(0)" onclick="switchNavTab('area2')">2. Penataan Tatalaksana</a></li>
          <li><a href="javascript:void(0)" onclick="switchNavTab('area3')">3. Manajemen SDM</a></li>
          <li><a href="javascript:void(0)" onclick="switchNavTab('area4')">4. Akuntabilitas Kinerja</a></li>
          <li><a href="javascript:void(0)" onclick="switchNavTab('area5')">5. Penguatan Pengawasan</a></li>
          <li><a href="javascript:void(0)" onclick="switchNavTab('area6')">6. Pelayanan Publik</a></li>
        </ul>
      </div>

      <div>
        <div class="footer-heading">Tautan Resmi</div>
        <ul class="footer-links">
          <li><a href="{DRIVE_ROOT}" target="_blank" rel="noopener noreferrer">📁 Google Drive Bukti Dukung</a></li>
          <li><a href="https://selayarkab.bps.go.id" target="_blank" rel="noopener noreferrer">🌐 Website BPS Kepulauan Selayar</a></li>
          <li><a href="https://lapor.go.id" target="_blank" rel="noopener noreferrer">📢 SP4N-LAPOR!</a></li>
          <li><a href="javascript:void(0)" onclick="switchNavTab('checklist')">📋 Checklist Kelengkapan</a></li>
          <li><a href="javascript:void(0)" onclick="switchNavTab('drive')">📂 Rekomendasi Struktur Drive</a></li>
        </ul>
      </div>
    </div>

    <div class="container footer-bottom">
      &copy; 2025 BPS Kabupaten Kepulauan Selayar. Seluruh Hak Cipta Dilindungi. Sistem Manajemen Bukti Dukung Zona Integritas.
    </div>
  </footer>

  <!-- Toast Notification element -->
  <div class="toast-container" id="toastContainer"></div>
""")

# Embedded JSON
html_parts.append(f"""
  <script>
    const APP_DATA = {json.dumps(data, ensure_ascii=False)};
  </script>
""")

# Pure JavaScript logic without f-string escaping
html_parts.append("""
  <script>
    // State
    let currentTab = 'dashboard';
    let isFilterAttentionOnly = false;
    let checkedItemsStorage = JSON.parse(localStorage.getItem('zi_selayar_checked_v1') || '{}');

    // Tab Navigation
    function switchNavTab(tabId) {
      currentTab = tabId;

      // Update Nav Buttons
      document.querySelectorAll('.nav-item-btn').forEach(btn => {
        btn.classList.remove('active');
        const onclickAttr = btn.getAttribute('onclick') || '';
        if (onclickAttr.includes(`'${tabId}'`)) {
          btn.classList.add('active');
        }
      });

      // Update Panes
      document.querySelectorAll('.area-pane').forEach(pane => {
        pane.classList.remove('active');
      });

      const targetPane = document.getElementById(`pane-${tabId}`);
      if (targetPane) {
        targetPane.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      // If opening checklist, re-render checklist table
      if (tabId === 'checklist') {
        renderChecklistTable();
      }
    }

    // Accordion Toggle
    function toggleCard(headerElement) {
      const card = headerElement.closest('.indicator-card');
      if (card) {
        card.classList.toggle('open');
      }
    }

    // Toggle All Cards in an Aspect Container
    function toggleAspectCards(containerId, openState) {
      const container = document.getElementById(`${containerId}-container`);
      if (container) {
        container.querySelectorAll('.indicator-card').forEach(card => {
          if (openState) {
            card.classList.add('open');
          } else {
            card.classList.remove('open');
          }
        });
      }
    }

    // Global Expand/Collapse All
    function expandAllIndicators(openState) {
      document.querySelectorAll('.indicator-card').forEach(card => {
        if (openState) {
          card.classList.add('open');
        } else {
          card.classList.remove('open');
        }
      });
      showToast(openState ? 'Membuka seluruh rincian indikator' : 'Menutup seluruh rincian indikator');
    }

    // Attention Filter Toggle
    function toggleAttentionFilter() {
      isFilterAttentionOnly = !isFilterAttentionOnly;
      const topBtn = document.getElementById('topFilterWarningBtn');
      const textSpan = document.getElementById('filterWarningText');
      const pillBtn = document.getElementById('filterPillAttention');
      const allPillBtn = document.getElementById('filterPillAll');

      if (isFilterAttentionOnly) {
        topBtn.classList.add('is-filtering');
        textSpan.textContent = 'Tampilkan Semua (Batal Filter)';
        pillBtn.classList.add('active-warning');
        allPillBtn.classList.remove('active');
        applyFilterVisibility('attention');
        showToast('Memfilter hanya item yang perlu perhatian / nilai < 1.00');
      } else {
        topBtn.classList.remove('is-filtering');
        textSpan.textContent = 'Perlu Perhatian (25)';
        pillBtn.classList.remove('active-warning');
        allPillBtn.classList.add('active');
        applyFilterVisibility('all');
        showToast('Menampilkan seluruh indikator');
      }
    }

    // Quick Filter (All / Attention / Complete)
    function setQuickFilter(type) {
      document.querySelectorAll('.pill-filter-btn').forEach(btn => {
        btn.classList.remove('active', 'active-warning');
      });

      if (type === 'attention') {
        isFilterAttentionOnly = true;
        document.getElementById('filterPillAttention').classList.add('active-warning');
        document.getElementById('topFilterWarningBtn').classList.add('is-filtering');
        document.getElementById('filterWarningText').textContent = 'Tampilkan Semua (Batal Filter)';
        applyFilterVisibility('attention');
      } else if (type === 'complete') {
        isFilterAttentionOnly = false;
        document.getElementById('filterPillComplete').classList.add('active');
        document.getElementById('topFilterWarningBtn').classList.remove('is-filtering');
        document.getElementById('filterWarningText').textContent = 'Perlu Perhatian (25)';
        applyFilterVisibility('complete');
      } else {
        isFilterAttentionOnly = false;
        document.getElementById('filterPillAll').classList.add('active');
        document.getElementById('topFilterWarningBtn').classList.remove('is-filtering');
        document.getElementById('filterWarningText').textContent = 'Perlu Perhatian (25)';
        applyFilterVisibility('all');
      }
    }

    function applyFilterVisibility(type) {
      document.querySelectorAll('.indicator-card').forEach(card => {
        const status = card.getAttribute('data-status');
        if (type === 'attention') {
          if (status === 'missing' || status === 'partial') {
            card.style.display = 'block';
            card.classList.add('open');
          } else {
            card.style.display = 'none';
          }
        } else if (type === 'complete') {
          if (status === 'complete') {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        } else {
          card.style.display = 'block';
        }
      });
    }

    // Live Search
    function handleLiveSearch(query) {
      const q = query.trim().toLowerCase();
      if (!q) {
        applyFilterVisibility(isFilterAttentionOnly ? 'attention' : 'all');
        return;
      }

      document.querySelectorAll('.indicator-card').forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(q)) {
          card.style.display = 'block';
          card.classList.add('open');
        } else {
          card.style.display = 'none';
        }
      });
    }

    // Copy Evidence List to Clipboard
    function copyEvidenceList(code, btn) {
      try {
        const rawList = btn.getAttribute('data-list');
        const list = JSON.parse(rawList || '[]');
        if (list.length === 0) return;

        const formatted = `Daftar Bukti Dukung Indikator ${code} - BPS Kab. Kepulauan Selayar:
` +
          list.map((item, idx) => `${idx + 1}. ${item}`).join(String.fromCharCode(10));

        navigator.clipboard.writeText(formatted).then(() => {
          showToast(`Berhasil menyalin ${list.length} bukti dukung indikator ${code}!`);
        }).catch(() => {
          // Fallback
          const textarea = document.createElement('textarea');
          textarea.value = formatted;
          document.body.appendChild(textarea);
          textarea.select();
          document.execCommand('copy');
          document.body.removeChild(textarea);
          showToast(`Berhasil menyalin bukti dukung ${code}!`);
        });
      } catch (err) {
        console.error(err);
      }
    }

    // Toast Notification Utility
    function showToast(message) {
      const container = document.getElementById('toastContainer');
      if (!container) return;

      const toast = document.createElement('div');
      toast.className = 'toast';
      toast.innerHTML = `<span>🔔</span><span>${message}</span>`;

      container.appendChild(toast);
      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(12px)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
      }, 3200);
    }

    // Checklist Generator & Tracker
    function getAllEvidenceItems() {
      const items = [];
      APP_DATA.areas.forEach(area => {
        // Pemenuhan
        area.pemenuhan.groups.forEach(grp => {
          grp.items.forEach(itm => {
            items.push({
              areaNum: area.number,
              areaTitle: area.title,
              aspect: 'Pemenuhan',
              code: itm.code,
              question: itm.question,
              bukti: itm.bukti || [],
              nilai: itm.nilai,
              status: itm.status,
              jawaban: itm.jawaban
            });
          });
        });
        // Reform
        area.reform.groups.forEach(grp => {
          grp.items.forEach(itm => {
            items.push({
              areaNum: area.number,
              areaTitle: area.title,
              aspect: 'Reform',
              code: itm.code,
              question: itm.question,
              bukti: itm.bukti || [],
              nilai: itm.nilai,
              status: itm.status,
              jawaban: itm.jawaban
            });
          });
        });
      });
      return items;
    }

    function renderChecklistTable() {
      const tbody = document.getElementById('checklistTableBody');
      if (!tbody) return;

      const items = getAllEvidenceItems();
      tbody.innerHTML = '';

      let totalEvidenceDocs = 0;
      let checkedEvidenceDocs = 0;

      items.forEach((item, index) => {
        const tr = document.createElement('tr');
        const key = `chk_${item.areaNum}_${item.aspect}_${item.code}`;
        const isChecked = !!checkedItemsStorage[key];

        totalEvidenceDocs += (item.bukti.length || 1);
        if (isChecked) {
          checkedEvidenceDocs += (item.bukti.length || 1);
        }

        const statusLabel = item.status === 'complete' ? 
          '<span class="badge-answer good" style="font-size:0.75rem;">✅ Lengkap</span>' :
          (item.status === 'partial' ? 
            '<span class="badge-answer warn" style="font-size:0.75rem;">⚠️ Sebagian</span>' : 
            '<span class="badge-answer bad" style="font-size:0.75rem;">❌ Belum Lengkap</span>');

        const buktiListHtml = item.bukti.length > 0 ? 
          '<ul style="margin: 0; padding-left: 18px; line-height: 1.5;">' +
            item.bukti.map(b => `<li style="margin-bottom: 4px;">${b}</li>`).join('') +
          '</ul>' :
          '<em style="color: var(--gray-400);">Lihat arahan LKE</em>';

        tr.innerHTML = `
          <td class="chk-col">
            <input type="checkbox" id="${key}" ${isChecked ? 'checked' : ''} onchange="toggleChecklistRow('${key}')">
          </td>
          <td><strong>Area ${item.areaNum}</strong><br><small style="color: var(--gray-500);">${item.aspect}</small></td>
          <td><span class="indicator-code-badge" style="font-size:0.75rem; padding: 2px 6px;">${item.code}</span></td>
          <td><strong>${item.question}</strong></td>
          <td>${buktiListHtml}</td>
          <td>${statusLabel}<br><small style="font-weight: 700; color: var(--gray-600);">Nilai: ${item.nilai}</small></td>
        `;

        tbody.appendChild(tr);
      });

      // Update counters
      document.getElementById('chkCountTotal').textContent = totalEvidenceDocs;
      document.getElementById('chkCountVerified').textContent = checkedEvidenceDocs;
      const pct = totalEvidenceDocs > 0 ? Math.round((checkedEvidenceDocs / totalEvidenceDocs) * 100) : 0;
      document.getElementById('chkPctVerified').textContent = `${pct}%`;
    }

    function toggleChecklistRow(key) {
      const cb = document.getElementById(key);
      if (cb) {
        if (cb.checked) {
          checkedItemsStorage[key] = true;
        } else {
          delete checkedItemsStorage[key];
        }
        localStorage.setItem('zi_selayar_checked_v1', JSON.stringify(checkedItemsStorage));
        renderChecklistTable();
      }
    }

    function resetChecklistStorage() {
      if (confirm('Apakah Anda yakin ingin mereset seluruh tanda checklist terverifikasi?')) {
        checkedItemsStorage = {};
        localStorage.removeItem('zi_selayar_checked_v1');
        renderChecklistTable();
        showToast('Checklist berhasil direset');
      }
    }

    // Export Checklist to CSV
    function exportChecklistCSV() {
      const items = getAllEvidenceItems();
      const rows = [];
      rows.push(['Area', 'Aspek', 'Kode', 'Pertanyaan', 'Daftar Bukti Dukung', 'Nilai', 'Status LKE', 'Verifikasi Mandiri']);

      items.forEach(itm => {
        const key = `chk_${itm.areaNum}_${itm.aspect}_${itm.code}`;
        const isChecked = !!checkedItemsStorage[key] ? 'SUDAH TERVERIFIKASI' : 'BELUM';
        const buktiClean = (itm.bukti || []).join(' | ').replace(/"/g, '""');
        const qClean = (itm.question || '').replace(/"/g, '""');

        rows.push([
          `Area ${itm.areaNum} - ${itm.areaTitle}`,
          itm.aspect,
          itm.code,
          qClean,
          buktiClean,
          itm.nilai,
          itm.status,
          isChecked
        ]);
      });

      const csvContent = rows.map(r => r.map(c => `"${String(c).replace(/"/g, '""')}"`).join(',')).join('\\n');
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', 'Checklist_Bukti_Dukung_ZI_BPS_Kepulauan_Selayar_2025.csv');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast('File CSV Checklist berhasil diunduh!');
    }

    // Initialize on DOMContentLoaded
    document.addEventListener('DOMContentLoaded', () => {
      renderChecklistTable();
    });
  </script>
</body>
</html>
""")

full_html = "".join(html_parts)
output_path = "/Volumes/work/_Projects/ZI/index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"HTML successfully generated at {output_path} with {len(full_html)} characters and {full_html.count(chr(10))} lines.")
