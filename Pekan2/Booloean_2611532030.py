# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data boolean
is_lulus_2030 = True
is_cumlaude_2030 = True

#Menggunakan Booloean
nilai_2030 = 85
batas_lulus_2030 = 75

#Menentukan nilai Boolean dari kondisi
status_kelulusan_2030 = nilai_2030 >= batas_lulus_2030 #Hasilnya akan True

print("=== Check Kelulusan===")
print("Nilai:", nilai_2030)
print("Apakah Lulus?:", status_kelulusan_2030)
if is_lulus_2030 and is_cumlaude_2030:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")