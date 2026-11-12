# Name: Maharaja Korga
# NIM: 2611532030
# Question 3 (B)

text = "Maharaja Korga"
count = 0
for char in text:
    if char in "aiueo":
        count += 1
    if char in "AIUEO":
        count += 1
print("Vowels:", count)