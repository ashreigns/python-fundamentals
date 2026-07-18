def find_gcd(num1, num2):
    # We find whichever number is smaller because the greatest common divisor cannot be larger than the smaller number
    if num1 < num2:
        smaller_num = num1
    else:
        smaller_num = num2
    # We try decreasing backwards starting from the smaller number down to 1
    for i in range(smaller_num, 0, -1):
        # If the number i divides both num1 and num2 with no remainder (i.e. remainder is 0)
        if num1 % i == 0 and num2 % i == 0:
            return i  # The moment we find the common divisor, we end the function and pass it to the gcd variable

def find_lcm(num1, num2, gcd_value):
    # Mathematical rule = Dividing the product of two numbers by their GCD gives the LCM
    # We use integer division // so that no decimal remainder appears in the division process
    return (num1 * num2) // gcd_value

print("*-*-*-* GCD & LCM Calculator *-*-*-*")
s1 = int(input("Please enter the first number = "))
s2 = int(input("Please enter the second number = "))

gcd = find_gcd(s1, s2)
lcm = find_lcm(s1, s2, gcd)

print(f"GCD = {gcd}")
print(f"LCM = {lcm}")