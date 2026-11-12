# Name: Maharaja Korga
# NIM: 2611532030
# Question Bonus

sentence = input("Kalimat: ")

cleaned = sentence.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")