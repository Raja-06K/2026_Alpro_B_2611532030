# 1. Baca kedua baris input, lalu pecah masing-masing dengan split()
daftar_kelas = input().split()
daftar_pengumpul = input().split()

# 2. Gunakan set untuk membuang nomor ganda, lalu hitung jumlah yang sudah mengumpulkan
set_kelas = set(daftar_kelas)
set_pengumpul = set(daftar_pengumpul)

jumlah_submitted = len(set_pengumpul)

# 3. Gunakan operasi set (selisih / difference) untuk menghitung jumlah yang belum mengumpulkan
belum_mengumpulkan = set_kelas - set_pengumpul
jumlah_not_submitted = len(belum_mengumpulkan)

# Cetak ringkasan sesuai format output
print(f"Submitted: {jumlah_submitted} students")
print(f"Not submitted: {jumlah_not_submitted} students")

# 4. Telusuri daftar kelas dari depan. Cetak nomor yang tidak ada di set pengumpul
for nomor in daftar_kelas:
    if nomor not in set_pengumpul:
        print(nomor)
