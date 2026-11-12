# Name: Maharaja Korga
# NIM: 2611532030
# Question 5 (B)

NIM = input("NIM: ")

if len(NIM) == 10 and NIM.isdigit():
    print("Valid, intake year 20" + NIM[:2])
else:
    print("Invalid NIM")