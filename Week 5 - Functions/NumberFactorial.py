def calculate_factorial(number):
    result = 1  # We start with 1 because it is the identity element in multiplication

    # It creates a sequence of numbers starting from the given number and going backwards down to 1
    # For example, if the number is 5, this sequence will go [5, 4, 3, 2, 1]
    for i in range(number, 0, -1): # Goes backwards from the entered number (for instance, 5) down to 1
        result = result * i  # Multiplies the old accumulated value by the new incoming number and updates it
    return result  # When the loop finishes, we return the final accumulated product value

print("*-*-*-*- Factorial Calculator -*-*-*-*")
entered_number = int(input("Please enter the number you want to calculate the factorial of = "))

calculated_value = calculate_factorial(entered_number)
print(calculated_value)