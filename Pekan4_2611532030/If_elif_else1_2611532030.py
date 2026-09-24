# Buat file dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit terakhir nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2030 = int(input("Input umur anda: "))
sim_2030 = input("Apakah anda sudah punya SIM C: ")[0]

if umur_2030 >= 17 and sim_2030 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_2030 >= 17 and sim_2030 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2030 < 17 and sim_2030 == 'y':
        print("Anda belum cukup umur punya SIM")
else:
     print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")