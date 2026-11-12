# Name: Maharaja Korga
# NIM: 2611532030
# Question 6

full_name = "  Siti Aisyah  "
nim = "2610511023"

# Build the username: first name in lowercase + last 3 digits of the NIM.
clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)