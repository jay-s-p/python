"""
1.3 Write a program to find maximum and minimum from 3 entered numbers.
"""
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

min = max = a
for i in [a, b, c]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min, "is min")
print(max, "is max")
