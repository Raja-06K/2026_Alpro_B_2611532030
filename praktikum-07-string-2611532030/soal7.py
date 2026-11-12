# Name: Maharaja Korga
# NIM: 2611532030
# Question 7

name = "maharaja korga"
nim = "2611532030"

space = name.find(" ")
if space == -1:
    first = name
else:
    first = name[:space]
username = first + nim[-3:]

intake = nim[:4]

line = "=" * 30
print(line)
print("STUDENT CARD".center(30))
print(line)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print(line)