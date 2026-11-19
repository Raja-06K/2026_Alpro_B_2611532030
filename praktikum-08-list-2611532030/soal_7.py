menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        qty = int(input(f"Day {day}, {menu}: "))
        row.append(qty)
    sales.append(row)

print("Total per day:")
for day_idx in range(number_of_days):
    day_total = 0
    for menu_idx in range(len(menus)):
        day_total += sales[day_idx][menu_idx]
    print(f"Day {day_idx + 1}: {day_total}")

menu_totals = []
for menu_idx in range(len(menus)):
    menu_total = 0
    for day_idx in range(number_of_days):
        menu_total += sales[day_idx][menu_idx]
    menu_totals.append((menus[menu_idx], menu_total))

print(f"Total per menu: {menu_totals}")

best_name = ""
best_total = -1

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")