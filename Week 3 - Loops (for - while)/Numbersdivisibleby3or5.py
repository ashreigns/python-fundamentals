total = 0
number = 1

while number <= 100:
    if number % 3 == 0 or number % 5 == 0:
        total = total + number
    number = number + 1

print(f"The sum of all numbers divisible by 3 or 5 = {total}")