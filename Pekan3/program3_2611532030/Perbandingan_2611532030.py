# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit terakhir nim contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2030 = int(input("input angka-1: "))
angka2_2030 = int(input("input angka-2: "))

# Lebih besar dari
hasil_2030 = angka1_2030 > angka2_2030
print("\nOperator Lebih Besar Dari")
print("angka1_2030 > angka2_2030 =", hasil_2030)

# Lebih kecil dari
hasil_2030 = angka1_2030 < angka2_2030
print("\nOperator Lebih Kecil Dari")
print("angka1_2030 < angka2_2030 =", hasil_2030)

# Lebih besar dari atau sama dengan
hasil_2030 = angka1_2030 >= angka2_2030
print("\nOperator Lebih Besar Dari atau Sama Dengan")
print("angka1_2030 >= angka2_2030 =", hasil_2030)

# Lebih kecil dari atau sama dengan
hasil_2030 = angka1_2030 <= angka2_2030
print("\nOperator Lebih Kecil Dari atau Sama Dengan")
print("angka1_2030 <= angka2_2030 =", hasil_2030)

# Sama dengan
hasil_2030 = angka1_2030 == angka2_2030
print("\nOperator Sama Dengan")
print("angka1_2030 == angka2_2030 =", hasil_2030)

# Tidak sama dengan
hasil_2030 = angka1_2030 != angka2_2030 
print("\nOperator Tidak Sama Dengan")
print("angka1_2030 != angka2_2030 =", hasil_2030)

# Tambahan: perbandingan berantai dalam Python
hasil_2030 = 0 < angka1_2030 < 100
print("\nOperator Perbandingan Berantai")
print("0 < angka1_2030 < 100 =", hasil_2030)

hasil_2030 = 0 < angka2_2030 < 100
print("0 < angka2_2030 < 100 =", hasil_2030)