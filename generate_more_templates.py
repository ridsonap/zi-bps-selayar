import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from generate_docx_templates import add_header_bps, set_cell_background, set_cell_margins

# 7. Role Model Pimpinan
def make_role_model():
    doc = Document()
    add_header_bps(doc)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = p_title.add_run("LAPORAN PENERAPAN CORE VALUES BERAKHLAK PIMPINAN\nSEBAGAI ROLE MODEL DAN CHANGE LEADER\nBPS KABUPATEN KEPULAUAN SELAYAR TAHUN 2025")
    r_t.bold = True
    r_t.font.size = Pt(12)

    doc.add_heading("I. Dasar Hukum", level=2)
    doc.add_paragraph("1. Surat Edaran Menteri PANRB Nomor 20 Tahun 2021 tentang Implementasi Core Values dan Employer Branding ASN.\n"
                      "2. Perka BPS terkait Pedoman Pembangunan Zona Integritas.")

    doc.add_heading("II. Bukti Keteladanan Pimpinan (Role Model)", level=2)
    doc.add_paragraph("Kepala BPS Kabupaten Kepulauan Selayar secara konsisten menunjukkan keteladanan dalam:\n"
                      "1. Berorientasi Pelayanan: Turut serta secara berkala menyapa pengunjung Pelayanan Statistik Terpadu (PST) dan merespon umpan balik masyarakat.\n"
                      "2. Akuntabel: Tertib dan tepat waktu dalam pelaporan LHKPN (100% tepat waktu pada Januari 2025), serta presensi kehadiran apel pagi.\n"
                      "3. Kompeten: Menginisiasi kegiatan sharing knowledge rutin mingguan bagi seluruh fungsional statistisi dan pranata komputer.\n"
                      "4. Harmonis: Menjaga iklim kerja yang inklusif, menghargai keberagaman, dan menyelesaikan kendala internal secara musyawarah.\n"
                      "5. Loyal: Menegakkan kepatuhan terhadap kode etik BPS dan menjaga integritas data statistik yang independen.\n"
                      "6. Adaptif: Mendorong transformasi digital proses kerja melalui optimalisasi aplikasi BOS, KipApp, dan pemanfaatan CAPI survei.\n"
                      "7. Kolaboratif: Membangun sinergi data Satu Data Indonesia (SDI) bersama Bappeda dan Diskominfo-SP Kabupaten Kepulauan Selayar.")

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.add_run("Benteng, 31 Desember 2025\nKepala BPS Kabupaten Kepulauan Selayar,\n\n\n\n(Nama Kepala BPS)\nNIP. 19xxxxxxxxxxxxxx")
    doc.save("templates/Format_07_Laporan_Penerapan_Role_Model_Pimpinan_BPS_Selayar.docx")

# 8. Laporan Agen Perubahan
def make_laporan_agen_perubahan():
    doc = Document()
    add_header_bps(doc)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = p_title.add_run("LAPORAN IMPLEMENTASI PROGRAM KERJA AGEN PERUBAHAN\n(CHANGE AMBASSADOR)\nBPS KABUPATEN KEPULAUAN SELAYAR TAHUN 2025")
    r_t.bold = True
    r_t.font.size = Pt(12)

    doc.add_heading("I. Profil Agen Perubahan", level=2)
    doc.add_paragraph("Nama Agen Perubahan : .......................................................................\n"
                      "Jabatan              : Statistisi Ahli Pertama / Pranata Komputer\n"
                      "SK Penetapan         : Keputusan Kepala BPS Kab. Kepulauan Selayar No. B-015/73010/OT.000/01/2025")

    doc.add_heading("II. Rencana dan Realisasi Program Perubahan", level=2)
    doc.add_paragraph("1. Inovasi 1: Digitalisasi Arsip Bukti Dukung ZI Berbasis Google Drive Terstruktur\n"
                      "   Deskripsi: Mengintegrasikan seluruh berkas fisik ke dalam sistem penyimpanan awan yang rapi dan mudah diakses tim evaluasi.\n"
                      "2. Inovasi 2: Kampanye Internal '5S di Pelayanan PST' (Senyum, Sapa, Salam, Sopan, Santun)\n"
                      "   Deskripsi: Meningkatkan keramahan dan kecepatan waktu tanggap loket konsultasi statistik.\n"
                      "3. Inovasi 3: Morning Briefing Mingguan Peningkatan Kualitas Data CAPI\n"
                      "   Deskripsi: Monitoring anomali isian survei secara real-time untuk meminimalkan re-cacah lapangan.")

    doc.add_heading("III. Dampak Perubahan", level=2)
    doc.add_paragraph("Program kerja agen perubahan terbukti meningkatkan kedisiplinan kerja, mengurangi waktu pencarian dokumen bukti dukung dari semula 30 menit menjadi kurang dari 1 menit, serta mendukung kelancaran evaluasi TPI.")

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.add_run("Benteng, 15 Desember 2025\nAgen Perubahan (Change Ambassador),\n\n\n\n(......................................................)\nNIP. ...............................................")
    doc.save("templates/Format_08_Laporan_Agen_Perubahan_BPS_Selayar.docx")

# 9. Kertas Kerja Evaluasi SOP
def make_evaluasi_sop():
    doc = Document()
    add_header_bps(doc)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = p_title.add_run("KERTAS KERJA MONITORING DAN EVALUASI SOP ADMINISTRASI PEMERINTAHAN\nBPS KABUPATEN KEPULAUAN SELAYAR TAHUN 2025")
    r_t.bold = True
    r_t.font.size = Pt(12)

    doc.add_heading("I. Latar Belakang", level=2)
    doc.add_paragraph("Evaluasi berkala terhadap Standar Operasional Prosedur (SOP) dilakukan sesuai Perka BPS Nomor 19 Tahun 2013 guna memastikan seluruh prosedur kerja tetap relevan dengan dinamika regulasi dan transformasi digital sistem kerja terkini.")

    doc.add_heading("II. Matriks Evaluasi SOP Teknis dan Non-Teknis", level=2)
    table = doc.add_table(rows=1, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    hdr[0].text = "No"
    hdr[1].text = "Judul SOP"
    hdr[2].text = "Kondisi Eksisting"
    hdr[3].text = "Permasalahan / Hambatan"
    hdr[4].text = "Rekomendasi Perbaikan"
    for c in hdr:
        set_cell_background(c, "1A365D")
        for p in c.paragraphs:
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

    data_sop = [
        ("1", "SOP Pelayanan Statistik Terpadu (PST)", "Pelayanan manual & online", "Pencatatan tamu masih ganda", "Integrasikan buku tamu digital dengan Simpel BPS"),
        ("2", "SOP Pengelolaan Surat Masuk / Keluar", "Surat fisik dan BOS", "Arsip digital belum otomatis terklasifikasi", "Optimalkan fitur agenda surat masuk pada BOS BPS"),
        ("3", "SOP Pelaksanaan Survei CAPI", "Penggunaan aplikasi CAPI Fasih", "Sinkronisasi data lapangan kadang terhambat sinyal pulau", "Tetapkan SOP upload data offline berkala di titik jaringan")
    ]
    for row_d in data_sop:
        row = table.add_row().cells
        for idx, val in enumerate(row_d):
            row[idx].text = val
            set_cell_margins(row[idx], 60, 60, 80, 80)

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.add_run("Benteng, 10 Oktober 2025\nTim Evaluasi SOP,\n\n\n\n(......................................................)\nNIP. ...............................................")
    doc.save("templates/Format_09_Kertas_Kerja_Evaluasi_SOP_BPS_Selayar.docx")

# 10. Laporan Pengelolaan Pengaduan & WBS
def make_laporan_pengaduan_wbs():
    doc = Document()
    add_header_bps(doc)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = p_title.add_run("LAPORAN PENGELOLAAN PENGADUAN MASYARAKAT DAN WHISTLEBLOWING SYSTEM (WBS)\nBPS KABUPATEN KEPULAUAN SELAYAR\nTAHUN 2025")
    r_t.bold = True
    r_t.font.size = Pt(12)

    doc.add_heading("I. Rekapitulasi Pengaduan Masyarakat (SP4N-LAPOR!)", level=2)
    doc.add_paragraph("Kanal Pengaduan yang disediakan: Kotak Pengaduan PST, SP4N-LAPOR! (lapor.go.id), Email Resmi (bps7301@bps.go.id), dan WhatsApp Pengaduan Satker.\n"
                      "- Jumlah Aduan Diterima: 0 aduan\n"
                      "- Jumlah Aduan Diproses: 0 aduan\n"
                      "- Jumlah Aduan Selesai: 0 aduan (Tingkat Penyelesaian 100%)\n"
                      "Keterangan: Seluruh layanan statistik dan pengadaan barang/jasa berjalan sesuai SOP dan tidak ada pengaduan penyimpangan dari masyarakat.")

    doc.add_heading("II. Pengelolaan Whistleblowing System (WBS)", level=2)
    doc.add_paragraph("Aplikasi WBS Inspektorat Utama BPS telah disosialisasikan dan link telah dipasang pada website resmi selayarkab.bps.go.id serta banner fisik di kantor BPS Kab. Kepulauan Selayar.\n"
                      "- Laporan WBS Masuk: 0 laporan\n"
                      "- Kepatuhan Penanganan: 100%")

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.add_run("Benteng, 31 Desember 2025\nPetugas Pengelola Pengaduan,\n\n\n\n(......................................................)\nNIP. ...............................................")
    doc.save("templates/Format_10_Laporan_Pengelolaan_Pengaduan_dan_WBS_BPS_Selayar.docx")

make_role_model()
make_laporan_agen_perubahan()
make_evaluasi_sop()
make_laporan_pengaduan_wbs()
print("All 10 Word templates created successfully.")
