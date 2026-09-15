# Kode program tugas "tugas2_2611532030.py"

from typing import Final

# Konstanta batas kelulusan
BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_2030 = input("Masukkan Nama Mahasiswa\t\t: ")
jenis_kelamin_2030 = input("Masukkan Jenis Kelamin (L/P)\t: ")
umur_2030 = int(input("Masukkan Umur\t\t\t: "))
skor_tes_2030 = float(input("Masukkan Skor Tes Awal\t\t: "))

# Deklarasi alamat secara multiline
alamat_2030 = """Jl. M. Yatim No. 31, 
Kecamatan Kuranji, Kelurahan Lubuk Lintah,
Kota Padang"""

# Token identifikasi menggunakan bilangan kompleks
token_2030 = 100+3j

# Evaluasi status kelulusan
status_lulus_2030 = skor_tes_2030 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa\t:", nama_2030, "| Tipe:", type(nama_2030))
print("Jenis Kelamin\t:", jenis_kelamin_2030, "| Tipe:", type(jenis_kelamin_2030))
print("Alamat Domisili\t:\n" + alamat_2030, "\n| Tipe:", type(alamat_2030))
print("Umur\t\t:", umur_2030, "tahun | Tipe:", type(umur_2030))
print("Skor Tes Awal\t:", skor_tes_2030, "| Tipe:", type(skor_tes_2030))
print("ID Token Sinyal\t:", token_2030, "| Tipe:", type(token_2030))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", status_lulus_2030, "| Tipe:", type(status_lulus_2030))