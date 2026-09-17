# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2030 = int(input("input angka-1: "))
angka2_2030 = int(input("input angka-2: "))

# Penjumlahan
hasil_2030 = angka1_2030 + angka2_2030
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2030)

# Pengurangan
hasil_2030 = angka1_2030 - angka2_2030
print("\nOperator Pengurangan")
print("Hasil =", hasil_2030)

# Perkalian
hasil_2030 = angka1_2030 * angka2_2030
print("\nOperator Perkalian")
print("Hasil =", hasil_2030)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2030 != 0:
    hasil_2030 = angka1_2030 / angka2_2030
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2030)

    hasil_2030 = angka1_2030 // angka2_2030
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2030)

    hasil_2030 = angka1_2030 % angka2_2030
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2030)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2030 = angka1_2030 ** angka2_2030
print("\nOperator Pangkat")
print("Hasil =", hasil_2030)