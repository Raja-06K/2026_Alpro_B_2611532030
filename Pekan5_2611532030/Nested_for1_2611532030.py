# Buat file dengan nama nested_for1_nim.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit terakhir nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2030 = int(input("Masukkan nilai batas: "))
for line_2030 in range(1, batas_2030 + 1):
    for j_2030 in range(1, (-1 * line_2030 + batas_2030) + 1):
        print(".", end="")
    print(line_2030)