# Name: Maharaja Korga
# NIM: 2611532030
# Question 5 (A)

username = input("Username: ")

# Urutan aman: cek panjang dulu, baru isi karakter, terakhir karakter pertama
if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")