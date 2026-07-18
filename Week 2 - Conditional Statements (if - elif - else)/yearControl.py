print("*-*-*-*- Year Calculator -*-*-*-*")

userYear = int(input("Please enter the year you want to check = "))

if userYear % 400 == 0:
    print(f"{userYear} is a leap year.")

elif userYear % 100 == 0:
    print(f"{userYear} is not a leap year.")

elif userYear % 4 == 0:
    print(f"{userYear} is a leap year.")

else:
    print(f"{userYear} is not a leap year.")