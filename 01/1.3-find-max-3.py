# 1.3 Write a program to find maximum and minimum from 3 entered numbers.
a = int(input("Enter first no.  : "))
b = int(input("Enter second no. : "))
c = int(input("Enter third no.  : "))

min = a
if a < b:
    if a > c:
        min = c
else:
    if b > c:
        min = c
    else:
        min = b
print(min, "is minimum")

max = a
if a > b:
    if a < c:
        max = c
elif b < c:
    max = c
else:
    max = b
print(max, "is max")
