a = 0
b = 1
counter = 0

while counter < 20:
    print(a)
    total = a + b
    a = b
    b = total
    counter += 1