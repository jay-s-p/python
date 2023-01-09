# 1.3 Write a program to find maximum and minimum from 3 entered numbers.
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

min = a
if a < b:
    if a > c:
        min = c
else:
    if b > c:
        min = c
    else:
        min = b

max = a
if a > b:
    if a < c:
        max = c
elif b < c:
    max = c
else:
    max = b
print(min, "is min")
print(max, "is max")
