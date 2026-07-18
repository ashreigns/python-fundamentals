num1 = int(input("Please enter the 1st number = "))
num2 = int(input("Please enter the 2nd number = "))
num3 = int(input("Please enter the 3rd number = "))

# if num1 > num2 and num1 > num3:
#     print(f"Largest number = {num1}")
# elif num2 > num3 and num2 > num3:
#     print(f"Largest number = {num2}")
# elif num3 > num1 and num3 > num2:
#     print(f"Largest number = {num3}")
#
# if num1 < num2 and num1 < num3:
#     print(f"Smallest number = {num1}")
# elif num2 < num3 and num2 < num3:
#     print(f"Smallest number = {num2}")
# elif num3 < num1 and num3 < num2:
#     print(f"Smallest number = {num3}")

# We find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Here we find the smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print(f"Out of the 3 numbers entered, the largest is = {largest}, and the smallest is = {smallest}")