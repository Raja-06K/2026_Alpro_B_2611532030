# Buat file dengan nama nested_for3_nim.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit terakhir nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2030 = int(input("Masukkan nilai batas: "))
for i_2030 in range(batas_2030+1):
    for j_2030 in range(batas_2030+1):
        print(i_2030 + j_2030, end=" ")
    print() # pindah ke baris berikutnya