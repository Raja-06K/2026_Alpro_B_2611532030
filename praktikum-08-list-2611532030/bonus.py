number_of_rows = 4
seats_per_row = 5
# Write your code below

# Membuat denah 4 baris x 5 kursi dengan list terpisah di tiap baris
hall = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]

while True:
    for r in range(number_of_rows):
        print(f"Row {r + 1}: {' '.join(hall[r])}")

    row_input = int(input("Row (0 to stop): "))
    if row_input == 0:
        break

    seat_input = int(input("Seat: "))

    if row_input < 1 or row_input > number_of_rows or seat_input < 1 or seat_input > seats_per_row:
        print("Invalid seat.")
    elif hall[row_input - 1][seat_input - 1] == "X":
        print("Seat already taken.")
    else:
        hall[row_input - 1][seat_input - 1] = "X"
        print("Seat booked.")

taken_count = 0
for row in hall:
    for seat in row:
        if seat == "X":
            taken_count += 1

print(f"Seats taken: {taken_count}")