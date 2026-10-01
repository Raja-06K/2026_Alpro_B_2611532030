# Buat file dengan nama nested_for4_nim.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit terakhir nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2030 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2030 % 2 != 0:
    print("Tinggi pola harus bilangan genap!")
else:
    a_2030 = tinggi_2030
    c_2030 = a_2030
    lebar_2030 = (2 * tinggi_2030) - 2

    for i_2030 in range(1, tinggi_2030 + 1):
        b_2030 = c_2030 + 1

        for j_2030 in range(1, lebar_2030 + 1):

            # Baris atas dan bawah
            if i_2030 == 1 or i_2030 == tinggi_2030:
                if j_2030 == 1 or j_2030 == lebar_2030:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_2030 == 1 or j_2030 == lebar_2030:
                    print("|", end="")
                else:
                    if j_2030 == c_2030:
                        print("<", end="")
                    elif j_2030 == b_2030:
                        print(">", end="")
                    elif j_2030 == (lebar_2030 - c_2030):
                        print("<", end="")
                    elif j_2030 == (lebar_2030 - c_2030 + 1):
                        print(">", end="")
                    elif j_2030 > b_2030 and j_2030 < (lebar_2030 - c_2030 + 1):
                        print(".", end="")
                    else:
                        print(" ", end="")
        
        print()

        # Logika asli java
        a_2030 -= 2

        if a_2030 <= 0:
            c_2030 = (-a_2030) + 2
        else:
            c_2030 = a_2030