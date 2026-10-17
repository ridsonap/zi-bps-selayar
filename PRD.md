# PRD – Panduan Penyusunan Bukti Dukung ZI (Zona Integritas)
## BPS Kabupaten Kepulauan Selayar

### 1. Latar Belakang
Penyusunan bukti dukung LKE (Lembar Kerja Evaluasi) Pembangunan Zona Integritas menuju WBK/WBBM seringkali membingungkan bagi satuan kerja. Dokumen yang harus disiapkan banyak, tersebar, dan struktur penamaannya tidak seragam. Web ini dibuat agar tim ZI BPS Kabupaten Kepulauan Selayar memiliki panduan yang jelas, terstruktur, dan bisa langsung diunduh format bukti dukungnya.

### 2. Tujuan Produk
- Menyediakan panduan lengkap penyusunan bukti dukung ZI secara terstruktur per area perubahan
- Memberikan contoh isi bukti dukung untuk setiap indikator (atas nama BPS Kabupaten Kepulauan Selayar)
- Menyediakan template/format bukti dukung yang bisa diunduh
- Menyediakan link langsung ke Google Drive penyimpanan bukti dukung
- Menampilkan progress/skor penilaian mandiri per area

### 3. Target Pengguna
- Tim Kerja Pembangunan ZI BPS Kabupaten Kepulauan Selayar
- Kepala BPS Kabupaten Kepulauan Selayar (monitoring)
- Agen Perubahan dan seluruh pegawai satker

### 4. Fitur Utama

#### 4.1 Dashboard Ringkasan
- Skor total penilaian mandiri (46.70 dari 100)
- Breakdown per area perubahan (6 area + Hasil)
- Visual progress bar per area
- Status: hijau (≥80%), kuning (50-79%), merah (<50%)

#### 4.2 Panduan Per Area Perubahan
6 area pengungkit + komponen hasil:
1. **Manajemen Perubahan** (bobot 4.00, capaian 63.54%)
2. **Penataan Tatalaksana** (bobot 3.50, capaian 96.43%)
3. **Penataan Sistem Manajemen SDM Aparatur** (bobot 5.00, capaian 79.17%)
4. **Penguatan Akuntabilitas** (bobot 5.00, capaian 100%)
5. **Penguatan Pengawasan** (bobot 7.50, capaian 45%)
6. **Peningkatan Kualitas Pelayanan Publik** (bobot 5.00, capaian 78.90%)

Setiap indikator menampilkan:
- Pertanyaan/indikator
- Kriteria penilaian (A/B/C/D/E atau Ya/Tidak)
- Jawaban yang dipilih + nilai
- Bukti dukung yang diperlukan
- Link contoh bukti dukung dari BPS Pusat
- Link folder Google Drive untuk upload

#### 4.3 Aspek Reform
Setiap area juga memiliki komponen Reform yang ditampilkan terpisah.

#### 4.4 Download Format Bukti Dukung
- Template narasi per indikator
- Checklist kelengkapan bukti dukung (Excel/PDF)
- Struktur folder Google Drive

#### 4.5 Link Penyimpanan
Setiap bukti dukung terhubung ke folder Google Drive:
`https://drive.google.com/drive/folders/16lT-0q81UKuSPrtD-_UGcEj4Nh2Jms_3`

### 5. Arsitektur Teknis
- **Frontend**: Single HTML file (vanilla HTML/CSS/JS)
- **Data**: Embedded JSON dari spreadsheet LKE
- **Hosting**: GitHub Pages (gratis, custom domain support)
- **No backend required** – semua data statis

### 6. Struktur Navigasi
```
Beranda (Dashboard)
├── Area 1: Manajemen Perubahan
│   ├── Aspek Pemenuhan
│   └── Aspek Reform
├── Area 2: Penataan Tatalaksana
│   ├── Aspek Pemenuhan
│   └── Aspek Reform
├── Area 3: Manajemen SDM
│   ├── Aspek Pemenuhan
│   └── Aspek Reform
├── Area 4: Penguatan Akuntabilitas
│   ├── Aspek Pemenuhan
│   └── Aspek Reform
├── Area 5: Penguatan Pengawasan
│   ├── Aspek Pemenuhan
│   └── Aspek Reform
├── Area 6: Pelayanan Publik
│   ├── Aspek Pemenuhan
│   └── Aspek Reform
├── Komponen Hasil
└── Download Template
```

### 7. Deployment
- GitHub Pages dari branch `main`
- URL: `https://<username>.github.io/ZI/`
- Auto-deploy on push

### 8. Timeline
- Fase 1: Build & deploy (sekarang)
- Fase 2: Update data sesuai progress pengumpulan bukti dukung
