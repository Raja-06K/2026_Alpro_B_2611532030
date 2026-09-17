# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2030 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2030 = [int(angka.strip()) for angka in input_data_2030.split(",")]

nilai_dicari_2030 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2030 = nilai_dicari_2030 in data_2030
print("\nOperator keanggotaan IN")
print(nilai_dicari_2030, "in", data_2030, "=", hasil_2030)

# Operator not in
hasil_2030 = nilai_dicari_2030 not in data_2030
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2030, "not in", data_2030, "=", hasil_2030)


print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("\n==================================")

# objek1 menggunakan list dari input pengguna
objek1_2030 = data_2030

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2030 = objek1_2030

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2030 = data_2030.copy()

# Operator is
hasil_2030 = objek1_2030 is objek2_2030
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_2030)

# Operator is not
hasil_2030 = objek1_2030 is not objek3_2030
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_2030)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai:")
print("objek1 is objek2 =", objek1_2030 is objek3_2030)
print("objek1 == objek3 =", objek1_2030 == objek3_2030)