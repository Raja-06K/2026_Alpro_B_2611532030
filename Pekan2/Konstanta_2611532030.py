# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2030 = float(input('Masukkan nilai jari-jari: '))
luas_2030 = PI * jari_2030 * jari_2030
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2030, luas_2030))