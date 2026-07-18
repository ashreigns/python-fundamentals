print("*-*-*-*-*- Triangle Perimeter and Area Calculator -*-*-*-*-*")

side1 = int(input("side1 = "))
side2 = int(input("side2 = "))
side3 = int(input("side3 = "))

perimeter = side1 + side2 + side3

a = perimeter / 2

area = (a * (a - side1) * (a - side2) * (a - side3)) ** 0.5

print(f"Perimeter of the triangle = {perimeter} Area of the triangle = {area}")