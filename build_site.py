# -*- coding: utf-8 -*-
import json
import os

data = {
    "areas": [
        {
            "id": "area1",
            "number": 1,
            "title": "Manajemen Perubahan",
            "icon": "🔄",
            "desc": "Bertujuan untuk mengubah secara sistematis dan konsisten mekanisme kerja, pola pikir (mind set), serta budaya kerja (culture set) individu pada BPS Kabupaten Kepulauan Selayar agar menjadi lebih baik sesuai dengan tujuan dan sasaran pembangunan ZI Menuju WBK/WBBM.",
            "pemenuhan": {
                "score": "2.54",
                "max": "4.00",
                "pct": "63.54%",
                "status": "warning",
                "groups": [
                    {
                        "name": "i. Penyusunan Tim Kerja",
                        "score": "0.50 / 0.50 (100%)",
                        "items": [
                            {
                                "code": "1.a",
                                "question": "Unit kerja telah membentuk tim untuk melakukan pembangunan Zona Integritas",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Jika unit kerja telah membentuk tim kerja pembangunan ZI yang ditetapkan dengan Surat Keputusan (SK) Kepala Unit Kerja.\n• Tidak: Jika belum dibentuk atau tidak ada SK.",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "BPS Kabupaten Kepulauan Selayar telah membentuk tim kerja didalam unit untuk melakukan pembangunan Zona Integritas, terlihat dari bukti dukung berupa SK tim kerja dan SK Reformasi Birokrasi tahun 2025.",
                                "catatan": "",
                                "bukti": [
                                    "SK Tim Kerja Pembangunan ZI menuju WBK/WBBM Tahun 2025",
                                    "SK Tim Reformasi Birokrasi BPS Kabupaten Kepulauan Selayar Tahun 2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_1a_bps",
                                "drive_folder": "1 a. UNIT KERJA TELAH MEMBENTUK TIM"
                            },
                            {
                                "code": "1.b",
                                "question": "Penentuan anggota Tim dipilih melalui prosedur/mekanisme yang jelas",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Jika dengan prosedur/mekanisme yang jelas dan mewakili seluruh unsur dalam unit kerja\n• b. Jika sebagian menggunakan prosedur yang mewakili sebagian besar unsur\n• c. Jika tidak di seleksi",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Penentuan anggota tim pembangunan ZI di BPS Kabupaten Kepulauan Selayar telah dipilih melalui prosedur yang jelas dan telah mewakili seluruh unsur dalam unit kerja.",
                                "catatan": "",
                                "bukti": [
                                    "Notulen / laporan pelaksanaan rapat pembentukan Tim Kerja ZI",
                                    "Mekanisme / SOP tata cara pemilihan anggota Tim",
                                    "Kertas kerja penentuan dan seleksi anggota Tim Kerja ZI"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_1b_bps",
                                "drive_folder": "1 b. PENENTUAN ANGGOTA TIM"
                            }
                        ]
                    },
                    {
                        "name": "ii. Rencana Pembangunan ZI",
                        "score": "1.00 / 1.00 (100%)",
                        "items": [
                            {
                                "code": "2.a",
                                "question": "Terdapat dokumen rencana kerja pembangunan ZI menuju WBK/WBBM",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Terdapat dokumen rencana kerja pembangunan ZI yang disusun bersama dan ditetapkan pimpinan.\n• Tidak: Tidak terdapat dokumen rencana kerja.",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "BPS Kabupaten Kepulauan Selayar telah melakukan rapat rencana kerja pembangunan ZI dan menghasilkan output berupa dokumen rencana kerja dan target prioritas.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Matriks Rencana Kerja Pembangunan ZI 2025",
                                    "Undangan, Daftar Hadir, dan Notulen Rapat Penyusunan Rencana Kerja"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_2a_bps",
                                "drive_folder": "2 a. DOKUMEN RENCANA KERJA"
                            },
                            {
                                "code": "2.b",
                                "question": "Dalam dokumen pembangunan terdapat target-target prioritas yang relevan",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Terdapat target prioritas yang sangat relevan dengan tujuan WBK/WBBM\n• b. Terdapat target prioritas namun kurang relevan\n• c. Tidak ada penetapan target prioritas",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Dokumen rencana kerja telah memuat sasaran strategis dan target prioritas per area perubahan.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Rencana Kerja yang memuat target prioritas & Matriks Rencana Kerja",
                                    "Perjanjian Kinerja (PK) BPS Kabupaten Kepulauan Selayar Tahun 2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_2b_bps",
                                "drive_folder": "2 b. TARGET PRIORITAS"
                            },
                            {
                                "code": "2.c",
                                "question": "Terdapat mekanisme atau media untuk mensosialisasikan pembangunan WBK/WBBM",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Tersedia berbagai media sosialisasi baik luring maupun daring secara intensif\n• b. Media sosialisasi terbatas pada satu kanal\n• c. Belum ada sosialisasi",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Sosialisasi pembangunan ZI telah dilakukan secara komprehensif melalui website, banner, media sosial, dan apel rutin.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan pelaksanaan sosialisasi mencakup sosialisasi offline (rapat, apel, briefing) dan online (medsos, website)",
                                    "Foto/tangkapan layar publikasi ZI di medsos & website BPS Selayar",
                                    "Banner/Spanduk komitmen ZI di kantor PST"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_2c_bps",
                                "drive_folder": "2 c. SOSIALISASI PEMBANGUNAN ZI"
                            }
                        ]
                    },
                    {
                        "name": "iii. Pemantauan dan Evaluasi",
                        "score": "0.67 / 1.00 (66.67%)",
                        "items": [
                            {
                                "code": "3.a",
                                "question": "Seluruh kegiatan pembangunan sudah dilaksanakan sesuai dengan rencana",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Seluruh kegiatan terlaksana 100% sesuai jadwal\n• B: Terlaksana 75%-99%\n• C: Terlaksana 50%-74%\n• D: Kurang dari 50%",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Realisasi kegiatan pembangunan ZI dipantau dan dilaporkan secara berkala.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Pelaksanaan Pembangunan ZI",
                                    "Matriks Realisasi Pembangunan ZI",
                                    "Laporan Monitoring Capaian Bukti Dukung ZI"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_3a_bps",
                                "drive_folder": "3 a. PELAKSANAAN SESUAI RENCANA"
                            },
                            {
                                "code": "3.b",
                                "question": "Terdapat monitoring dan evaluasi terhadap pembangunan Zona Integritas",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Monev berkala setiap bulan\n• B: Monev setiap triwulan\n• C: Monev setiap semester\n• D: Belum dilaksanakan monev berkala",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Belum ada laporan monev ZI triwulanan yang tersusun rapi beserta kelengkapan risalah rapat.",
                                "catatan": "PERHATIAN: Segera laksanakan dan susun dokumen Monev Triwulanan I, II, dan III tahun 2025.",
                                "bukti": [
                                    "Dokumen Laporan Monev ZI Triwulanan (TW I, TW II, TW III)",
                                    "Undangan, Daftar Hadir, dan Notulen Rapat Monev ZI",
                                    "Dokumentasi foto rapat monev"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_3b_bps",
                                "drive_folder": "3 b. MONITORING DAN EVALUASI ZI"
                            },
                            {
                                "code": "3.c",
                                "question": "Hasil Monitoring dan Evaluasi telah ditindaklanjuti",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Seluruh rekomendasi monev telah ditindaklanjuti 100%\n• B: Ditindaklanjuti 75%-99%\n• C: Ditindaklanjuti <75%\n• D: Belum ditindaklanjuti",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Rekomendasi dari hasil evaluasi telah ditindaklanjuti oleh masing-masing koordinator area.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Tindak Lanjut Evaluasi Hasil Monev ZI Triwulanan",
                                    "Matriks monitoring status tindak lanjut temuan"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_3c_bps",
                                "drive_folder": "3 c. TINDAK LANJUT MONEV"
                            }
                        ]
                    },
                    {
                        "name": "iv. Perubahan Pola Pikir dan Budaya Kerja",
                        "score": "0.38 / 1.50 (25.00%)",
                        "items": [
                            {
                                "code": "4.a",
                                "question": "Pimpinan berperan sebagai role model dalam pembangunan Zona Integritas",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Pimpinan menjadi teladan nyata (presensi, kepatuhan LHKPN, komitmen BerAKHLAK, keteladanan kerja).\n• Tidak: Bukti peran role model belum terangkum dalam laporan.",
                                "jawaban": "Tidak",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Bukti dukung keteladanan pimpinan belum dihimpun ke dalam satu laporan role model komprehensif.",
                                "catatan": "PERHATIAN: Kumpulkan rekap presensi Kepala BPS, dokumen CKP, rekap LHKPN, dan dokumentasi keterlibatan langsung pimpinan pada apel dan kegiatan ZI.",
                                "bukti": [
                                    "Rekap Presensi Pimpinan (Ketepatan waktu kehadiran)",
                                    "Capaian Kinerja Pegawai (CKP) Pimpinan",
                                    "Dokumentasi Kegiatan Keteladanan Pimpinan (Apel, pembinaan, kunjungan lapangan)",
                                    "Tanda Terima LHKPN / LHKASN Pimpinan",
                                    "Laporan Penerapan Core Values BerAKHLAK oleh Pimpinan"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_4a_bps",
                                "drive_folder": "4 a. PIMPINAN SEBAGAI ROLE MODEL"
                            },
                            {
                                "code": "4.b",
                                "question": "Sudah ditetapkan agen perubahan (Change Agent)",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Agen perubahan telah ditetapkan melalui mekanisme seleksi dan memiliki program kerja nyata\n• b. Ditetapkan tanpa seleksi atau tanpa program kerja\n• c. Belum ditetapkan agen perubahan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "partial",
                                "badge": "Catatan: Kurang Laporan",
                                "narasi": "Telah ditetapkan 1 orang Change Ambassador (CA) di BPS Kabupaten Kepulauan Selayar.",
                                "catatan": "CATATAN KHUSUS: SK dan seleksi sudah ada, namun 'kurang laporan pelaksanaan kegiatan agen perubahan'. Harus segera diunggah laporannya.",
                                "bukti": [
                                    "SK Penetapan Agen Perubahan (Change Ambassador) Tahun 2025",
                                    "Dokumen Rapat & Kertas Kerja Penentuan/Pemilihan Agen Perubahan",
                                    "Laporan Kegiatan dan Proyek Perubahan Change Ambassador"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_4b_bps",
                                "drive_folder": "4 b. PENETAPAN AGEN PERUBAHAN"
                            },
                            {
                                "code": "4.c",
                                "question": "Telah dibangun budaya kerja dan pola pikir di lingkungan organisasi",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Telah dilaksanakan pembudayaan nilai-nilai BerAKHLAK secara terstruktur dan terukur dampaknya\n• b. Pembudayaan dilakukan insidental\n• c. Belum dibangun budaya kerja secara sistematis",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Dokumentasi dan laporan terstruktur pembudayaan budaya kerja (BerAKHLAK) masih minim pembuktian formal.",
                                "catatan": "PERHATIAN: Susun rangkuman kegiatan internalisasi BerAKHLAK, pelaksanaan apel Senin, kultum/briefing, dan evaluasi perubahan perilaku pegawai.",
                                "bukti": [
                                    "Rangkuman Kegiatan Perubahan Budaya Kerja dan Pola Pikir",
                                    "Dokumentasi Rutin Apel Pagi / Briefing dan amanat BerAKHLAK",
                                    "Laporan Dampak Perubahan Budaya Kerja Pegawai"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_4c_bps",
                                "drive_folder": "4 c. PEMBANGUNAN BUDAYA KERJA"
                            },
                            {
                                "code": "4.d",
                                "question": "Anggota organisasi terlibat dalam pembangunan Zona Integritas",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Seluruh pegawai (100%) terlibat aktif dalam seluruh tahapan pembangunan ZI\n• B: Sebagian besar pegawai (>75%) terlibat\n• C: Hanya anggota tim kerja yang terlibat (50%-75%)\n• D: Kurang dari 50% anggota terlibat",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Bukti pelibatan seluruh aparatur (termasuk PPNPN/staf) belum diorganisir dengan rapi dalam berkas.",
                                "catatan": "PERHATIAN: Buat pakta integritas ditandatangani 100% pegawai, dokumentasi banner komitmen bersama bertandatangan, dan daftar hadir rapat seluruh pegawai.",
                                "bukti": [
                                    "Dokumentasi Keterlibatan Pegawai pada Rapat Monev ZI",
                                    "Bukti Keterlibatan Anggota dalam Pengumpulan Bukti Dukung ZI",
                                    "Pakta Integritas yang ditandatangani SELURUH pegawai",
                                    "Foto dan Banner Dukungan Pembangunan ZI dengan tanda tangan seluruh aparatur"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_4d_bps",
                                "drive_folder": "4 d. KETERLIBATAN ANGGOTA ORGANISASI"
                            }
                        ]
                    }
                ]
            },
            "reform": {
                "score": "4.00",
                "max": "4.00",
                "pct": "100.00%",
                "status": "success",
                "groups": [
                    {
                        "name": "Reform i. Komitmen dalam Perubahan",
                        "score": "2.00 / 2.00 (100%)",
                        "items": [
                            {
                                "code": "R.1.a",
                                "question": "Agen perubahan telah membuat perubahan yang konkret di Instansi (persentase perubahan)",
                                "tipe": "% (Persentase)",
                                "kriteria": "Dihitung dari rasio inovasi/perubahan terhadap jumlah agen perubahan (target minimal 1 perubahan per agen).",
                                "jawaban": "300% (1 Agen : 3 Perubahan)",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Sempurna (300%)",
                                "narasi": "BPS Kabupaten Kepulauan Selayar telah menetapkan SK Agen Perubahan. Jumlah Agen Perubahan sebanyak 1 orang terdiri dari 1 orang Change Ambassador (CA). Terdapat 1 program perubahan utama dengan 3 turunan implementasi nyata yang telah dibuat.",
                                "catatan": "",
                                "bukti": [
                                    "SK Agen Perubahan BPS Kabupaten Kepulauan Selayar Tahun 2025",
                                    "Laporan Manajemen Perubahan dan Proyek Inovasi Tahun 2025",
                                    "Dokumentasi hasil implementasi perubahan di lingkungan kerja"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_Reform1a_bps",
                                "drive_folder": "R1 a. PERUBAHAN OLEH AGEN PERUBAHAN"
                            },
                            {
                                "code": "R.1.b",
                                "question": "Perubahan yang dibuat Agen Perubahan telah terintegrasi dalam sistem manajemen",
                                "tipe": "% (Persentase)",
                                "kriteria": "Persentase inovasi agen perubahan yang diadopsi dan dilembagakan dalam SOP atau sistem kerja kantor.",
                                "jawaban": "100%",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Sempurna (100%)",
                                "narasi": "Seluruh program perubahan yang dibuat telah diintegrasikan dalam sistem manajemen dan alur kerja harian BPS Kabupaten Kepulauan Selayar.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan manajemen perubahan yang memuat dokumentasi dan narasi pelaksanaan proyek perubahan",
                                    "SOP / Surat Edaran / Instruksi Pimpinan terkait penerapan inovasi ke dalam sistem manajemen kantor"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_Reform1b_bps",
                                "drive_folder": "R1 b. INTEGRASI PERUBAHAN"
                            }
                        ]
                    },
                    {
                        "name": "Reform ii. Komitmen Pimpinan",
                        "score": "1.00 / 1.00 (100%)",
                        "items": [
                            {
                                "code": "R.2",
                                "question": "Pimpinan memiliki komitmen terhadap pelaksanaan reformasi birokrasi",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Pimpinan memimpin langsung dan mengawal roadmap reformasi birokrasi serta mengalokasikan anggaran & SDM penuh\n• B: Keterlibatan pimpinan tinggi namun anggaran terbatas\n• C/D/E: Keterlibatan pimpinan rendah",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Kepala BPS Kabupaten Kepulauan Selayar memimpin secara proaktif rapat pembentukan tim, penetapan rencana kerja, penandatanganan komitmen, serta monev berkala.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen rencana kerja pembangunan ZI di BPS Kabupaten Kepulauan Selayar yang ditandatangani Kepala BPS",
                                    "Dokumentasi arahan pimpinan dalam setiap forum pembinaan dan monev",
                                    "DIPA / POK alokasi anggaran operasional pembangunan ZI"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_Reform2_bps",
                                "drive_folder": "R2. KOMITMEN PIMPINAN"
                            }
                        ]
                    },
                    {
                        "name": "Reform iii. Membangun Budaya Kerja",
                        "score": "1.00 / 1.00 (100%)",
                        "items": [
                            {
                                "code": "R.3",
                                "question": "Instansi membangun budaya kerja positif dan menginternalisasikan nilai-nilai organisasi",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Penerapan budaya kerja terstruktur, terdapat internalisasi rutin, dan dikaitkan dalam SOP kerja\n• B: Internalisasi berkala tapi belum terikat SOP\n• C/D: Belum terstruktur",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Nilai-nilai Core Values ASN BerAKHLAK telah diinternalisasikan ke dalam seluruh SOP operasional pelayanan dan administrasi.",
                                "catatan": "",
                                "bukti": [
                                    "Undangan, daftar hadir, notulen dan dokumentasi kegiatan internalisasi budaya kerja BerAKHLAK",
                                    "SOP kegiatan pelayanan dan teknis yang telah terdapat narasi keterkaitan dengan budaya kerja BerAKHLAK"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenPerubahan_Reform3_bps",
                                "drive_folder": "R3. MEMBANGUN BUDAYA KERJA"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": "area2",
            "number": 2,
            "title": "Penataan Tatalaksana",
            "icon": "⚙️",
            "desc": "Bertujuan untuk meningkatkan efisiensi dan efektivitas sistem, proses, dan prosedur kerja yang jelas, efektif, efisien, dan terukur pada BPS Kabupaten Kepulauan Selayar.",
            "pemenuhan": {
                "score": "3.38",
                "max": "3.50",
                "pct": "96.43%",
                "status": "success",
                "groups": [
                    {
                        "name": "i. Prosedur Operasional Tetap (SOP) Kegiatan Utama",
                        "score": "1.00 / 1.00 (100%)",
                        "items": [
                            {
                                "code": "1.a",
                                "question": "SOP mengacu pada peta proses bisnis instansi",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Seluruh SOP kegiatan utama mengacu 100% pada peta proses bisnis BPS\n• B: Sebagian besar (75-99%)\n• C: Sebagian (50-74%)\n• D: Kurang dari 50%",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Seluruh SOP administrasi dan teknis disusun merujuk pada Peta Proses Bisnis BPS RI.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Proses Bisnis BPS",
                                    "Dokumen SOP Teknis dan Administrasi BPS Kabupaten Kepulauan Selayar",
                                    "Dokumen SOP Kegiatan Inovasi Layanan"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_1a_bps",
                                "drive_folder": "1 a. SOP MENGACU PETA PROSES BISNIS"
                            },
                            {
                                "code": "1.b",
                                "question": "Prosedur operasional tetap (SOP) telah diterapkan",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Seluruh SOP telah diterapkan secara konsisten disertai evaluasi berkala\n• B: Sebagian besar diterapkan\n• C/D/E: Sebagian kecil atau belum diterapkan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "SOP diterapkan secara menyeluruh di unit pelayanan statistik terpadu (PST) maupun administrasi persuratan.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Kegiatan Teknis/Administrasi",
                                    "Memorandum SOP & Matriks SOP",
                                    "Dokumentasi Sosialisasi dan Internalisasi SOP kepada seluruh pegawai",
                                    "Laporan Inovasi pada SOP"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_1b_bps",
                                "drive_folder": "1 b. PENERAPAN SOP"
                            },
                            {
                                "code": "1.c",
                                "question": "Prosedur operasional tetap (SOP) telah dievaluasi",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Dilakukan reviu dan evaluasi terhadap seluruh SOP secara berkala\n• B: Dilakukan evaluasi sebagian\n• C/D/E: Belum dievaluasi",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Telah dilakukan rapat evaluasi SOP secara berkala untuk menyesuaikan dengan regulasi terbaru.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Undangan, Notulen, dan Daftar Hadir Rapat Evaluasi SOP",
                                    "Dokumen SOP Hasil Perbaikan / Reviu Terkini"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_1c_bps",
                                "drive_folder": "1 c. EVALUASI SOP"
                            }
                        ]
                    },
                    {
                        "name": "ii. Sistem Pemerintahan Berbasis Elektronik (SPBE)",
                        "score": "2.00 / 2.00 (100%)",
                        "items": [
                            {
                                "code": "2.a",
                                "question": "Sistem pengukuran kinerja unit sudah menggunakan teknologi informasi",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Menggunakan sistem informasi kinerja terintegrasi penuh (KipApp, SiMonev)\n• b. Menggunakan TI parsial\n• c. Manual",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Pengukuran capaian kinerja satker memanfaatkan aplikasi KipApp, SiMonev Bappenas, dan SMART DJA.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Pemanfaatan Aplikasi Pengukuran Kinerja (KipApp & SiMonev)",
                                    "Kompilasi Aplikasi dan Daftar Penerapan TI",
                                    "Tangkapan Layar Dashboard Pengukuran Kinerja",
                                    "Laporan Pemanfaatan Aplikasi Inovasi"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_2a_bps",
                                "drive_folder": "2 a. TI PENGUKURAN KINERJA"
                            },
                            {
                                "code": "2.b",
                                "question": "Operasionalisasi manajemen SDM sudah menggunakan TI",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Penuh menggunakan sistem informasi kepegawaian (SIMPEG BPS, SIASN BKN)\n• b. Parsial\n• c. Belum menggunakan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Seluruh urusan presensi, cuti, SKP, data riwayat pegawai dikelola melalui SIMPEG dan Portal SDM BPS.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Pemanfaatan Aplikasi SIMPEG Online dan Portal SDM",
                                    "Kompilasi Aplikasi Kepegawaian dan Daftar Penerapan TI",
                                    "Tangkapan Layar Fitur SIMPEG (Presensi Online, Cuti, Profil Pegawai)"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_2b_bps",
                                "drive_folder": "2 b. TI MANAJEMEN SDM"
                            },
                            {
                                "code": "2.c",
                                "question": "Pemberian pelayanan kepada publik sudah menggunakan teknologi informasi",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Layanan publik telah terdigitalisasi penuh dengan inovasi layanan pendukung\n• b. Sebagian layanan menggunakan TI\n• c. Manual",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Unit kerja telah memberikan pelayanan publik dengan menggunakan teknologi informasi terpusat (website selayarkab.bps.go.id, PST Online, PPID, Allstat) serta terdapat inovasi lokal (SIMPLE, POLASSI, SIAP, dll.).",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Pemanfaatan Website BPS Kepulauan Selayar dan PST Online",
                                    "Kompilasi Aplikasi Layanan Publik Eksternal",
                                    "Tangkapan Layar Aplikasi Layanan Publik dan Inovasi (SIMPLE, POLASSI, SIAP)"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_2c_bps",
                                "drive_folder": "2 c. TI PELAYANAN PUBLIK"
                            },
                            {
                                "code": "2.d",
                                "question": "Telah dilakukan monitoring dan evaluasi terhadap pemanfaatan teknologi informasi",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Dilakukan monev berkala dan ditindaklanjuti secara terdokumentasi\n• b. Monev tanpa tindak lanjut\n• c. Belum ada monev",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "partial",
                                "badge": "Catatan: Kurang Risalah",
                                "narasi": "Laporan monev TI telah dibuat, namun berkas rapat monev perlu dilengkapi.",
                                "catatan": "CATATAN KHUSUS: Belum tersedia undangan, notulen, dan daftar hadir rapat monev pemanfaatan TI. Lengkapi berkas rapat!",
                                "bukti": [
                                    "Laporan Bukti Tindak Lanjut atas Laporan Monev Perkembangan TI",
                                    "Laporan Aplikasi Monev & Pemeliharaan Sarana TI",
                                    "Undangan, Daftar Hadir, dan Notulen Rapat Monev TI (Perlu Dilengkapi)"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_2d_bps",
                                "drive_folder": "2 d. MONEV PEMANFAATAN TI"
                            }
                        ]
                    },
                    {
                        "name": "iii. Keterbukaan Informasi Publik",
                        "score": "0.38 / 0.50 (75.00%)",
                        "items": [
                            {
                                "code": "3.a",
                                "question": "Kebijakan tentang keterbukaan informasi publik telah diterapkan",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Telah ditetapkan regulasi/SK PPID dan informasi publik diumumkan secara berkala\n• b. Regulasi ada tapi implementasi minim\n• c. Belum diterapkan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Sudah terdapat SK PPID dan penetapan Daftar Informasi Publik (DIP) yang dapat diakses publik.",
                                "catatan": "",
                                "bukti": [
                                    "SK PPID BPS Kabupaten Kepulauan Selayar",
                                    "Daftar Informasi Publik (DIP) yang dapat diakses masyarakat di website & PST"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_3a_bps",
                                "drive_folder": "3 a. KEBIJAKAN KIP"
                            },
                            {
                                "code": "3.b",
                                "question": "Telah dilakukan monitoring dan evaluasi pelaksanaan kebijakan keterbukaan informasi publik",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Monev semesteran/tahunan teratur dan dipublikasikan\n• b. Monev dilakukan namun belum rutin / dokumen belum lengkap\n• c. Belum dilakukan monev",
                                "jawaban": "B",
                                "nilai": "0.50",
                                "status": "partial",
                                "badge": "Perlu Ditingkatkan",
                                "narasi": "Monev keterbukaan informasi publik masih dalam bentuk rekap parsial, belum menjadi Laporan Tahunan Layanan Informasi PPID komprehensif.",
                                "catatan": "PERHATIAN: Susun Laporan Tahunan Layanan Informasi Publik PPID BPS Kabupaten Kepulauan Selayar untuk mendapatkan nilai maksimal 1.00.",
                                "bukti": [
                                    "Daftar informasi publik yang dapat diakses berkala",
                                    "Laporan Keterbukaan Informasi Publik / Laporan Tahunan Layanan PPID"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_3b_bps",
                                "drive_folder": "3 b. MONEV KIP"
                            }
                        ]
                    }
                ]
            },
            "reform": {
                "score": "3.50",
                "max": "3.50",
                "pct": "100.00%",
                "status": "success",
                "groups": [
                    {
                        "name": "Reform i. Peta Proses Bisnis",
                        "score": "0.50 / 0.50 (100%)",
                        "items": [
                            {
                                "code": "R.1",
                                "question": "Telah disusun peta proses bisnis dengan adanya penyederhanaan jabatan",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Peta proses bisnis telah disesuaikan pasca penyederhanaan birokrasi dan jabatan fungsional\n• B/C/D: Belum disesuaikan sepenuhnya",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Peta proses bisnis telah diselaraskan dengan tata kerja fungsional berbasis tim kerja.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Proses Bisnis BPS pasca penyederhanaan birokrasi",
                                    "Peraturan BPS Nomor 7 Tahun 2020 & Peraturan BPS Nomor 5 Tahun 2023",
                                    "SE Menteri PANRB Nomor 393 Tahun 2019"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_Reform1a_bps",
                                "drive_folder": "R1. PETA PROSES BISNIS PENYEDERHANAAN"
                            }
                        ]
                    },
                    {
                        "name": "Reform ii. SPBE yang Terintegrasi",
                        "score": "1.00 / 1.00 (100%)",
                        "items": [
                            {
                                "code": "R.2.a",
                                "question": "Implementasi SPBE telah terintegrasi dan mampu mendorong pelaksanaan pelayanan publik",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Sistem pelayanan publik terhubung secara elektronik dan terintegrasi\n• b. Parsial\n• c. Belum terintegrasi",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Layanan publik eksternal memanfaatkan sistem terpadu portal BPS dan integrasi data.",
                                "catatan": "",
                                "bukti": [
                                    "Deskripsi Daftar SPBE Eksternal",
                                    "Daftar Layanan Pada Pelayanan Publik yang mengimplementasikan SPBE Eksternal"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_Reform2a_bps",
                                "drive_folder": "R2 a. SPBE PELAYANAN PUBLIK"
                            },
                            {
                                "code": "R.2.b",
                                "question": "Implementasi SPBE telah terintegrasi dan mampu mendorong pelayanan internal",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Sistem administrasi internal terhubung (BOS, KipApp, SIMPEG, Srikandi)\n• b. Parsial\n• c. Belum terintegrasi",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Sistem persuratan, tata usaha, dan anggaran telah saling terhubung secara elektronik.",
                                "catatan": "",
                                "bukti": [
                                    "Deskripsi Daftar SPBE Internal BPS",
                                    "Daftar Layanan Administrasi Internal yang mengimplementasikan SPBE Internal"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_Reform2b_bps",
                                "drive_folder": "R2 b. SPBE INTERNAL"
                            }
                        ]
                    },
                    {
                        "name": "Reform iii. Transformasi Digital",
                        "score": "2.00 / 2.00 (100%)",
                        "items": [
                            {
                                "code": "R.3.a",
                                "question": "Transformasi digital pada bidang proses bisnis utama (pengumpulan & pengolahan data)",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Transformasi total dari konvensional (PAPI) menjadi digital (CAPI, CAWI, Fasih)\n• B/C/D/E: Sebagian kecil atau belum",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Pendataan survei dan sensus telah bertransformasi dari PAPI ke CAPI menggunakan aplikasi FASIH dan CAPI BPS.",
                                "catatan": "",
                                "bukti": [
                                    "Narasi alasan perubahan metode PAPI menjadi CAPI",
                                    "Buku Pedoman Penggunaan CAPI / FASIH",
                                    "Surat Edaran BPS RI terkait Digitalisasi Survei",
                                    "Tangkapan layar pemanfaatan aplikasi CAPI di lapangan"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_Reform3a_bps",
                                "drive_folder": "R3 a. DIGITALISASI PROSES BISNIS"
                            },
                            {
                                "code": "R.3.b",
                                "question": "Transformasi digital pada bidang administrasi pemerintahan",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Administrasi tata laksana perkantoran 100% digital (BOS, KipApp, Srikandi)\n• B/C/D/E: Parsial",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Administrasi keuangan dan persuratan telah terdigitalisasi penuh dengan BOS dan KipApp.",
                                "catatan": "",
                                "bukti": [
                                    "Narasi pemanfaatan aplikasi BOS (Back Office System) dan KipApp",
                                    "Buku Pedoman & Juknis Aplikasi Administrasi",
                                    "Tangkapan layar penggunaan BOS dan KipApp dalam persetujuan dinas/keuangan"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_Reform3b_bps",
                                "drive_folder": "R3 b. DIGITALISASI ADMINISTRASI"
                            },
                            {
                                "code": "R.3.c",
                                "question": "Transformasi digital pada bidang pelayanan publik",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Layanan publik terdigitalisasi menyeluruh (Website, Silastik, Romantik, PPID, SIRUP)\n• B/C/D/E: Parsial",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Seluruh konsultasi statistik dan permohonan rekomendasi statistik telah terdigitalisasi melalui Silastik dan Romantik.",
                                "catatan": "",
                                "bukti": [
                                    "Narasi dan Panduan Penggunaan Website Selayar, Silastik, Romantik, dan PPID",
                                    "Tangkapan layar transaksi layanan publik online dan rekap pengguna layanan digital"
                                ],
                                "link_contoh": "http://s.bps.go.id/PenataanTatalaksana_Reform3c_bps",
                                "drive_folder": "R3 c. DIGITALISASI PELAYANAN PUBLIK"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": "area3",
            "number": 3,
            "title": "Penataan Sistem Manajemen SDM Aparatur",
            "icon": "👥",
            "desc": "Bertujuan untuk meningkatkan profesionalisme SDM aparatur pada BPS Kabupaten Kepulauan Selayar yang didukung oleh sistem rekrutmen, mutasi, penilaian kinerja, dan pengembangan kompetensi berbasis merit.",
            "pemenuhan": {
                "score": "3.96",
                "max": "5.00",
                "pct": "79.17%",
                "status": "warning",
                "groups": [
                    {
                        "name": "i. Perencanaan Kebutuhan Pegawai",
                        "score": "0.25 / 0.25 (100%)",
                        "items": [
                            {
                                "code": "1.a",
                                "question": "Kebutuhan pegawai mengacu kepada peta jabatan dan hasil analisis beban kerja (ABK)",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Disusun berdasarkan peta jabatan dan ABK resmi\n• Tidak: Tidak mengacu peta jabatan/ABK",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Penyusunan formasi kebutuhan pegawai di BPS Kabupaten Kepulauan Selayar mengacu pada peta jabatan dan ABK tahun berjalan.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Peta Jabatan BPS Kabupaten Kepulauan Selayar",
                                    "Dokumen Analisis Beban Kerja (ABK) Pegawai"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_1a_bps",
                                "drive_folder": "1 a. PERENCANAAN PEGAWAI DARI ABK"
                            },
                            {
                                "code": "1.b",
                                "question": "Penempatan pegawai hasil rekrutmen murni mengacu kepada kebutuhan riil",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: 100% penempatan sesuai formasi kebutuhan riil\n• B: 75-99%\n• C: 50-74%\n• D: <50%",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Penempatan CPNS dan PPPK tepat sasaran pada unit kerja yang kekurangan beban kerja.",
                                "catatan": "",
                                "bukti": [
                                    "Surat Usulan Kebutuhan Pegawai / CPNS / PPPK",
                                    "SK Penempatan Pegawai Baru Sesuai Formasi"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_1b_bps",
                                "drive_folder": "1 b. PENEMPATAN REKRUTMEN"
                            },
                            {
                                "code": "1.c",
                                "question": "Telah dilakukan monitoring dan evaluasi terhadap penempatan pegawai",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Dilakukan monev kesesuaian penempatan berkala\n• Tidak: Belum dimonev",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Monev penempatan dilakukan secara berkala tiap semester.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Monitoring dan Evaluasi Penempatan Pegawai BPS Selayar"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_1c_bps",
                                "drive_folder": "1 c. MONEV PENEMPATAN PEGAWAI"
                            }
                        ]
                    },
                    {
                        "name": "ii. Pola Mutasi Internal",
                        "score": "0.50 / 0.50 (100%)",
                        "items": [
                            {
                                "code": "2.a",
                                "question": "Telah dilakukan mutasi pegawai antar jabatan",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Dilakukan rotasi/mutasi internal secara terencana\n• Tidak: Tidak ada mutasi internal",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Mutasi dan rotasi internal dilaksanakan guna penyegaran dan penguatan tim kerja.",
                                "catatan": "",
                                "bukti": [
                                    "Notulen Rapat Tim Mutasi dan Rotasi Pegawai",
                                    "SK Kepala BPS tentang Mutasi / Rotasi Internal Pegawai"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_2a_bps",
                                "drive_folder": "2 a. MUTASI INTERNAL PEGAWAI"
                            },
                            {
                                "code": "2.b",
                                "question": "Mutasi pegawai telah memperhatikan kompetensi jabatan",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: 100% mutasi memperhatikan standar kompetensi jabatan\n• B/C/D/E: Sebagian atau tidak mempertimbangkan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Penetapan mutasi didasarkan pada analisis kesesuaian profil dan kualifikasi pegawai.",
                                "catatan": "",
                                "bukti": [
                                    "Notulen Rapat Mutasi Rotasi Pegawai",
                                    "SK Mutasi Rotasi Pegawai",
                                    "Dokumen Analisis Kesesuaian Kompetensi Jabatan Pegawai"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_2b_bps",
                                "drive_folder": "2 b. MUTASI BERBASIS KOMPETENSI"
                            },
                            {
                                "code": "2.c",
                                "question": "Telah dilakukan monitoring dan evaluasi terhadap kegiatan mutasi",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Dampak mutasi terhadap kinerja pegawai dievaluasi\n• Tidak: Belum dievaluasi",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Monev mutasi menunjukkan peningkatan produktivitas tim kerja.",
                                "catatan": "",
                                "bukti": [
                                    "Rekapitulasi Mutasi Rotasi Pegawai 2025",
                                    "Analisis Kesesuaian Kompetensi Jabatan Pegawai",
                                    "Laporan Monev Mutasi Pegawai 2025",
                                    "Rekap Nilai SKP Bulanan Pegawai Pasca Mutasi 2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_2c_bps",
                                "drive_folder": "2 c. MONEV MUTASI INTERNAL"
                            }
                        ]
                    },
                    {
                        "name": "iii. Pengembangan Pegawai Berbasis Kompetensi",
                        "score": "0.21 / 1.25 (16.67%)",
                        "items": [
                            {
                                "code": "3.a",
                                "question": "Unit Kerja melakukan Training Need Analysis (TNA)",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Melakukan analisis kebutuhan diklat/pelatihan\n• Tidak: Tidak melakukan TNA",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Telah dilakukan survei pemetaan kebutuhan pelatihan pegawai.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Laporan Training Need Analysis (TNA) BPS Kabupaten Kepulauan Selayar"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_3a_bps",
                                "drive_folder": "3 a. TRAINING NEED ANALYSIS"
                            },
                            {
                                "code": "3.b",
                                "question": "Rencana pengembangan kompetensi pegawai telah mempertimbangkan hasil pengelolaan kinerja",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: 100% rencana diklat mengacu pada hasil gap kinerja SKP\n• B/C: Sebagian\n• D: Belum mempertimbangkan hasil kinerja",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Hasil evaluasi kinerja individu belum tersinkronisasi secara formal dengan rencana pengembangan kompetensi.",
                                "catatan": "PERHATIAN: Susun Laporan Analisis Kesenjangan Pegawai yang mengaitkan hasil SKP tahun lalu dengan rencana diklat.",
                                "bukti": [
                                    "Laporan Analisis Kesenjangan Pegawai BPS Kab. Kepulauan Selayar Berdasarkan Hasil Pengelolaan Kinerja SKP"
                                ],
                                "link_contoh": "http://s.bps.go.id/PilarManajemenSDM_3b_bps",
                                "drive_folder": "3 b. RENCANA DIKLAT BERBASIS KINERJA"
                            },
                            {
                                "code": "3.c",
                                "question": "Tingkat kesenjangan kompetensi pegawai telah dipetakan",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Kesenjangan kompetensi terpetakan 100%\n• B/C: Sebagian\n• D: Belum terpetakan",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Matriks pemetaan gap kompetensi per individu pegawai belum lengkap.",
                                "catatan": "PERHATIAN: Kumpulkan dan susun dokumen pemetaan kesenjangan kompetensi seluruh pegawai.",
                                "bukti": [
                                    "Laporan Training Need Analysis (TNA)",
                                    "Matriks dan Laporan Analisis Kesenjangan Kompetensi Pegawai"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_3c_bps",
                                "drive_folder": "3 c. PEMETAAN GAP KOMPETENSI"
                            },
                            {
                                "code": "3.d",
                                "question": "Pegawai telah memperoleh kesempatan mengikuti diklat/pengembangan kompetensi",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Seluruh pegawai memperoleh kesempatan minimal 20 JP per tahun\n• B: >75%\n• C: 50-74%\n• D: <50%",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Bukti surat tugas diklat, bimtek, dan izin belajar belum terhimpun secara lengkap.",
                                "catatan": "PERHATIAN: Himpun seluruh surat tugas diklat teknis/fungsional, MOOC Pusdiklat, dan izin belajar tahun 2024-2025.",
                                "bukti": [
                                    "Undangan diklat, pelatihan, bimtek pegawai tahun 2024-2025",
                                    "Pengajuan Diklat dan Izin Belajar Pegawai",
                                    "Rekapitulasi jam pelajaran (JP) pengembangan kompetensi pegawai"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_3d_bps",
                                "drive_folder": "3 d. KESEMPATAN DIKLAT PEGAWAI"
                            },
                            {
                                "code": "3.e",
                                "question": "Unit kerja melakukan upaya pengembangan kompetensi internal (knowledge sharing/coaching)",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Rutin mengadakan sharing session / bimtek mandiri setiap bulan\n• B/C: Insidental\n• D: Belum ada upaya mandiri",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Dokumentasi kegiatan internalisasi mandiri (Gugus Kendali Mutu / Knowledge Sharing) belum terdokumentasi rapi.",
                                "catatan": "PERHATIAN: Laksanakan dan dokumentasikan minimal 3 kali Knowledge Sharing internal beserta laporan, undangan, materi, dan sertifikat.",
                                "bukti": [
                                    "Laporan Kegiatan dan Undangan Pelatihan Internal / Knowledge Sharing",
                                    "Sertifikat Pelatihan dan Bimtek Pegawai Tahun 2024-2025",
                                    "Dokumentasi Foto dan Materi Paparan Knowledge Sharing"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_3e_bps",
                                "drive_folder": "3 e. PENGEMBANGAN KOMPETENSI MANDIRI"
                            },
                            {
                                "code": "3.f",
                                "question": "Telah dilakukan monitoring dan evaluasi terhadap hasil pengembangan kompetensi",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Monev dampak diklat terhadap kinerja dilaksanakan berkala\n• b. Parsial\n• c. Belum dimonev",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Belum ada laporan evaluasi pasca-diklat mengenai peningkatan kinerja pegawai setelah mengikuti pelatihan.",
                                "catatan": "PERHATIAN: Buat Laporan Monev Hasil Pengembangan Kompetensi yang mengevaluasi peningkatan performa kerja pegawai pasca-diklat.",
                                "bukti": [
                                    "Daftar Rekapitulasi Diklat Kompetensi Pegawai 2024-2025",
                                    "Laporan Monev Hasil Pengembangan Kompetensi Pegawai 2024-2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_3f_bps",
                                "drive_folder": "3 f. MONEV HASIL PENGEMBANGAN"
                            }
                        ]
                    },
                    {
                        "name": "iv. Penetapan Kinerja Individu",
                        "score": "2.00 / 2.00 (100%)",
                        "items": [
                            {
                                "code": "4.a",
                                "question": "Terdapat penetapan kinerja individu yang terkait dengan perjanjian kinerja organisasi",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: 100% SKP pegawai terhubung (cascading) dengan PK pimpinan\n• B: 75-99%\n• C/D: <75%",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "SKP seluruh pegawai disusun melalui aplikasi KipApp dengan cascading langsung dari PK Kepala BPS.",
                                "catatan": "",
                                "bukti": [
                                    "SKP Seluruh Pegawai BPS Selayar dari KipApp",
                                    "Indikator Kinerja Individu (IKI) Seluruh Pegawai",
                                    "Matriks Cascading Indikator Kinerja Organisasi ke Individu"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_4a_bps",
                                "drive_folder": "4 a. PENETAPAN KINERJA INDIVIDU"
                            },
                            {
                                "code": "4.b",
                                "question": "Ukuran kinerja individu telah memiliki kesesuaian dengan IKI level diatasnya",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Seluruh IKI pegawai selaras dengan IKI pejabat atasan / koordinator tim\n• B/C/D: Sebagian atau belum selaras",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Penetapan IKI didukung oleh dokumen pohon kinerja yang menunjukkan direct linkage output kerja.",
                                "catatan": "",
                                "bukti": [
                                    "Analisis Sederhana Cascading IK 2025",
                                    "Dokumen Pohon Kinerja BPS Kabupaten Kepulauan Selayar 2025",
                                    "Rekap IKI Per Individu",
                                    "Dokumen LAKIN BPS Kabupaten Kepulauan Selayar"
                                ],
                                "link_contoh": "http://s.bps.go.id/PilarManajemenSDM_4b_BPS",
                                "drive_folder": "4 b. KESESUAIAN IKI BERJENJANG"
                            },
                            {
                                "code": "4.c",
                                "question": "Pengukuran kinerja individu dilakukan secara periodik",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Pengukuran kinerja dilakukan rutin setiap bulan melalui sistem online\n• B/C/D/E: Triwulanan / Tahunan / Manual",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Penilaian CKP dan SKP dilakukan secara bulanan di KipApp oleh pejabat penilai.",
                                "catatan": "",
                                "bukti": [
                                    "Rekapitulasi Nilai SKP Bulanan Pegawai Tahun 2025",
                                    "Alur Penilaian dan Verifikasi Kinerja pada KipApp"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_4c_bps",
                                "drive_folder": "4 c. PENGUKURAN KINERJA PERIODIK"
                            },
                            {
                                "code": "4.d",
                                "question": "Hasil penilaian kinerja individu telah dijadikan dasar untuk pemberian reward",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Terdapat skema penghargaan (Employee of the Month / Piagam) berbasis capaian kinerja terukur\n• Tidak: Belum ada pemberian reward",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Penghargaan Employee of the Month (EOM) diberikan secara berkala dengan kriteria penilaian objektif.",
                                "catatan": "",
                                "bukti": [
                                    "Rekapitulasi Nilai SKP Bulanan 2025",
                                    "Kriteria dan Rubrik Penilaian Employee Of The Month (EOM)",
                                    "SK Kepala BPS tentang Implementasi KipApp Penilaian EOM",
                                    "Kertas Kerja Pemilihan dan Piagam Penghargaan EOM 2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_4d_bps",
                                "drive_folder": "4 d. REWARD BERBASIS KINERJA"
                            }
                        ]
                    },
                    {
                        "name": "v. Penegakan Aturan Disiplin",
                        "score": "0.75 / 0.75 (100%)",
                        "items": [
                            {
                                "code": "5.a",
                                "question": "Aturan disiplin / kode etik / kode perilaku telah diimplementasikan",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Kode etik ASN dan aturan disiplin ditegakkan konsisten, SIMPEG & SPT terpantau 100%\n• B/C/D: Sebagian",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Penegakan PP 94/2021 dan kode etik BPS diterapkan tegas, seluruh aparatur patuh pelaporan SPT dan presensi.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Aturan Disiplin, Perka, Kepka, dan Perban Kode Etik Pegawai BPS",
                                    "Laporan Rekap Pelanggaran Disiplin Pegawai (Nihil / Tercatat)",
                                    "Bukti Update SIMPEG, Pemutakhiran SKP, dan Tanda Terima SPT Tahunan Seluruh Pegawai"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_5a_bps",
                                "drive_folder": "5 a. PENEGAKAN DISIPLIN"
                            }
                        ]
                    },
                    {
                        "name": "vi. Sistem Informasi Kepegawaian",
                        "score": "0.25 / 0.25 (100%)",
                        "items": [
                            {
                                "code": "6.a",
                                "question": "Data informasi kepegawaian unit kerja telah dimutakhirkan secara berkala",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Data SIMPEG terupdate real-time setiap terjadi perubahan data/kenaikan pangkat/berkala\n• b. Update tahunan\n• c. Tidak update",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Data SIMPEG dan berkas kepegawaian selalu dimutakhirkan oleh subbagian umum.",
                                "catatan": "",
                                "bukti": [
                                    "Bukti Pemutakhiran Data SIMPEG",
                                    "Pemutakhiran Dokumen SKP & SPT",
                                    "Laporan Keadaan Pegawai BPS Selayar Kondisi Januari & Desember 2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_6a_BPS",
                                "drive_folder": "6 a. SISTEM INFORMASI KEPEGAWAIAN"
                            }
                        ]
                    }
                ]
            },
            "reform": {
                "score": "3.50",
                "max": "5.00",
                "pct": "70.00%",
                "status": "warning",
                "groups": [
                    {
                        "name": "Reform i. Kinerja Individu",
                        "score": "0.75 / 1.50 (50.00%)",
                        "items": [
                            {
                                "code": "R.1",
                                "question": "Ukuran kinerja individu telah berorientasi hasil (outcome)",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Seluruh indikator kinerja individu (100%) berorientasi outcome\n• b. Sebagian berorientasi outcome dan sebagian output kegiatan (50-99%)\n• c. Masih sebatas orientasi aktivitas/input",
                                "jawaban": "B",
                                "nilai": "0.50",
                                "status": "partial",
                                "badge": "Perlu Ditingkatkan",
                                "narasi": "Sebagian besar indikator masih berfokus pada target penyelesaian output kegiatan, sedang didorong menuju orientasi outcome manfaat publik.",
                                "catatan": "PERHATIAN: Tingkatkan formulasi sasaran kinerja pegawai pada KipApp agar memuat outcome pemanfaatan data dan kualitas layanan.",
                                "bukti": [
                                    "Dokumen SKP Pegawai dengan indikator berorientasi hasil (outcome)",
                                    "Laporan Capaian Kinerja Individu berbasis pemanfaatan hasil survei"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_Reform1_bps",
                                "drive_folder": "R1. IKI BERORIENTASI OUTCOME"
                            }
                        ]
                    },
                    {
                        "name": "Reform ii. Assessment Pegawai",
                        "score": "0.75 / 1.50 (50.00%)",
                        "items": [
                            {
                                "code": "R.2",
                                "question": "Hasil assessment telah dijadikan pertimbangan untuk mutasi dan pengembangan karir",
                                "tipe": "A/B/C",
                                "kriteria": "• a. 100% mutasi dan pengembangan karir menggunakan hasil asesmen resmi (profil kompetensi BKN/BPS)\n• b. Dijadikan pertimbangan sebagian\n• c. Tidak dijadikan dasar",
                                "jawaban": "B",
                                "nilai": "0.50",
                                "status": "partial",
                                "badge": "Perlu Ditingkatkan",
                                "narasi": "Hasil asesmen kompetensi telah mulai dijadikan referensi penugasan ketua tim kerja fungsional.",
                                "catatan": "PERHATIAN: Lengkapi dengan dokumen resmi korelasi hasil asesmen kompetensi pegawai terhadap penetapan SK Tim Kerja.",
                                "bukti": [
                                    "Dokumen hasil asesmen kompetensi pegawai (Uji Kompetensi / Penilaian Potensi)",
                                    "Kertas kerja pertimbangan asesmen dalam penugasan jabatan fungsional dan mutasi internal"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_Reform2_bps",
                                "drive_folder": "R2. HASIL ASSESMENT PEGAWAI"
                            }
                        ]
                    },
                    {
                        "name": "Reform iii. Penurunan Pelanggaran Disiplin Pegawai",
                        "score": "2.00 / 2.00 (100%)",
                        "items": [
                            {
                                "code": "R.3",
                                "question": "Penurunan tingkat pelanggaran disiplin pegawai (persentase penurunan / kepatuhan penuh)",
                                "tipe": "% (Persentase)",
                                "kriteria": "Tingkat penurunan kasus hukuman disiplin. Jika satker telah mempertahankan 0 kasus pelanggaran disiplin secara konsisten, dinilai 100%.",
                                "jawaban": "100% (Kasus Tahun Lalu: 0, Tahun Ini: 0)",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Sempurna (100%)",
                                "narasi": "BPS Kabupaten Kepulauan Selayar mempertahankan zero tolerance terhadap pelanggaran disiplin, nihil laporan pelanggaran kode etik.",
                                "catatan": "",
                                "bukti": [
                                    "Daftar Rekapitulasi Laporan Pelanggaran Disiplin Pegawai Triwulan I s.d. IV (Surat Keterangan Bebas Pelanggaran)",
                                    "Surat Keterangan dari Tim Pembinaan Disiplin / Kepala BPS Selayar"
                                ],
                                "link_contoh": "http://s.bps.go.id/ManajemenSDM_Reform3_bps",
                                "drive_folder": "R3. PENURUNAN PELANGGARAN DISIPLIN"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": "area4",
            "number": 4,
            "title": "Penguatan Akuntabilitas",
            "icon": "📊",
            "desc": "Bertujuan untuk meningkatkan kapasitas dan akuntabilitas kinerja BPS Kabupaten Kepulauan Selayar, memastikan pimpinan terlibat aktif dalam pengelolaan kinerja organisasi yang berorientasi hasil.",
            "pemenuhan": {
                "score": "5.00",
                "max": "5.00",
                "pct": "100.00%",
                "status": "success",
                "groups": [
                    {
                        "name": "i. Keterlibatan Pimpinan",
                        "score": "2.50 / 2.50 (100%)",
                        "items": [
                            {
                                "code": "1.a",
                                "question": "Pimpinan terlibat langsung pada saat penyusunan perencanaan kinerja dan anggaran",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Pimpinan memimpin langsung seluruh tahapan rapat perencanaan\n• b. Pimpinan hanya hadir saat penetapan\n• c. Tidak terlibat",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Unit kerja telah melengkapi dokumen perencanaan anggaran dan kegiatan yang mana pimpinan terlibat penuh dalam setiap tahap penyusunan perencanaan.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumentasi Rapat Perencanaan Anggaran (Undangan, Daftar Hadir, Notulen, Foto Dokumentasi)",
                                    "Dokumen Perencanaan Anggaran dan Rencana Kegiatan (POK / DIPA 2025)"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_41a_bps",
                                "drive_folder": "1 a. KETERLIBATAN PIMPINAN PERENCANAAN"
                            },
                            {
                                "code": "1.b",
                                "question": "Pimpinan terlibat langsung saat penyusunan penetapan kinerja (Perjanjian Kinerja)",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Pimpinan mengarahkan langsung target sasaran strategis dan matriks peran hasil\n• b. Parsial\n• c. Tidak terlibat",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Kepala BPS mengawal langsung perumusan target Perjanjian Kinerja (PK) tahun 2025.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Perjanjian Kinerja (PK) BPS Selayar Tahun 2025",
                                    "Dokumentasi Rapat Penyusunan Penetapan Kinerja bersama Pimpinan",
                                    "Matriks Peran Hasil (MPH) Unit Kerja"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_41b_bps",
                                "drive_folder": "1 b. PIMPINAN DALAM PENETAPAN KINERJA"
                            },
                            {
                                "code": "1.c",
                                "question": "Pimpinan memantau pencapaian kinerja secara berkala",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Pimpinan memantau dan memimpin rapat evaluasi capaian kinerja setiap triwulan\n• B: Semesteran\n• C: Tahunan\n• D: Tidak memantau",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Unit kerja telah melaksanakan monitoring capaian kinerja setiap triwulannya dipimpin langsung oleh Kepala BPS.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Pembahasan Capaian Kinerja Triwulanan (TW I, TW II, TW III)",
                                    "Risalah Rapat Evaluasi Kinerja Triwulanan dan Arahan Tindak Lanjut Pimpinan"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_41c_bps",
                                "drive_folder": "1 c. PIMPINAN MEMANTAU KINERJA"
                            }
                        ]
                    },
                    {
                        "name": "ii. Pengelolaan Akuntabilitas Kinerja",
                        "score": "2.50 / 2.50 (100%)",
                        "items": [
                            {
                                "code": "2.a",
                                "question": "Dokumen perencanaan kinerja sudah ada dan lengkap",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Dokumen Renstra, RKT, PK tersedia lengkap dan selaras\n• Tidak: Dokumen tidak lengkap",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Renstra BPS Kabupaten Kepulauan Selayar dan PK telah terdokumentasi rapi.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Perjanjian Kinerja (PK)",
                                    "Dokumen Rencana Strategis (Renstra) BPS Selayar",
                                    "Dokumen Reviu Renstra"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_42a_bps",
                                "drive_folder": "2 a. DOKUMEN PERENCANAAN KINERJA"
                            },
                            {
                                "code": "2.b",
                                "question": "Perencanaan kinerja telah berorientasi hasil (outcome-oriented)",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Sasaran strategis memuat tolok ukur dampak dan kemanfaatan data statistik\n• Tidak: Hanya berorientasi output",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Sasaran kinerja telah dirumuskan dengan Matriks Peran Hasil yang berorientasi hasil.",
                                "catatan": "",
                                "bukti": [
                                    "Matriks Peran Hasil (MPH)",
                                    "Notulen Penetapan Target PK Berorientasi Hasil",
                                    "Dokumen Perjanjian Kinerja Terkini"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_42b_bps",
                                "drive_folder": "2 b. PERENCANAAN BERORIENTASI HASIL"
                            },
                            {
                                "code": "2.c",
                                "question": "Terdapat penetapan Indikator Kinerja Utama (IKU)",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Ditetapkan IKU resmi unit kerja yang mengacu pada IKU instansi\n• Tidak: Belum ada penetapan IKU",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "IKU BPS Kabupaten Kepulauan Selayar telah ditetapkan mengacu pada regulasi IKU BPS RI.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Keputusan Penetapan IKU BPS Kabupaten Kepulauan Selayar",
                                    "Surat Edaran / Pedoman Penyusunan PK Berbasis IKU"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_42c_bps",
                                "drive_folder": "2 c. PENETAPAN IKU"
                            },
                            {
                                "code": "2.d",
                                "question": "Indikator kinerja telah memenuhi kriteria SMART (Specific, Measurable, Achievable, Relevant, Time-bound)",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: 100% indikator memenuhi kaidah SMART\n• B: 75-99%\n• C/D: <75%",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Indikator kinerja dalam LAKIN telah diuji dan memenuhi prinsip SMART.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen LAKIN BPS Kepulauan Selayar dengan penjabaran Indikator SMART",
                                    "Kertas Kerja Reviu Indikator Kinerja SMART"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_42d_bps",
                                "drive_folder": "2 d. INDIKATOR SMART"
                            },
                            {
                                "code": "2.e",
                                "question": "Laporan kinerja telah disusun tepat waktu",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Disahkan dan diunggah ke aplikasi pelaporan sebelum batas waktu\n• Tidak: Terlambat",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "LAKIN BPS Kabupaten Kepulauan Selayar disahkan pimpinan tepat waktu pada awal tahun.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen LAKIN yang disahkan oleh Kepala BPS",
                                    "Bukti tanda terima unggah pada SiMonev Bappenas dan SIPERMADU"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_42e_bps",
                                "drive_folder": "2 e. LAPORAN KINERJA TEPAT WAKTU"
                            },
                            {
                                "code": "2.f",
                                "question": "Laporan kinerja telah memberikan informasi yang memadai tentang pencapaian kinerja",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Memuat analisis komprehensif, perbandingan target vs realisasi, efisiensi anggaran, dan kendala\n• b. Analisis deskriptif terbatas\n• c. Hanya tabel angka",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "LAKIN memuat analisis capaian, faktor pendorong, kendala, dan rekomendasi perbaikan pada Bab III.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen LAKIN Lengkap (Terdapat Informasi Analisis Kinerja Mendalam pada BAB III)"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_42f_bps",
                                "drive_folder": "2 f. INFORMASI KINERJA DALAM LAKIN"
                            },
                            {
                                "code": "2.g",
                                "question": "Terdapat sistem informasi / mekanisme pengelolaan informasi kinerja",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Dikelola tim SAKIP didukung sistem informasi kinerja handal\n• Tidak: Belum terorganisir",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Pengelolaan akuntabilitas kinerja dikoordinasikan oleh Tim SAKIP terintegrasi.",
                                "catatan": "",
                                "bukti": [
                                    "SK Tim SAKIP BPS Kabupaten Kepulauan Selayar",
                                    "Daftar data personil pengelola dan kompetensi teknis SAKIP"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_42g_bps",
                                "drive_folder": "2 g. PENGELOLA SISTEM INFORMASI KINERJA"
                            },
                            {
                                "code": "2.h",
                                "question": "Unit kerja telah berupaya meningkatkan kapasitas SDM yang menangani akuntabilitas kinerja",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Seluruh personil pengelola SAKIP telah mengikuti bimtek/sosialisasi SAKIP\n• b. Sebagian\n• c. Belum pernah",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Tim SAKIP aktif mengikuti sosialisasi dan bimbingan teknis penyusunan LAKIN.",
                                "catatan": "",
                                "bukti": [
                                    "Sertifikat Pelatihan / Bimtek SAKIP Pegawai",
                                    "SK Tim Pengelola SAKIP",
                                    "Data Profil Kompetensi Pengelola Akuntabilitas Kinerja"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_42h_bps",
                                "drive_folder": "2 h. PENINGKATAN KAPASITAS TIM SAKIP"
                            }
                        ]
                    }
                ]
            },
            "reform": {
                "score": "3.50",
                "max": "5.00",
                "pct": "70.00%",
                "status": "warning",
                "groups": [
                    {
                        "name": "Reform i. Meningkatnya Capaian Kinerja",
                        "score": "2.00 / 2.00 (100%)",
                        "items": [
                            {
                                "code": "R.1",
                                "question": "Persentase Sasaran Strategis dengan capaian 100% atau lebih",
                                "tipe": "% (Persentase)",
                                "kriteria": "Persentase rata-rata realisasi target kinerja terhadap target perjanjian kinerja tahun berjalan.",
                                "jawaban": "105.74%",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Melampaui Target (105.74%)",
                                "narasi": "Realisasi seluruh indikator kinerja utama melampaui target yang ditetapkan dalam Perjanjian Kinerja dengan rata-rata 105.74%.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen LAKIN BPS Kabupaten Kepulauan Selayar (Bab Evaluasi Capaian Sasaran)",
                                    "Matriks Pengukuran Kinerja Akhir Tahun"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_Reform1_bps",
                                "drive_folder": "R1. PENINGKATAN CAPAIAN KINERJA"
                            }
                        ]
                    },
                    {
                        "name": "Reform ii. Pemberian Reward and Punishment",
                        "score": "0.00 / 1.50 (0%)",
                        "items": [
                            {
                                "code": "R.2",
                                "question": "Hasil capaian monitoring PK dijadikan dasar pemberian reward and punishment organisasi",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Diterapkan secara formal berbasis Peraturan/SK dan berdampak riil pada reward/punishment tim\n• B/C: Sebagian\n• D: Belum dijadikan dasar secara formal",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Pemberian reward & punishment baru sebatas individu (EOM), belum mencakup skema reward/punishment berbasis capaian PK tim kerja.",
                                "catatan": "PERHATIAN: Susun mekanisme dan SK pemberian reward & punishment bagi tim kerja berdasarkan realisasi Perjanjian Kinerja (PK) triwulanan.",
                                "bukti": [
                                    "Dokumen LAKIN & Laporan Capaian PK",
                                    "Dokumen Mekanisme / SK Kepala BPS tentang Pemberian Reward dan Punishment Berbasis Capaian PK",
                                    "Bukti Penyerahan Reward / Teguran Tertulis terkait pencapaian PK"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_Reform2_bps",
                                "drive_folder": "R2. REWARD PUNISHMENT PK"
                            }
                        ]
                    },
                    {
                        "name": "Reform iii. Kerangka Logis Kinerja",
                        "score": "1.50 / 1.50 (100%)",
                        "items": [
                            {
                                "code": "R.3",
                                "question": "Terdapat penjenjangan kinerja (Kerangka Logis Kinerja / Cascading Logis)",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Kerangka logis penjenjangan kinerja selaras dari level BPS RI, Provinsi, hingga satker kabupaten\n• B/C/D: Sebagian atau belum ada kerangka logis",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Kerangka logis kinerja telah terstruktur dengan rapi menghubungkan visi BPS ke level tim kerja dan IKI.",
                                "catatan": "",
                                "bukti": [
                                    "Matriks Peran Hasil (MPH) Penjenjangan Kinerja",
                                    "Dokumen IKU & Perjanjian Kinerja (PK)",
                                    "Indikator Kinerja Individu (IKI) Berjenjang"
                                ],
                                "link_contoh": "http://s.bps.go.id/Akuntabilitas_Reform3_bps",
                                "drive_folder": "R3. KERANGKA LOGIS KINERJA"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": "area5",
            "number": 5,
            "title": "Penguatan Pengawasan",
            "icon": "🛡️",
            "desc": "Bertujuan untuk meningkatkan penyelenggaraan pemerintahan yang bersih dan bebas KKN pada BPS Kabupaten Kepulauan Selayar melalui pengendalian gratifikasi, penerapan SPIP, penanganan pengaduan masyarakat, WBS, dan penanganan benturan kepentingan.",
            "pemenuhan": {
                "score": "3.38",
                "max": "7.50",
                "pct": "45.00%",
                "status": "danger",
                "groups": [
                    {
                        "name": "i. Pengendalian Gratifikasi",
                        "score": "1.50 / 1.50 (100%)",
                        "items": [
                            {
                                "code": "1.a",
                                "question": "Telah dilakukan public campaign tentang pengendalian gratifikasi dan tolak suap/pungli",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Public campaign dilakukan rutin multi-kanal (banner kantor, medsos, website, sosialisasi eksternal)\n• b. Parsial\n• c. Belum ada campaign",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Public campaign anti gratifikasi dipasang jelas di loket PST, media sosial, serta ditekankan dalam setiap sosialisasi survei.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumentasi & tangkapan layar banner, spanduk, dan postingan media sosial tolak gratifikasi",
                                    "Dokumen sosialisasi larangan gratifikasi dalam rapat bersama responden dan mitra eksternal",
                                    "Dokumen Pakta Integritas Pegawai & Foto penandatanganan pakta integritas bersama"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_1a_bps",
                                "drive_folder": "1 a. PUBLIC CAMPAIGN GRATIFIKASI"
                            },
                            {
                                "code": "1.b",
                                "question": "Pengendalian gratifikasi telah diimplementasikan secara terstruktur",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Tim UPG aktif, memiliki SOP/alur pelaporan, dan menyusun laporan monev nihil/gratifikasi berkala\n• B/C/D: Sebagian",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Unit Pengendali Gratifikasi (UPG) telah dibentuk dan melaporkan kondisi gratifikasi secara periodik.",
                                "catatan": "",
                                "bukti": [
                                    "SK Tim UPG (Unit Pengendali Gratifikasi) BPS Kabupaten Kepulauan Selayar",
                                    "Mekanisme / Rencana Aksi dan SOP Pengendalian Gratifikasi",
                                    "Laporan Monitoring dan Evaluasi UPG (Laporan Nihil Gratifikasi Semesteran)"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_1b_bps",
                                "drive_folder": "1 b. IMPLEMENTASI UPG"
                            }
                        ]
                    },
                    {
                        "name": "ii. Penerapan SPIP (Sistem Pengendalian Intern Pemerintah)",
                        "score": "0.38 / 1.50 (25.00%)",
                        "items": [
                            {
                                "code": "2.a",
                                "question": "Telah dibangun lingkungan pengendalian yang memadai",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Lingkungan pengendalian kondusif, terdapat SK Tim SPIP dan laporan penyelenggaraan resmi\n• B/C/D/E: Sebagian atau belum",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Lingkungan pengendalian internal dibangun melalui komitmen pimpinan dan pembentukan Satgas SPIP.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen sosialisasi SPIP kepada seluruh pegawai",
                                    "SK Tim Satgas SPIP BPS Kabupaten Kepulauan Selayar",
                                    "Dokumen Laporan Penyelenggaraan SPIP Unit Kerja"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_2a_bps",
                                "drive_folder": "2 a. LINGKUNGAN PENGENDALIAN SPIP"
                            },
                            {
                                "code": "2.b",
                                "question": "Telah dilakukan penilaian risiko (Risk Assessment) atas pelaksanaan tugas dan fungsi",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Manajemen risiko menyeluruh di seluruh proses bisnis, register risiko terdata lengkap\n• B/C/D: Sebagian\n• E: Belum dilakukan penilaian risiko secara komprehensif",
                                "jawaban": "E",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Dokumen manajemen risiko unit kerja belum terpetakan dalam Daftar Register Risiko resmi.",
                                "catatan": "PERHATIAN KRITIS: Segera susun Dokumen Manajemen Risiko (Risk Assessment) dan Register Risiko untuk seluruh kegiatan teknis dan administrasi BPS Selayar.",
                                "bukti": [
                                    "Dokumen Manajemen Risiko (Risk Assessment) BPS Kabupaten Kepulauan Selayar",
                                    "Daftar Register Risiko Organisasi (Peluang & Ancaman)"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_2b_bps",
                                "drive_folder": "2 b. PENILAIAN RISIKO"
                            },
                            {
                                "code": "2.c",
                                "question": "Telah dilakukan kegiatan pengendalian untuk meminimalisir risiko yang telah diidentifikasi",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Terdapat Rencana Tindak Pengendalian (RTP) untuk setiap risiko dan diimplementasikan\n• b. Ada RTP tapi belum diimplementasikan\n• c. Belum ada kegiatan pengendalian risiko",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Rencana Tindak Pengendalian (RTP) risiko belum dituangkan ke dalam matriks mitigasi risiko.",
                                "catatan": "PERHATIAN KRITIS: Buat Dokumen Rencana Tindak Pengendalian (RTP) Risiko sebagai turunan dari register risiko.",
                                "bukti": [
                                    "Dokumen Rencana Tindak Pengendalian (RTP) Risiko BPS Kabupaten Kepulauan Selayar",
                                    "Laporan Pelaksanaan Mitigasi Pengendalian Risiko"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_2c_bps",
                                "drive_folder": "2 c. KEGIATAN PENGENDALIAN RISIKO"
                            },
                            {
                                "code": "2.d",
                                "question": "Sistem Pengendalian Intern (SPI) telah diinformasikan dan dikomunikasikan kepada seluruh jajaran",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Dikomunikasikan berkala melalui media formal dan sosialisasi rutin\n• b. Terbatas\n• c. Belum dikomunikasikan secara luas",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Internalisasi SPIP kepada staf pelaksana masih perlu dilengkapi bukti dokumentasinya.",
                                "catatan": "PERHATIAN: Laksanakan sosialisasi SPIP internal dan lengkapi risalah rapat (undangan, notulen, materi, daftar hadir).",
                                "bukti": [
                                    "Notulen dan Daftar Hadir Rapat Sosialisasi / Internalisasi SPIP",
                                    "Media Informasi / Banner Edukasi SPIP di Lingkungan Kantor"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_2d_bps",
                                "drive_folder": "2 d. KOMUNIKASI SPIP"
                            }
                        ]
                    },
                    {
                        "name": "iii. Pengaduan Masyarakat",
                        "score": "0.00 / 1.50 (0%)",
                        "items": [
                            {
                                "code": "3.a",
                                "question": "Kebijakan penanganan pengaduan masyarakat telah diimplementasikan",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Ditetapkan SK Tim Pengelola Pengaduan, SOP penanganan pengaduan, dan sarana pengaduan aktif\n• b. SOP ada tapi belum aktif\n• c. Belum diimplementasikan",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "SOP dan SK pengelolaan pengaduan masyarakat di satker perlu diperbarui dan diaktifkan secara terpadu.",
                                "catatan": "PERHATIAN KRITIS: Buat SK Tim Pengelola Pengaduan dan SOP Penanganan Pengaduan Masyarakat Satker 2025.",
                                "bukti": [
                                    "SK Tim Pengelola Pengaduan Masyarakat BPS Kabupaten Kepulauan Selayar",
                                    "Dokumen SOP Penanganan Pengaduan Masyarakat",
                                    "Dokumentasi Sarana Pengaduan (Kotak Saran, Banner, Nomor Hotline)"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_3a_bps",
                                "drive_folder": "3 a. KEBIJAKAN PENGADUAN MASYARAKAT"
                            },
                            {
                                "code": "3.b",
                                "question": "Pengaduan masyarakat ditindaklanjuti secara cepat dan tuntas",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: 100% aduan masyarakat ditindaklanjuti sesuai batas waktu SOP\n• Tidak: Ada aduan tidak ditindaklanjuti atau dokumen nihil tidak tersedia",
                                "jawaban": "Tidak",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Laporan penanganan pengaduan atau surat keterangan register aduan belum disusun ke dalam buku register.",
                                "catatan": "PERHATIAN KRITIS: Buat Buku Register Pengaduan Masyarakat (jika tidak ada aduan, buat Surat Keterangan / Laporan Nihil Pengaduan).",
                                "bukti": [
                                    "Buku Register Pengaduan Masyarakat Tahun 2025",
                                    "Laporan Tindak Lanjut Pengaduan Masyarakat / Surat Keterangan Nihil Aduan"
                                ],
                                "link_contoh": "https://s.bps.go.id/Pengawasan_3b_bps",
                                "drive_folder": "3 b. TINDAK LANJUT PENGADUAN"
                            },
                            {
                                "code": "3.c",
                                "question": "Telah dilakukan monitoring dan evaluasi atas penanganan pengaduan masyarakat",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Monev pengaduan dilakukan berkala per triwulan/semester\n• b. Tahunan\n• c. Belum dilakukan monev",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Belum ada dokumen laporan monev pengaduan masyarakat secara berkala.",
                                "catatan": "PERHATIAN KRITIS: Susun Laporan Monev Penanganan Pengaduan Triwulanan.",
                                "bukti": [
                                    "Laporan Monitoring dan Evaluasi Penanganan Pengaduan Masyarakat Berkala"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_3c_bps",
                                "drive_folder": "3 c. MONEV PENGADUAN MASYARAKAT"
                            },
                            {
                                "code": "3.d",
                                "question": "Hasil evaluasi atas penanganan pengaduan masyarakat telah ditindaklanjuti",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Rekomendasi perbaikan pelayanan dari aduan 100% ditindaklanjuti\n• b. Sebagian\n• c. Belum ditindaklanjuti",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Laporan tindak lanjut hasil monev pengaduan masyarakat belum terdokumentasi.",
                                "catatan": "PERHATIAN KRITIS: Susun dokumen laporan tindak lanjut rekomendasi hasil evaluasi pengaduan.",
                                "bukti": [
                                    "Laporan Tindak Lanjut Evaluasi Penanganan Pengaduan Masyarakat"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_3d_bps",
                                "drive_folder": "3 d. TINDAK LANJUT EVALUASI ADUAN"
                            }
                        ]
                    },
                    {
                        "name": "iv. Whistle-Blowing System (WBS)",
                        "score": "1.50 / 1.50 (100%)",
                        "items": [
                            {
                                "code": "4.a",
                                "question": "Whistle-Blowing System (WBS) telah diterapkan dan disosialisasikan",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Kanal WBS BPS diterapkan, disosialisasikan intensif, dan tim pengelola aktif\n• b. Parsial\n• c. Belum diterapkan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "WBS BPS RI telah terintegrasi di lingkungan kantor dan disosialisasikan kepada pegawai dan mitra.",
                                "catatan": "",
                                "bukti": [
                                    "SK Tim Pengelola Whistle-Blowing System (WBS) Unit Kerja",
                                    "Dokumen Kebijakan & Pedoman WBS",
                                    "Tangkapan Layar Aplikasi WBS BPS dan Media Sosial",
                                    "Dokumentasi Banner / X-Banner WBS di Kantor",
                                    "Laporan Pengelolaan dan Sosialisasi WBS"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_4a_bps",
                                "drive_folder": "4 a. PENERAPAN WBS"
                            },
                            {
                                "code": "4.b",
                                "question": "Telah dilakukan evaluasi atas penerapan Whistle-Blowing System (WBS)",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Evaluasi penerapan WBS dilakukan rutin secara berkala\n• b. Evaluasi parsial\n• c. Belum ada evaluasi",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Evaluasi pengelolaan kanal pelaporan pelanggaran WBS dilaksanakan setiap semester.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Pengelolaan dan Evaluasi Penerapan WBS BPS Kabupaten Kepulauan Selayar"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_4b_bps",
                                "drive_folder": "4 b. EVALUASI WBS"
                            },
                            {
                                "code": "4.c",
                                "question": "Hasil evaluasi atas penerapan WBS telah ditindaklanjuti",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Seluruh rekomendasi monev WBS telah ditindaklanjuti 100%\n• b. Sebagian\n• c. Belum ditindaklanjuti",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Tindak lanjut evaluasi WBS telah dilaksanakan guna memastikan kerahasiaan dan kemudahan akses pelapor.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Tindak Lanjut Hasil Evaluasi Pengelolaan WBS"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_4c_bps",
                                "drive_folder": "4 c. TINDAK LANJUT EVALUASI WBS"
                            }
                        ]
                    },
                    {
                        "name": "v. Penanganan Benturan Kepentingan (Conflict of Interest)",
                        "score": "0.00 / 1.50 (0%)",
                        "items": [
                            {
                                "code": "5.a",
                                "question": "Telah terdapat identifikasi / pemetaan potensi benturan kepentingan",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Pemetaan benturan kepentingan lengkap untuk seluruh proses layanan, pengadaan barang jasa, dan kepegawaian\n• B/C: Parsial\n• D: Belum diidentifikasi",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Belum ada dokumen resmi pemetaan potensi benturan kepentingan.",
                                "catatan": "PERHATIAN KRITIS: Buat Dokumen Identifikasi dan Pemetaan Potensi Benturan Kepentingan di BPS Kabupaten Kepulauan Selayar (PBJ, perekrutan mitra, mutasi).",
                                "bukti": [
                                    "Dokumen Identifikasi & Pemetaan Potensi Benturan Kepentingan Tahun 2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_5a_bps",
                                "drive_folder": "5 a. PEMETAAN BENTURAN KEPENTINGAN"
                            },
                            {
                                "code": "5.b",
                                "question": "Penanganan benturan kepentingan telah disosialisasikan kepada seluruh pegawai",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Disosialisasikan intensif disertai bukti rapat, banner, dan komitmen bersama\n• B/C: Sebagian\n• D: Belum disosialisasikan",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Sosialisasi penanganan benturan kepentingan belum dilaksanakan secara formal.",
                                "catatan": "PERHATIAN KRITIS: Selenggarakan sosialisasi pencegahan benturan kepentingan dan buat laporannya.",
                                "bukti": [
                                    "Laporan Pelaksanaan Sosialisasi Penanganan Benturan Kepentingan",
                                    "Undangan, Notulen, dan Daftar Hadir Rapat Sosialisasi",
                                    "Foto Dokumentasi Sosialisasi Benturan Kepentingan"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_5b_bps",
                                "drive_folder": "5 b. SOSIALISASI BENTURAN KEPENTINGAN"
                            },
                            {
                                "code": "5.c",
                                "question": "Penanganan benturan kepentingan telah diimplementasikan dalam pelaksanaan tugas",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Telah ada penandatanganan Surat Pernyataan Bebas Benturan Kepentingan oleh pejabat pengadaan, pimpinan, dan tim kerja\n• B/C: Sebagian\n• D: Belum diimplementasikan",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Surat pernyataan bebas benturan kepentingan belum diisi dan dihimpun.",
                                "catatan": "PERHATIAN KRITIS: Seluruh PPK, Pejabat Pengadaan, Panitia Seleksi Mitra, dan Pimpinan wajib menandatangani Surat Pernyataan Bebas Benturan Kepentingan.",
                                "bukti": [
                                    "Surat Pernyataan Bebas Benturan Kepentingan (PPK, Pengadaan, Mitra, Pimpinan)",
                                    "Logbook Implementasi Penanganan Benturan Kepentingan"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_5c_bps",
                                "drive_folder": "5 c. IMPLEMENTASI BENTURAN KEPENTINGAN"
                            },
                            {
                                "code": "5.d",
                                "question": "Telah dilakukan evaluasi atas penanganan benturan kepentingan",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Evaluasi dilakukan secara berkala tiap semester\n• b. Tahunan\n• c. Belum dievaluasi",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Laporan evaluasi berkala penanganan benturan kepentingan belum tersedia.",
                                "catatan": "PERHATIAN KRITIS: Buat Laporan Evaluasi Penanganan Benturan Kepentingan Semester I & II.",
                                "bukti": [
                                    "Laporan Evaluasi Penanganan Benturan Kepentingan BPS Selayar"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_5d_bps",
                                "drive_folder": "5 d. EVALUASI BENTURAN KEPENTINGAN"
                            },
                            {
                                "code": "5.e",
                                "question": "Hasil evaluasi atas penanganan benturan kepentingan telah ditindaklanjuti",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Seluruh rekomendasi evaluasi ditindaklanjuti 100%\n• b. Sebagian\n• c. Belum ditindaklanjuti",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Belum ada dokumen tindak lanjut dari hasil evaluasi benturan kepentingan.",
                                "catatan": "PERHATIAN KRITIS: Susun laporan tindak lanjut rekomendasi hasil evaluasi benturan kepentingan.",
                                "bukti": [
                                    "Laporan Tindak Lanjut Hasil Evaluasi Benturan Kepentingan"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_5e_bps",
                                "drive_folder": "5 e. TINDAK LANJUT EVALUASI BENTURAN"
                            }
                        ]
                    }
                ]
            },
            "reform": {
                "score": "7.50",
                "max": "7.50",
                "pct": "100.00%",
                "status": "success",
                "groups": [
                    {
                        "name": "Reform i. Mekanisme Pengendalian",
                        "score": "2.50 / 2.50 (100%)",
                        "items": [
                            {
                                "code": "R.1",
                                "question": "Telah dilakukan mekanisme pengendalian aktivitas secara berjenjang (Supervisi & Reviu)",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Mekanisme pengendalian aktivitas berjenjang berjalan 100% didukung kartu kendali / catatan reviu atasan\n• B/C/D/E: Sebagian atau belum",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Pengendalian tugas dan administrasi dilakukan berjenjang melalui reviu ketua tim kerja dan persetujuan pimpinan.",
                                "catatan": "",
                                "bukti": [
                                    "Matriks Pengendalian Berjenjang Kegiatan Lapangan dan Administrasi",
                                    "Catatan Reviu Atasan Langsung pada Aplikasi Manajemen Tugas dan Persuratan",
                                    "Kartu Kendali Supervisi Kegiatan Lapangan"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_reform_ia_bps",
                                "drive_folder": "R1. PENGENDALIAN BERJENJANG"
                            }
                        ]
                    },
                    {
                        "name": "Reform ii. Penanganan Pengaduan Masyarakat",
                        "score": "3.00 / 3.00 (100%)",
                        "items": [
                            {
                                "code": "R.2",
                                "question": "Persentase penanganan pengaduan masyarakat yang selesai ditindaklanjuti",
                                "tipe": "% (Persentase)",
                                "kriteria": "Rasio aduan yang diselesaikan terhadap total aduan yang masuk. Jika nihil aduan, dinilai 100%.",
                                "jawaban": "100%",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Sempurna (100%)",
                                "narasi": "Jumlah pengaduan yang harus ditindaklanjuti: 0, sedang diproses: 0, selesai: 0 (Tingkat penyelesaian 100% nihil tunggakan).",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Rekapitulasi Penanganan Pengaduan Masyarakat (Tingkat Penyelesaian 100%)",
                                    "Surat Keterangan Nihil Aduan Tertunggak dari Pengelola Pengaduan"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_reform_iia_bps",
                                "drive_folder": "R2. PENYELESAIAN PENGADUAN REFORM"
                            }
                        ]
                    },
                    {
                        "name": "Reform iii. Penyampaian Laporan Harta Kekayaan (LHKPN & LHKASN)",
                        "score": "2.00 / 2.00 (100%)",
                        "items": [
                            {
                                "code": "R.3.a",
                                "question": "Tingkat kepatuhan penyampaian LHKPN pejabat wajib lapor tepat waktu",
                                "tipe": "% (Persentase)",
                                "kriteria": "Persentase wajib lapor LHKPN yang telah menyampaikan tanda terima KPK tepat waktu.",
                                "jawaban": "100% (5 dari 5 Wajib Lapor)",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Sempurna (100%)",
                                "narasi": "Tingkat kepatuhan 100%. Wajib lapor sebanyak 5 orang (Kepala BPS: 1 orang, PPK / Pejabat Pengadaan / Bendahara: 4 orang), seluruhnya telah melapor 100% tepat waktu.",
                                "catatan": "",
                                "bukti": [
                                    "Kompilasi Tanda Terima e-LHKPN KPK Seluruh Pejabat Wajib Lapor 2025",
                                    "Rekapitulasi Kepatuhan Pelaporan LHKPN BPS Kabupaten Kepulauan Selayar"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_reform_iii_ia_bps",
                                "drive_folder": "R3 a. KEPATUHAN LHKPN"
                            },
                            {
                                "code": "R.3.b",
                                "question": "Tingkat kepatuhan penyampaian Non LHKPN (LHKASN/SPT)",
                                "tipe": "% (Persentase)",
                                "kriteria": "Persentase wajib lapor LHKASN/SPT.",
                                "jawaban": "0% (Jumlah Wajib: 0 Non-LHKPN Khusus)",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Sempurna (100% SPT Patuh)",
                                "narasi": "Seluruh pegawai non-LHKPN mematuhi pelaporan SPT tahunan melalui DJP Online secara lengkap.",
                                "catatan": "",
                                "bukti": [
                                    "Bukti Penerimaan Elektronik (BPE) SPT Tahunan Seluruh Pegawai BPS Selayar",
                                    "Rekapitulasi Kepatuhan SPT Tahunan Satker"
                                ],
                                "link_contoh": "http://s.bps.go.id/Pengawasan_reform_iii_iia_bps",
                                "drive_folder": "R3 b. KEPATUHAN NON LHKPN"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": "area6",
            "number": 6,
            "title": "Peningkatan Kualitas Pelayanan Publik",
            "icon": "⭐",
            "desc": "Bertujuan untuk meningkatkan kualitas dan inovasi pelayanan publik pada BPS Kabupaten Kepulauan Selayar sesuai kebutuhan dan harapan masyarakat melalui standar pelayanan, budaya pelayanan prima, pengelolaan pengaduan, dan survei kepuasan.",
            "pemenuhan": {
                "score": "3.95",
                "max": "5.00",
                "pct": "78.90%",
                "status": "warning",
                "groups": [
                    {
                        "name": "i. Standar Pelayanan",
                        "score": "1.00 / 1.00 (100%)",
                        "items": [
                            {
                                "code": "1.a",
                                "question": "Terdapat kebijakan standar pelayanan yang ditetapkan dan berlaku resmi",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Ditetapkan Standar Pelayanan Publik resmi mengacu Perka BPS 78/2020 dan Permenpan\n• B/C/D/E: Sebagian atau belum",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Standar Pelayanan Publik telah ditetapkan melalui SK Kepala BPS mengacu pada Perka BPS No 78 Tahun 2020.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen SK Standar Pelayanan Publik BPS Kepulauan Selayar Tahun 2024-2025",
                                    "Buku Standar Pelayanan Publik BPS (Perka BPS No 78 Tahun 2020)"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_1a_bps",
                                "drive_folder": "1 a. KEBIJAKAN STANDAR PELAYANAN"
                            },
                            {
                                "code": "1.b",
                                "question": "Standar pelayanan telah dimaklumatkan secara luas",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Maklumat pelayanan dipajang di ruang PST, website, dan media sosial\n• B: Terpasang di satu tempat\n• C/D: Belum dimaklumatkan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Maklumat Pelayanan dipajang dengan jelas di lobby pelayanan PST dan dipublikasikan di kanal digital.",
                                "catatan": "",
                                "bukti": [
                                    "Foto Maklumat Standar Pelayanan di Ruang PST Kantor BPS",
                                    "Tangkapan layar Maklumat Pelayanan pada Website Resmi & Media Sosial"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_1b_bps",
                                "drive_folder": "1 b. MAKLUMAT PELAYANAN"
                            },
                            {
                                "code": "1.c",
                                "question": "Dilakukan reviu dan perbaikan atas standar pelayanan",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Reviu standar pelayanan dilakukan berkala melibatkan pengguna layanan (FKP)\n• B: Reviu internal\n• C/D: Belum direviu",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Standar pelayanan ditinjau berkala melalui Forum Konsultasi Publik (FKP).",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Laporan Pelaksanaan Forum Konsultasi Publik (FKP) Standar Pelayanan",
                                    "Laporan Reviu dan Perbaikan Standar Pelayanan BPS Selayar",
                                    "Berita Acara Kesepakatan Reviu Standar Pelayanan"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_1c_bps",
                                "drive_folder": "1 c. REVIU STANDAR PELAYANAN"
                            },
                            {
                                "code": "1.d",
                                "question": "Telah melakukan publikasi atas standar pelayanan dan maklumat pelayanan",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Dipublikasikan multi-media luring dan daring\n• Tidak: Tidak dipublikasikan",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Publikasi standar pelayanan mencakup brosur, standing banner, website, dan medsos.",
                                "catatan": "",
                                "bukti": [
                                    "Narasi dan dokumentasi publikasi standar pelayanan",
                                    "Foto dan tangkapan layar publikasi maklumat pelayanan di berbagai platform"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_1d_bps",
                                "drive_folder": "1 d. PUBLIKASI STANDAR PELAYANAN"
                            }
                        ]
                    },
                    {
                        "name": "ii. Budaya Pelayanan Prima",
                        "score": "0.61 / 1.00 (61.17%)",
                        "items": [
                            {
                                "code": "2.a",
                                "question": "Telah dilakukan berbagai upaya peningkatan kemampuan tentang budaya pelayanan prima",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Pelatihan / service excellence rutin diselenggarakan bagi petugas PST\n• B/C/D/E: Sebagian atau belum",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Petugas PST dibekali pelatihan service excellence dan knowledge sharing rutin.",
                                "catatan": "",
                                "bukti": [
                                    "Laporan Pelaksanaan Knowledge Sharing PST / Pelatihan Service Excellence",
                                    "Undangan, Daftar Hadir, dan Dokumentasi Pelatihan",
                                    "Laporan Tahunan Pelayanan Publik Tahun 2024-2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_2a_bps",
                                "drive_folder": "2 a. PELATIHAN PELAYANAN PRIMA"
                            },
                            {
                                "code": "2.b",
                                "question": "Informasi tentang pelayanan mudah diakses melalui berbagai sarana",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Informasi layanan sangat mudah diakses di kantor, website, SIPPN KemenpanRB, medsos\n• B/C/D: Terbatas",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "partial",
                                "badge": "Catatan: Update SIPPN",
                                "narasi": "Sarana informasi pelayanan telah tersedia di PST dan web, namun akun SIPPN perlu dimutakhirkan.",
                                "catatan": "CATATAN KHUSUS: UPDATE 2025 (SIPPN KemenPANRB belum diperbarui). Segera login dan update profil layanan di SIPPN!",
                                "bukti": [
                                    "Tangkapan layar sarana informasi pelayanan pada berbagai media sosial & website",
                                    "Tangkapan layar profil satker pada portal SIPPN KemenPANRB (Perlu Update 2025)",
                                    "Brosur / Leaflet Layanan PST"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_2b_bps",
                                "drive_folder": "2 b. AKSES INFORMASI PELAYANAN"
                            },
                            {
                                "code": "2.c",
                                "question": "Telah terdapat sistem pemberian penghargaan dan sanksi bagi petugas pemberi pelayanan",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: SK dan mekanisme reward/punishment khusus petugas pelayanan diterapkan konsisten\n• B/C: Parsial\n• D: Belum ada skema reward/punishment petugas PST",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Belum ada dokumen formal reward and punishment khusus petugas layanan PST.",
                                "catatan": "PERHATIAN: Buat SK dan Mekanisme Reward & Punishment khusus petugas layanan PST beserta bukti pemberian apresiasi.",
                                "bukti": [
                                    "Dokumen Mekanisme & SK Kepala BPS tentang Reward and Punishment Petugas Pelayanan",
                                    "Laporan Tahunan Pelayanan Publik (Bab Apresiasi Petugas PST)",
                                    "Foto Penyerahan Piagam Penghargaan Petugas Pelayanan Terbaik"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_2c_bps",
                                "drive_folder": "2 c. REWARD PUNISHMENT PETUGAS"
                            },
                            {
                                "code": "2.d",
                                "question": "Telah terdapat sistem pemberian kompensasi kepada penerima layanan bila layanan tidak sesuai standar",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Ditetapkan mekanisme kompensasi dan direalisasikan saat terjadi keterlambatan layanan\n• B: Mekanisme ada namun belum disosialisasikan luas\n• C/D: Belum ada kompensasi",
                                "jawaban": "B",
                                "nilai": "0.67",
                                "status": "partial",
                                "badge": "Perlu Ditingkatkan",
                                "narasi": "Mekanisme kompensasi layanan (souvenir/permohonan maaf resmi) telah dirancang namun belum dipublikasikan di maklumat.",
                                "catatan": "PERHATIAN: Cantumkan kompensasi layanan secara tegas pada banner maklumat dan buat SK penetapan kompensasi.",
                                "bukti": [
                                    "Dokumen Mekanisme dan SK Penetapan Pemberian Kompensasi Layanan",
                                    "Laporan Tahunan Pelayanan Publik (Klausul Kompensasi Keterlambatan Layanan)"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_2d_bps",
                                "drive_folder": "2 d. KOMPENSASI PELAYANAN"
                            },
                            {
                                "code": "2.e",
                                "question": "Terdapat sarana layanan terpadu / terintegrasi (PST)",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Tersedia ruang Pelayanan Statistik Terpadu (PST) representatif, ramah difabel, dan terhubung online\n• B/C/D: Kurang memadai",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "PST BPS Kepulauan Selayar menyediakan ruang representatif dilengkapi fasilitas ramah disabilitas dan layanan daring.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumentasi Foto Fasilitas Layanan PST (Meja Layanan, Ruang Laktasi, Jalur Disabilitas, Buku Tamu Digital)",
                                    "Tangkapan layar layanan PST Online dan Allstat"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_2e_bps",
                                "drive_folder": "2 e. SARANA LAYANAN TERPADU PST"
                            },
                            {
                                "code": "2.f",
                                "question": "Terdapat inovasi pelayanan yang mempermudah dan mempercepat layanan publik",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Memiliki inovasi layanan publik unggulan yang telah teruji dan beroperasi stabil\n• B/C/D: Inovasi tahap awal\n• E: Belum ada inovasi layanan terdata",
                                "jawaban": "E",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Inovasi layanan belum terangkum dalam dokumen proposal inovasi / laporan dampak inovasi resmi.",
                                "catatan": "PERHATIAN KRITIS: Buat Laporan / Profil Inovasi Layanan Publik (Inovasi Desa Cantik, inovasi sarana/layanan digital lokal).",
                                "bukti": [
                                    "Dokumen Profil dan Inovasi Sarana Prasarana Layanan",
                                    "Buku Panduan dan Laporan Dampak Inovasi Pelayanan Publik",
                                    "Laporan Pelaksanaan Inovasi Pembinaan Desa Cantik (Desa Cinta Statistik)"
                                ],
                                "link_contoh": "http://s.bps.go.id/PeningkatanKualitasPelayananPublik_2f_bps",
                                "drive_folder": "2 f. INOVASI PELAYANAN PUBLIK"
                            }
                        ]
                    },
                    {
                        "name": "iii. Pengelolaan Pengaduan Pelayanan",
                        "score": "0.67 / 1.00 (66.67%)",
                        "items": [
                            {
                                "code": "3.a",
                                "question": "Terdapat media pengaduan dan konsultasi pelayanan yang terintegrasi dengan SP4N-Lapor!",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Terhubung aktif dengan SP4N-LAPOR!, admin ditunjuk dengan SK resmi\n• B/C/D/E: Sebagian atau belum",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Pengaduan layanan telah terintegrasi dengan SP4N-LAPOR! dan admin unit kerja aktif memantau.",
                                "catatan": "",
                                "bukti": [
                                    "Tangkapan layar profil instansi BPS Selayar pada lapor.go.id",
                                    "Dokumentasi akses dan dashboard admin SP4N-LAPOR!",
                                    "SK Satgas / Tim Penanganan Pengaduan BPS Selayar"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_3a_bps",
                                "drive_folder": "3 a. MEDIA SP4N LAPOR"
                            },
                            {
                                "code": "3.b",
                                "question": "Terdapat unit yang mengelola pengaduan dan konsultasi pelayanan",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Unit pengelola aduan ditetapkan resmi dengan uraian tugas jelas\n• b. Parsial\n• c. Tidak ada unit pengelola",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Pengelolaan aduan dilakukan oleh tim terpadu di bawah pengawasan Kasubbag Umum.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumentasi akses admin SP4N-LAPOR!",
                                    "SK Penanganan Pengaduan di Level Unit Kerja Tahun 2024-2025"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_3b_bps",
                                "drive_folder": "3 b. UNIT PENGELOLA PENGADUAN"
                            },
                            {
                                "code": "3.c",
                                "question": "Telah dilakukan evaluasi atas penanganan keluhan / masukan dan konsultasi",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Evaluasi dilakukan berkala per triwulan/semester\n• b. Tahunan\n• c. Belum ada dokumen evaluasi",
                                "jawaban": "C",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Laporan rekap evaluasi konsultasi dan pengaduan belum diunggah untuk periode berjalan.",
                                "catatan": "CATATAN KHUSUS: UPLOAD 2026. Susun dan unggah dokumen laporan evaluasi berkala atas penanganan keluhan dan konsultasi.",
                                "bukti": [
                                    "Dokumen Laporan Evaluasi atas Penanganan Keluhan/Masukan dan Konsultasi Berkala"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_3c_bps",
                                "drive_folder": "3 c. EVALUASI PENANGANAN KELUHAN"
                            }
                        ]
                    },
                    {
                        "name": "iv. Penilaian Kepuasan terhadap Pelayanan",
                        "score": "0.67 / 1.00 (66.67%)",
                        "items": [
                            {
                                "code": "4.a",
                                "question": "Telah dilakukan survei kepuasan masyarakat (SKM / SKD) secara teratur",
                                "tipe": "A/B/C/D/E",
                                "kriteria": "• A: Survei Kebutuhan Data (SKD) & survei harian di PST berjalan penuh dan dilaporkan tiap triwulan\n• B/C/D/E: Sebagian",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "partial",
                                "badge": "Catatan: Update TW 4",
                                "narasi": "Survei SKD dan survei kepuasan harian telah dilakukan, menyisakan rekap triwulan IV.",
                                "catatan": "CATATAN KHUSUS: UPDATE 2025 (kurang laporan TW 4). Segera tuntaskan rekap hasil kepuasan Triwulan IV!",
                                "bukti": [
                                    "Dokumentasi kuesioner / angket kepuasan layanan PST",
                                    "Laporan Hasil Survei Kepuasan Masyarakat (SKM) Berkala",
                                    "Dokumen Laporan Pelaksanaan SKD (Survei Kebutuhan Data) 2024"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_4a_bps",
                                "drive_folder": "4 a. SURVEI KEPUASAN MASYARAKAT"
                            },
                            {
                                "code": "4.b",
                                "question": "Hasil survei kepuasan masyarakat dapat diakses secara terbuka oleh publik",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Dipublikasikan lengkap di website, laporan publikasi digital, dan papan info PST\n• b. Parsial\n• c. Tidak dipublikasikan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Publikasi Hasil Analisis SKD telah dirilis dan dapat diunduh bebas di portal BPS Selayar.",
                                "catatan": "",
                                "bukti": [
                                    "Tautan link publikasi Buku Hasil SKD 2024 di website resmi BPS Selayar",
                                    "Tangkapan layar postingan infografis Indeks Kepuasan Konsumen (IKK) di medsos"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_4b_bps",
                                "drive_folder": "4 b. PUBLIKASI HASIL SURVEI"
                            },
                            {
                                "code": "4.c",
                                "question": "Dilakukan tindak lanjut atas hasil survei kepuasan masyarakat",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Rekomendasi perbaikan SKD dituangkan dalam rencana aksi dan ditindaklanjuti 100%\n• B/C: Sebagian\n• D: Belum ada laporan tindak lanjut formal",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Belum ada dokumen laporan formal tindak lanjut rekomendasi hasil survei SKD/SKM.",
                                "catatan": "PERHATIAN: Buat Dokumen Rencana Tindak Lanjut Hasil SKD dan Bukti Realisasi Perbaikan Fasilitas/Layanan.",
                                "bukti": [
                                    "Dokumen Rencana Tindak Lanjut / Rekomendasi Hasil SKD 2024",
                                    "Dokumentasi Bukti Nyata Tindak Lanjut Perbaikan Layanan Berdasarkan Saran Konsumen"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_4c_bps",
                                "drive_folder": "4 c. TINDAK LANJUT HASIL SURVEI"
                            }
                        ]
                    },
                    {
                        "name": "v. Pemanfaatan Teknologi Informasi",
                        "score": "1.00 / 1.00 (100%)",
                        "items": [
                            {
                                "code": "5.a",
                                "question": "Telah menerapkan teknologi informasi dalam memberikan pelayanan",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: 100% layanan publik didukung sistem TI terintegrasi\n• B/C/D: Sebagian",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Layanan statistik didukung PST Online, Silastik, Romantik, portal allstat, dan inovasi Top Up Data.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumentasi Layanan PST Online, Website Resmi, Silastik, Romantik, dan Aplikasi Allstat",
                                    "Dokumentasi Pemanfaatan Inovasi 'Top Up Data'"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_5a_bps",
                                "drive_folder": "5 a. TI PELAYANAN PUBLIK"
                            },
                            {
                                "code": "5.b",
                                "question": "Telah dilakukan perbaikan secara terus menerus terhadap sarana TI pelayanan",
                                "tipe": "A/B/C",
                                "kriteria": "• a. Pembaruan data dan pemeliharaan website/aplikasi dilakukan berkala\n• b. Insidental\n• c. Tidak ada pembaruan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Website BPS Selayar diperbarui setiap rilis data statistik resmi (BRS) dan publikasi baru.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumentasi update data dan pemutakhiran informasi pada website secara berkala (Log CMS Website)",
                                    "Jadwal rilis publikasi dan Berita Resmi Statistik (BRS)"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_5c_bps",
                                "drive_folder": "5 b. PERBAIKAN TI BERKELANJUTAN"
                            },
                            {
                                "code": "5.c",
                                "question": "Telah membangun database pelayanan yang terintegrasi",
                                "tipe": "Ya/Tidak",
                                "kriteria": "• Ya: Basis data permohonan data dan konsultasi terpusat pada sistem basis data nasional\n• Tidak: Data masih terpisah-pisah",
                                "jawaban": "Ya",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Pencatatan tamu dan pemohon data terhubung langsung ke database terpusat PST Nasional.",
                                "catatan": "",
                                "bukti": [
                                    "Narasi dan skema terkait integrasi layanan pada PST dengan database tersentralisir",
                                    "Tangkapan layar backend database pengguna data"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_5b_bps",
                                "drive_folder": "5 c. DATABASE LAYANAN TERINTEGRASI"
                            }
                        ]
                    }
                ]
            },
            "reform": {
                "score": "2.50",
                "max": "5.00",
                "pct": "50.00%",
                "status": "warning",
                "groups": [
                    {
                        "name": "Reform i. Upaya dan/atau Inovasi Pelayanan Publik",
                        "score": "2.50 / 2.50 (100%)",
                        "items": [
                            {
                                "code": "R.1.a",
                                "question": "Upaya dan/atau inovasi telah mendorong perbaikan nyata pelayanan publik",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Inovasi terbukti memangkas waktu layanan dan meningkatkan kepuasan konsumen\n• B/C/D: Belum terbukti signifikan",
                                "jawaban": "A",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Lengkap",
                                "narasi": "Inovasi pelayanan mempercepat waktu pemenuhan data statistik sektoral bagi OPD Pemkab Kepulauan Selayar.",
                                "catatan": "",
                                "bukti": [
                                    "Dokumen Laporan Tahunan Pelayanan Publik Tahun 2024-2025",
                                    "Dokumen Analisis Hasil SKD 2024",
                                    "Narasi Dampak Inovasi terhadap Efisiensi Waktu Pelayanan"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_R1a_bps",
                                "drive_folder": "R1 a. DAMPAK INOVASI LAYANAN"
                            },
                            {
                                "code": "R.1.b",
                                "question": "Upaya dan/atau inovasi pada perizinan / pelayanan telah mempermudah alur layanan",
                                "tipe": "% (Persentase)",
                                "kriteria": "Persentase jenis layanan yang berhasil disederhanakan alurnya.",
                                "jawaban": "100% (2 dari 2 Layanan Dipermudah)",
                                "nilai": "1.00",
                                "status": "complete",
                                "badge": "Sempurna (100%)",
                                "narasi": "Layanan Rekomendasi Statistik (Romantik) dan Konsultasi Statistik telah disederhanakan 100% secara daring.",
                                "catatan": "",
                                "bukti": [
                                    "Narasi Komparasi Efektivitas Pelayanan Hasil Inovasi (Alur Sebelum vs Sesudah Inovasi)",
                                    "Standar Waktu Penyelesaian Layanan yang Dipercepat"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_R1b_bps",
                                "drive_folder": "R1 b. PENYEDERHANAAN ALUR LAYANAN"
                            }
                        ]
                    },
                    {
                        "name": "Reform ii. Penanganan Pengaduan Pelayanan dan Konsultasi",
                        "score": "0.00 / 2.50 (0%)",
                        "items": [
                            {
                                "code": "R.2",
                                "question": "Penanganan pengaduan pelayanan dilakukan melalui berbagai kanal / media terintegrasi",
                                "tipe": "A/B/C/D",
                                "kriteria": "• A: Penanganan aduan terintegrasi multi-kanal secara efektif dengan laporan tindak lanjut tuntas\n• B/C: Parsial\n• D: Belum terintegrasi optimal",
                                "jawaban": "D",
                                "nilai": "0.00",
                                "status": "missing",
                                "badge": "Perlu Dilengkapi",
                                "narasi": "Pengelolaan multi-kanal pengaduan pelayanan (media sosial, SP4N, kotak aduan, WA Center) belum terintegrasi ke dalam satu laporan monev komprehensif.",
                                "catatan": "PERHATIAN KRITIS: Susun Laporan Monitoring, Evaluasi, dan Tindak Lanjut Penanganan Pengaduan Multi-Kanal secara berkala.",
                                "bukti": [
                                    "Laporan Monitoring, Evaluasi, dan Tindak Lanjut Penanganan Pengaduan Multi-Kanal",
                                    "Laporan Dokumentasi Pengelolaan Media Pengaduan (Media Sosial, Website, PST, WA)"
                                ],
                                "link_contoh": "http://s.bps.go.id/PelayananPublik_Reform2_BPS",
                                "drive_folder": "R2. PENGADUAN MULTIKANAL REFORM"
                            }
                        ]
                    }
                ]
            }
        }
    ],
    "hasil": {
        "score": "0.00",
        "max": "40.00",
        "pct": "0.00%",
        "status": "waiting",
        "desc": "Komponen Hasil (Bobot 40.00) merupakan penilaian independen atas dampak pembangunan Zona Integritas. Skor saat ini masih 0.00 karena masih menunggu pelaksanaan survei eksternal oleh BPS RI dan Tim Penilai Nasional (TPN) KemenPAN-RB.",
        "sub": [
            {
                "title": "I. Birokrasi yang Bersih dan Akuntabel",
                "bobot": "22.50",
                "status": "Menunggu Survei Eksternal",
                "items": [
                    {
                        "name": "a. Nilai Survei Persepsi Korupsi (IPAK)",
                        "bobot": "17.50",
                        "status": "Belum ada nilai",
                        "target": "Minimal 3.60 / Skala 4.00 (≥ 90.00)",
                        "desc": "Diukur melalui survei persepsi korupsi terhadap pengguna layanan PST dan stakeholder BPS Kabupaten Kepulauan Selayar oleh BPS RI / KemenPANRB."
                    },
                    {
                        "name": "b. Capaian Kinerja Organisasi",
                        "bobot": "5.00",
                        "status": "Belum ada nilai",
                        "target": "Realisasi Sasaran Strategis ≥ 100%",
                        "desc": "Evaluasi terhadap efektivitas pencapaian target kinerja utama dan nilai SAKIP satuan kerja."
                    }
                ]
            },
            {
                "title": "II. Pelayanan Publik yang Prima",
                "bobot": "17.50",
                "status": "Menunggu Survei Eksternal",
                "items": [
                    {
                        "name": "a. Nilai Persepsi Kualitas Pelayanan (IPKP)",
                        "bobot": "17.50",
                        "status": "Belum ada nilai",
                        "target": "Minimal 3.60 / Skala 4.00 (≥ 90.00)",
                        "desc": "Diukur melalui survei kepuasan kualitas layanan statistik oleh tim penilai independen terhadap pengguna data BPS."
                    }
                ]
            }
        ]
    }
}

print(f"Total Areas loaded: {len(data['areas'])}")
with open('/tmp/zi_data.json', 'w') as f:
    json.dump(data, f, indent=2)
print("Data JSON saved to /tmp/zi_data.json")
