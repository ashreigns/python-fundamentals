print("*-*-*-*- Password Validator -*-*-*-*")
password = input("Enter your password = ")

hasUppercase = False
hasDigit = False
charCounter = 0

for char in password:
    charCounter = charCounter + 1
    if "A" <= char <= "Z":
        hasUppercase = True
    elif "0" <= char <= "9":
        hasDigit = True

if charCounter < 8:
    print("Password must be at least 8 characters long.")
elif hasUppercase == False:
    print("Password must contain at least one uppercase letter.")
elif hasDigit == False:
    print("Password must contain at least one digit.")
else:
    print("Password saved.")