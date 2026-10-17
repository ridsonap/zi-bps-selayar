with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add nav button
nav_needle = '<button type="button" class="nav-item-btn" onclick="switchNavTab(\'drive\')">📁 Folder Drive</button>'
nav_replacement = nav_needle + '\n        <button type="button" class="nav-item-btn" onclick="switchNavTab(\'templates\')">📥 Unduh Format</button>'
assert nav_needle in html, "nav_needle not found"
html = html.replace(nav_needle, nav_replacement)

# 2. Add hero button
hero_needle = '<button type="button" class="hero-btn-secondary" onclick="switchNavTab(\'checklist\')">'
hero_replacement = '<button type="button" class="hero-btn-secondary" onclick="switchNavTab(\'templates\')">\n          <span>📥</span>\n          <span>Unduh Format Dokumen</span>\n        </button>\n        ' + hero_needle
assert hero_needle in html, "hero_needle not found"
html = html.replace(hero_needle, hero_replacement)

# 3. Add Excel download button in checklist
chk_needle = '<button type="button" class="btn-action-primary" onclick="exportChecklistCSV()">'
chk_replacement = '<a href="templates/Checklist_Bukti_Dukung_ZI_BPS_Kepulauan_Selayar_2025.xlsx" download class="btn-action-primary" style="background: #166534; text-decoration: none;">\n              <span>📊</span>\n              <span>Unduh Format Excel (.xlsx)</span>\n            </a>\n            ' + chk_needle
assert chk_needle in html, "chk_needle not found"
html = html.replace(chk_needle, chk_replacement)

# 4. Add pane-templates before </main>
templates_pane_html = """
    <!-- ======================================================================
         PANE: PUSAT UNDUHAN FORMAT BUKTI DUKUNG
         ====================================================================== -->
    <div id="pane-templates" class="area-pane">
      <div class="checklist-section">
        <div class="section-header">
          <div class="section-title-wrap">
            <h2 class="section-title"><span>📥</span> Pusat Unduhan Format &amp; Template Bukti Dukung</h2>
            <span class="section-desc">Format baku dokumen resmi bertuliskan <strong>Badan Pusat Statistik Kabupaten Kepulauan Selayar</strong> dalam format Microsoft Word (.docx) dan Microsoft Excel (.xlsx) siap pakai dan disesuaikan dengan LKE ZI 2025</span>
          </div>
          <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
            <a href="templates/Checklist_Bukti_Dukung_ZI_BPS_Kepulauan_Selayar_2025.xlsx" download class="btn-action-primary" style="background: #166534; text-decoration: none;">
              <span>📊</span>
              <span>Unduh Master Checklist Excel</span>
            </a>
            <a href="https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-action-outline">
              <span>↗️</span>
              <span>Buka Google Drive ZI Selayar</span>
            </a>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 20px; margin-top: 24px;">

          <!-- Card 0: Master Excel -->
          <div class="indicator-card" style="border-left: 4px solid #166534; padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: #dcfce7; color: #166534;">EXCEL (.XLSX)</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">19 KB • 110 Indikator</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                📊 Master Checklist LKE &amp; Ringkasan Nilai ZI 2025
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Buku kerja Excel berisi lembar Ringkasan Nilai per Area Pengungkit dan lembar Checklist Pemenuhan Bukti Dukung lengkap dengan status verifikasi.
              </p>
              <div style="font-size: 0.78rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px;">
                <strong>Peruntukan:</strong> Monitoring berkas oleh Ketua Tim ZI &amp; Kepala BPS Kab. Kepulauan Selayar.
              </div>
            </div>
            <a href="templates/Checklist_Bukti_Dukung_ZI_BPS_Kepulauan_Selayar_2025.xlsx" download class="btn-action-primary" style="background: #166534; justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Template Excel</span>
            </a>
          </div>

          <!-- Card 1: SK Tim ZI -->
          <div class="indicator-card" style="border-left: 4px solid var(--primary); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--primary-soft); color: var(--primary);">AREA 1 • WORD (.DOCX)</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">38 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 01: SK Tim Kerja Pembangunan ZI 2025
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Keputusan Kepala BPS Kab. Kepulauan Selayar tentang Pembentukan Tim Kerja Pembangunan ZI Menuju WBK/WBBM Tahun 2025 beserta lampiran susunan tim pada 6 Area Perubahan.
              </p>
              <div style="font-size: 0.78rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px;">
                <strong>Bukti Dukung Indikator:</strong> Area 1 (1.a &amp; R.1.a)
              </div>
            </div>
            <a href="templates/Format_01_SK_Tim_Pembangunan_ZI_2025_BPS_Selayar.docx" download class="btn-action-primary" style="justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 2: Notula Pembentukan Tim -->
          <div class="indicator-card" style="border-left: 4px solid var(--primary); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--primary-soft); color: var(--primary);">AREA 1 • WORD (.DOCX)</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">38 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 02: Notula Rapat &amp; Prosedur Pemilihan Tim
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Notula rapat pembentukan tim, kriteria objektif penentuan anggota, mekanisme pemilihan yang mewakili seluruh fungsi di BPS Kab. Kepulauan Selayar.
              </p>
              <div style="font-size: 0.78rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px;">
                <strong>Bukti Dukung Indikator:</strong> Area 1 (1.b)
              </div>
            </div>
            <a href="templates/Format_02_Notula_Rapat_Pembentukan_Tim_ZI_BPS_Selayar.docx" download class="btn-action-primary" style="justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 3: Bebas Benturan Kepentingan -->
          <div class="indicator-card" style="border-left: 4px solid var(--danger); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--danger-light); color: var(--danger);">AREA 5 • PRIORITAS KRITIS</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">38 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 03: Surat Pernyataan Bebas Benturan Kepentingan
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Format resmi surat pernyataan bebas benturan kepentingan sesuai Perka BPS No. 36 Tahun 2023 untuk PPK, Pejabat Pengadaan, Panitia Rekrutmen Mitra, dan Pimpinan.
              </p>
              <div style="font-size: 0.78rem; background: var(--danger-light); border: 1px solid var(--danger-border); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px; color: var(--danger-dark);">
                <strong>Wajib Diisi:</strong> Skor saat ini 0.00 (Area 5.v.c). Seluruh pejabat &amp; tim wajib bertanda tangan.
              </div>
            </div>
            <a href="templates/Format_03_Surat_Pernyataan_Bebas_Benturan_Kepentingan_BPS_Selayar.docx" download class="btn-action-primary" style="background: var(--danger); justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 4: Laporan Monev ZI -->
          <div class="indicator-card" style="border-left: 4px solid var(--primary); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--primary-soft); color: var(--primary);">AREA 1 • WORD (.DOCX)</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">38 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 04: Laporan Monev ZI Triwulanan
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Dokumen laporan monitoring dan evaluasi triwulanan yang memuat analisa kendala, matriks capaian 6 area, dan rekomendasi tindak lanjut yang dipimpin Kepala BPS Selayar.
              </p>
              <div style="font-size: 0.78rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px;">
                <strong>Bukti Dukung Indikator:</strong> Area 1 (3.b &amp; 3.c)
              </div>
            </div>
            <a href="templates/Format_04_Laporan_Monev_ZI_Triwulan_BPS_Selayar.docx" download class="btn-action-primary" style="justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 5: Pakta Integritas -->
          <div class="indicator-card" style="border-left: 4px solid var(--primary); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--primary-soft); color: var(--primary);">AREA 1 &amp; 5 • WORD (.DOCX)</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">38 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 05: Pakta Integritas Pegawai ZI 2025
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Pernyataan komitmen bebas KKN, penolakan gratifikasi, dan kepatuhan Core Values BerAKHLAK yang ditandatangani oleh seluruh pegawai BPS Kabupaten Kepulauan Selayar.
              </p>
              <div style="font-size: 0.78rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px;">
                <strong>Bukti Dukung Indikator:</strong> Area 1 (4.d) &amp; Area 5 (1.a)
              </div>
            </div>
            <a href="templates/Format_05_Pakta_Integritas_Pegawai_BPS_Selayar.docx" download class="btn-action-primary" style="justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 6: Reward Punishment PST -->
          <div class="indicator-card" style="border-left: 4px solid var(--warning); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--warning-light); color: var(--warning);">AREA 6 • PRIORITAS</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">38 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 06: Kebijakan Reward &amp; Punishment PST
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Pedoman dan SOP formal pemberian penghargaan dan sanksi bagi petugas pemberi layanan Pelayanan Statistik Terpadu (PST) berdasarkan disiplin, kinerja, dan kepuasan tamu.
              </p>
              <div style="font-size: 0.78rem; background: var(--warning-light); border: 1px solid var(--warning-border); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px; color: var(--warning-dark);">
                <strong>Bukti Dukung Indikator:</strong> Area 6 (2.c) — Nilai saat ini 0.00
              </div>
            </div>
            <a href="templates/Format_06_Pedoman_Reward_Punishment_Petugas_Layanan_BPS_Selayar.docx" download class="btn-action-primary" style="background: var(--warning-dark); justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 7: Role Model Pimpinan -->
          <div class="indicator-card" style="border-left: 4px solid var(--primary); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--primary-soft); color: var(--primary);">AREA 1 • WORD (.DOCX)</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">37 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 07: Laporan Penerapan Role Model Pimpinan
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Laporan pelaksanaan keteladanan nilai BerAKHLAK oleh Kepala BPS Kab. Kepulauan Selayar sebagai role model dan agen perubahan pimpinan.
              </p>
              <div style="font-size: 0.78rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px;">
                <strong>Bukti Dukung Indikator:</strong> Area 1 (4.a) &amp; Reform 2
              </div>
            </div>
            <a href="templates/Format_07_Laporan_Penerapan_Role_Model_Pimpinan_BPS_Selayar.docx" download class="btn-action-primary" style="justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 8: Agen Perubahan -->
          <div class="indicator-card" style="border-left: 4px solid var(--primary); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--primary-soft); color: var(--primary);">AREA 1 • WORD (.DOCX)</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">37 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 08: Laporan Agen Perubahan (Change Ambassador)
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Laporan konkret realisasi program inovasi kerja agen perubahan yang telah diintegrasikan ke dalam sistem kerja manajemen BPS Kab. Kepulauan Selayar.
              </p>
              <div style="font-size: 0.78rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px;">
                <strong>Bukti Dukung Indikator:</strong> Area 1 (4.b, R.1.a, R.1.b)
              </div>
            </div>
            <a href="templates/Format_08_Laporan_Agen_Perubahan_BPS_Selayar.docx" download class="btn-action-primary" style="justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 9: Evaluasi SOP -->
          <div class="indicator-card" style="border-left: 4px solid var(--primary); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--primary-soft); color: var(--primary);">AREA 2 • WORD (.DOCX)</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">37 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 09: Kertas Kerja Evaluasi &amp; Reviu SOP
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Kertas kerja berkala untuk memonitor, mengevaluasi, dan merekomendasikan pembaruan Standar Operasional Prosedur (SOP) sesuai Perka BPS 19/2013.
              </p>
              <div style="font-size: 0.78rem; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px;">
                <strong>Bukti Dukung Indikator:</strong> Area 2 (1.c)
              </div>
            </div>
            <a href="templates/Format_09_Kertas_Kerja_Evaluasi_SOP_BPS_Selayar.docx" download class="btn-action-primary" style="justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

          <!-- Card 10: Pengaduan & WBS -->
          <div class="indicator-card" style="border-left: 4px solid var(--danger); padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <span class="indicator-code-badge" style="background: var(--danger-light); color: var(--danger);">AREA 5 • PRIORITAS KRITIS</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--gray-500);">37 KB</span>
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--gray-900); margin-bottom: 6px;">
                Format 10: Laporan Pengelolaan Aduan &amp; WBS
              </h3>
              <p style="font-size: 0.85rem; color: var(--gray-600); line-height: 1.5; margin-bottom: 12px;">
                Format laporan komprehensif penanganan aduan SP4N-LAPOR!, kotak aduan luring, hotline WhatsApp, dan Whistleblowing System (termasuk format laporan nihil).
              </p>
              <div style="font-size: 0.78rem; background: var(--danger-light); border: 1px solid var(--danger-border); border-radius: var(--radius-sm); padding: 8px; margin-bottom: 16px; color: var(--danger-dark);">
                <strong>Bukti Dukung Indikator:</strong> Area 5 (3.b, 3.c, 3.d &amp; 4.a) — Nilai saat ini 0.00
              </div>
            </div>
            <a href="templates/Format_10_Laporan_Pengelolaan_Pengaduan_dan_WBS_BPS_Selayar.docx" download class="btn-action-primary" style="background: var(--danger); justify-content: center; text-decoration: none;">
              <span>⬇️</span>
              <span>Unduh Dokumen (.docx)</span>
            </a>
          </div>

        </div>
      </div>
    </div>
"""

main_close = "  </main>"
assert main_close in html, "main_close not found"
html = html.replace(main_close, templates_pane_html + "\n" + main_close)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with templates pane and nav links!")
