schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

hari_terbanyak = ""
jumlah_terbanyak = 0

for hari in schedule:
    jumlah = len(schedule[hari])
    if jumlah > jumlah_terbanyak:
        jumlah_terbanyak = jumlah
        hari_terbanyak = hari

print(f"Busiest day: {hari_terbanyak} ({jumlah_terbanyak} courses)")

matkul = input("masukkan mata kuliah: ").strip()
total_hari = 0

for hari in schedule:
    if matkul in schedule[hari]:
        total_hari = total_hari + 1

print(f"{matkul}: {total_hari} days")