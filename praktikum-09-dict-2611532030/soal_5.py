n_2030 = int(input())
kas_2030 = {}

for i_2030 in range(n_2030):
    nama_2030, nominal_2030 = input().split()
    nominal_2030 = int(nominal_2030)
    kas_2030[nama_2030] = kas_2030.get(nama_2030, 0) + nominal_2030

for nama_2030, total_2030 in kas_2030.items():
    print(f"{nama_2030}: {total_2030}")

print(f"Total cash: {sum(kas_2030.values())}")

top_2030 = max(kas_2030, key=kas_2030.get)
print(f"Top contributor: {top_2030} ({kas_2030[top_2030]})")