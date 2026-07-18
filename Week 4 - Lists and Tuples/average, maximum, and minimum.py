print("*-*-*-*- Average, Largest, and Smallest Calculator -*-*-*-*")

numbers = []
counter = 0

while counter < 10:
    entered_number = int(input("Please enter a number = "))
    numbers.append(entered_number)
    counter += 1

largest = max(numbers) # selects the largest of all the numbers entered by the user
smallest = min(numbers) # selects the smallest of all the numbers entered by the user
average = sum(numbers) / 10 # here, sum adds up all the numbers and divides by 10 to find the average as a result

print("All numbers entered = ", numbers)
print("Largest number = ", largest)
print("Smallest number = ", smallest)
print("Average of all numbers = ", average)