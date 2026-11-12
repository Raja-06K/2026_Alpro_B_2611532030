pin = input("Masukkan PIN: ") #E
correct_pin = "1234" #K
attempt = 1 #B
MAX_ATTEMPTS = 3 #H
while pin != correct_pin and attempt < MAX_ATTEMPTS: #C
    print("Incorrect PIN.") #I
    attempt += 1 #G
    pin = input("Masukkan PIN: ") #E
if pin == correct_pin: #J
    print("Access granted") #D
else: #F
    print("Account locked") #A