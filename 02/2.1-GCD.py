"""
2.1 Write a program to find GCD of two numbers.
"""
# Greatest Common Divisor
# Highest Common Factor

cd = 0
a = int(input("Enter a : "))
b = int(input("Enter b : "))

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        cd = i

print("GCD is", cd)