print("*-*-*-*- Multiplication Table Calculator -*-*-*-*")
number = int(input("Please enter a number from 1 to 10 = "))

multiplier = 1

while multiplier <= 10:
    result = number * multiplier
    print(number, "x", multiplier, "=", result)
    multiplier += 1