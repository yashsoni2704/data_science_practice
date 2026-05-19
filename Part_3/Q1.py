n = input("Enter a string: ")

rev = ""
for ch in n:
    rev = ch + rev
if n == rev:
    print("It is palindrome")
else:
    print("No,It's not")