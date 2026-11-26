n = int(input("Masukkan jumlah data: "))
kas = {}

for i in range(n):
    nama, nominal = input("Masukkan nama dan nominal: ").split()
    nominal = int(nominal)
    kas[nama] = kas.get(nama, 0) + nominal

for nama, total in kas.items():
    print(f"{nama}: {total}")

print(f"Total cash: {sum(kas.values())}")

top = max(kas, key=kas.get)
print(f"Top contributor: {top} ({kas[top]//1000}K)")