# tugas3_2611532030.py
# Sistem Simulasi Transaksi dan Validasi Akses Toko

print("=== SISTEM TRANSAKSI TOKO ===\n")

# 1. INPUT DATA PELANGGAN & TRANSAKSI
nama_2030 = input("Masukkan Nama Pelanggan : ")
status_2030 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_2030 = float(input("Masukkan Total Belanja : "))
jumlah_2030 = int(input("Masukkan Jumlah Barang : "))
promo_2030 = input("Masukkan Kode Promo : ")

# Daftar kode promo yang tersedia di toko
daftar_promo_2030 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# 2. OPERATOR PERBANDINGAN
syarat_belanja_2030 = total_2030 >= 200000
syarat_barang_2030 = jumlah_2030 >= 3
is_member_2030 = status_2030.lower() == "member"

# 3. OPERATOR LOGIKA
diskon_member_2030 = is_member_2030 and syarat_belanja_2030
dapat_promo_2030 = (is_member_2030 and syarat_belanja_2030) or syarat_barang_2030
bukan_member_2030 = not is_member_2030

# 4. OPERATOR KEANGGOTAAN (in / not in)
promo_tersedia_2030 = promo_2030 in daftar_promo_2030
promo_tidak_tersedia_2030 = promo_2030 not in daftar_promo_2030

# 5. OPERATOR ARITMATIKA
if diskon_member_2030 or dapat_promo_2030:
    diskon_2030 = total_2030 * 0.1
else:
    diskon_2030 = 0.0

bayar_2030 = total_2030 - diskon_2030
rata_2030 = bayar_2030 / jumlah_2030
sisa_barang_2030 = jumlah_2030 % 2

# 6. OPERATOR PENUGASAN (assignment)
poin_2030 = 0
poin_2030 += jumlah_2030
if dapat_promo_2030:
    poin_2030 *= 2
bayar_2030 -= 0

# 7. OPERATOR IDENTITAS (is / is not)
objek1_2030 = ["status", is_member_2030]
objek2_2030 = ["status", is_member_2030]
objek3_2030 = objek1_2030
identitas_sama_2030 = objek1_2030 is objek3_2030
identitas_beda_2030 = objek1_2030 is not objek2_2030
nilai_sama_2030 = objek1_2030 == objek2_2030

# 8. OPERATOR BITWISE
bit_member_2030   = 0b0001 if is_member_2030 else 0b0000
bit_belanja_2030  = 0b0010 if syarat_belanja_2030 else 0b0000
bit_barang_2030   = 0b0100 if syarat_barang_2030 else 0b0000
bit_promo_2030    = 0b1000 if promo_tersedia_2030 else 0b0000

# OR (|) -> menggabungkan seluruh kondisi menjadi satu kode status
kode_status_2030 = bit_member_2030 | bit_belanja_2030 | bit_barang_2030 | bit_promo_2030

# AND (&) -> memeriksa apakah bit tertentu aktif
cek_member_2030 = kode_status_2030 & 0b0001
cek_promo_2030  = kode_status_2030 & 0b1000

# XOR (^) -> membandingkan perbedaan status dengan kode referensi
kode_referensi_2030 = 0b1011
selisih_status_2030 = kode_status_2030 ^ kode_referensi_2030

# Shift kiri (<<) -> contoh tambahan operator bitwise
geser_status_2030 = kode_status_2030 << 1

# Hak akses berdasarkan hasil bitwise
member_access_2030 = bool(cek_member_2030)
promo_access_2030 = bool(cek_promo_2030)
free_shipping_access_2030 = (promo_2030 == "GRATISONGKIR") and promo_tersedia_2030

# OUTPUT PROGRAM
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_2030}")
print(f"Status Pelanggan     : {status_2030}")
print(f"Total Belanja        : Rp{total_2030:.0f}")
print(f"Jumlah Barang        : {jumlah_2030}")
print(f"Kode Promo           : {promo_2030}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_belanja_2030}")
print(f"Jumlah Barang >= 3         : {syarat_barang_2030}")
print(f"Status Member              : {is_member_2030}")
print(f"Kode Promo Tersedia        : {promo_tersedia_2030}")
print(f"Mendapatkan Diskon Member  : {diskon_member_2030}")
print(f"Mendapatkan Promo          : {dapat_promo_2030}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : Rp{diskon_2030:.0f}")
print(f"Total Pembayaran           : Rp{bayar_2030:.0f}")
print(f"Rata-rata Harga Barang     : Rp{rata_2030:.0f}")
print(f"Sisa Bagi Jumlah Barang %2 : {sisa_barang_2030}")
print(f"Poin Pelanggan             : {poin_2030}")

print("\n=== OPERATOR IDENTITAS ===")
print(f"objek1 is objek3 (sama)     : {identitas_sama_2030}")
print(f"objek1 is not objek2 (beda) : {identitas_beda_2030}")
print(f"objek1 == objek2 (nilai)    : {nilai_sama_2030}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Status (biner)  : {bin(kode_status_2030)}")
print(f"Kode Status (desimal): {kode_status_2030}")
print(f"Member Access        : {member_access_2030}")
print(f"Promo Access         : {promo_access_2030}")
print(f"Free Shipping Access : {free_shipping_access_2030}")

print("\n=== OPERASI BITWISE ===")
print(f"Cek Member  -> {bin(kode_status_2030)} & 0001 = {bin(cek_member_2030)} ({cek_member_2030})")
print(f"Cek Promo   -> {bin(kode_status_2030)} & 1000 = {bin(cek_promo_2030)} ({cek_promo_2030})")
print(f"XOR Ref     -> {bin(kode_status_2030)} ^ {bin(kode_referensi_2030)} = {bin(selisih_status_2030)} ({selisih_status_2030})")
print(f"Shift Kiri  -> {bin(kode_status_2030)} << 1 = {bin(geser_status_2030)} ({geser_status_2030})")

print("\n=== SELESAI ===")