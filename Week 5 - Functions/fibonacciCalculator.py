def fibonacci_loop(n):
    # If n is 0 or 1, we directly return it
    if n <= 1:
        return n
    # We start by putting the first two elements into variables
    previous = 0
    current = 1
    # We move forward by adding them up with a loop
    for _ in range(2, n + 1):
        temp = previous + current
        previous = current
        current = temp
    return current

position = int(input("Which element of the Fibonacci sequence do you want? = "))

result = fibonacci_loop(position)

print(result)