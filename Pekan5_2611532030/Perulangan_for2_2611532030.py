# Buat file dengan nama perulangan_for2_nim.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit terakhir nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2030 = int(input("Inputkan angka: "))
print("Perulangan ke-0 sampai ke-", ulang_2030-1)
for i_2030 in range(ulang_2030):
    print(i_2030, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_2030)
for i_2030 in range(1, ulang_2030 + 1):
    print(i_2030, end=" ")