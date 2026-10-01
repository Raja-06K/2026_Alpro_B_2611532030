# Buat file dengan nama jumlah_genap_nim.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit terakhir nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2030 = int(input("Masukkan nilai batas: "))

jumlah_2030 = 0
for i_2030 in range(1, ulang_2030 + 1):
    if i_2030 % 2 == 0:
        print(i_2030, end=" ")
        jumlah_2030 = jumlah_2030 + i_2030

        if i_2030 < ulang_2030:
            print("+", end=" ")
        else:
            print("= ", jumlah_2030, end=" ")
print()
print("Jumlah =", jumlah_2030)