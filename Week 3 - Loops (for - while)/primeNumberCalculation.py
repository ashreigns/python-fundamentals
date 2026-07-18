print("*-*-*-*- Prime Number Checker -*-*-*-*")
number = int(input("Enter the number you want to check = "))

divisor = 2
isPrime = True

while divisor < number:
    if number % divisor == 0:
        isPrime = False
    divisor = divisor + 1

if number <= 1:
    print("The number is not prime.")
elif isPrime == True:
    print("The number is prime.")
else:
    print("The number is not prime.")