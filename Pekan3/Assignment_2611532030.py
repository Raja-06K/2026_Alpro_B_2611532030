# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menggunakan fungsi input()
# Nilai program yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2030 = int(input("input angka-1: "))
angka2_2030 = int(input("input angka-2: "))

print("\nNilai awal angka1 =", angka1_2030)
print("\nNilai awal angka2 =", angka2_2030)

# assignment biasa
hasil = angka1_2030
print("\nOperator assignment biasa (=)")
print("hasil =", hasil)

# assignment penambahan
hasil = angka1_2030
hasil += angka2_2030
print("\nOperator assignment penambahan (+=)")
print("hasil =", hasil)

# assignment pengurangan
hasil = angka1_2030
hasil -= angka2_2030
print("\nOperator assignment pengurangan (-=)")
print("hasil =", hasil)

# assignment perkalian
hasil = angka1_2030
hasil *= angka2_2030
print("\nOperator assignment perkalian (*=)")
print("hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2030 != 0:
    hasil = angka1_2030
    hasil /= angka2_2030
    print("\nAssignment pembagian (/=)")
    print("hasil =", hasil)
    # Operator tambahan
    hasil = angka1_2030
    hasil //= angka2_2030
    print("\nAssignment pembagian bulat (//=)")
    print("hasil =", hasil)
    hasil = angka1_2030
    hasil %= angka2_2030
    print("\nAssignment sisa bagi (%=)")
    print("hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment berpangkat
hasil = angka1_2030
hasil **= angka2_2030
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)