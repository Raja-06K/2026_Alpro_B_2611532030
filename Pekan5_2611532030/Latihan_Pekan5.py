# Tugas5 Buatlah program untuk menampilkan output segitiga bintang menggunakan perulangan for
tinggi_2030 = int(input("Masukkan tinggi segitiga: "))

for i_2030 in range(1, tinggi_2030 + 1):
    print(" " * (tinggi_2030 - i_2030), end="")

    for j_2030 in range(i_2030):
        print("*", end=" ")
    print()