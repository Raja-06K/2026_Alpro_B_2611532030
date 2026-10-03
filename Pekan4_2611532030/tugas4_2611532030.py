# Nama File : tugas4_2611532030.py
# Nama/NIM  : Maharaja Korga / 2611532030
# Tugas 4   : Struktur Percabangan pada Python (if, if-else, if-elif-else, multi-if, match-case)

import sys

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung & String Handling
nama_2030 = input("Masukkan Nama Pengunjung          : ")
umur_2030 = int(input("Input umur anda                  : "))
input_sim_2030 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
sim_2030 = input_sim_2030[0] if input_sim_2030 else 't'

# 2. Pemilihan Wahana Menggunakan match-case
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_2030 = int(input("Masukkan nomor paket (1-5)      : "))

match paket_2030:
    case 1:
        nama_paket_2030 = "Wahana Safari Rimba"
        harga_satuan_2030 = 50000
    case 2:
        nama_paket_2030 = "Wahana Arung Jeram"
        harga_satuan_2030 = 75000
    case 3:
        nama_paket_2030 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2030 = 120000
    case 4:
        nama_paket_2030 = "Wahana Roller Coaster Kilat"
        harga_satuan_2030 = 100000
    case 5:
        nama_paket_2030 = "Wahana All-Access VIP"
        harga_satuan_2030 = 220000
    case _:
        print("\nPaket wahana tidak valid!")
        sys.exit()

jumlah_tiket_2030 = int(input("Masukkan jumlah tiket            : "))

# Validation if-tunggal untuk jumlah tiket
if jumlah_tiket_2030 <= 0:
    print("\nPeringatan: Kuota tiket tidak valid!")
    sys.exit()

input_member_2030 = input("Apakah Anda member? (y/t)        : ").strip().lower()
input_promo_2030 = input("Apakah kode promo valid? (y/t)   : ").strip().lower()

# 3. Validasi Izin Kendali Wahana Menggunakan if-elif-else dan Operator Logika
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_2030 == 3:
    if umur_2030 >= 17 and sim_2030 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_2030 >= 17 and sim_2030 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_2030 < 17 and sim_2030 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_2030 >= 10:
        print("Status Akses: Pengunjung memenuhi kriteria usia minimal untuk wahana ini.")
    else:
        print("Status Akses: Pengunjung belum cukup umur (wajib didampingi orang tua).")

# 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
subtotal_2030 = harga_satuan_2030 * jumlah_tiket_2030
total_diskon_persen_2030 = 0

if subtotal_2030 >= 200000:
    total_diskon_persen_2030 += 10

if input_member_2030 in ['y', 'ya']:
    total_diskon_persen_2030 += 5

if input_promo_2030 in ['y', 'ya']:
    total_diskon_persen_2030 += 15

if jumlah_tiket_2030 >= 5:
    total_diskon_persen_2030 += 5

nominal_diskon_2030 = subtotal_2030 * (total_diskon_persen_2030 / 100)
total_bayar_2030 = subtotal_2030 - nominal_diskon_2030

# 5. Evaluasi Kelulusan Audit Menggunakan if-else & Print Output
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_2030:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_2030}% (Rp {nominal_diskon_2030:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_2030:,.0f}")

if total_bayar_2030 > 300000:
    print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan  : Terima kasih telah berkunjung.")

print("Program Selesai")