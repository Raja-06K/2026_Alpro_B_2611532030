# Name: Maharaja Korga
# NIM: 2611532030
# Question 4

phone = "082611532030"
bintang = len(phone) - 7
masked = phone[:4] + ("*" * bintang) + phone[-3:]
print(masked)