LAST_DIGIT = 0  
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for day in range(1, 8):
    amount = int(input(f"Day {day}: "))
    expenses.append(amount)

total = 0
highest_value = expenses[0]
highest_day = 1
days_above_limit = 0

for index in range(len(expenses)):
    value = expenses[index]
    day_num = index + 1

    total += value

    if value > highest_value:
        highest_value = value
        highest_day = day_num

    if value > daily_limit:
        days_above_limit += 1

average = total / len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_value})")
print(f"Days above limit: {days_above_limit}")