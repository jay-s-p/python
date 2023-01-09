# 1.1 Write a program to check entered number is even-odd.

a = int(input("Enter no. : "))
if a == 0:
    print("Invalid value")
elif a % 2 == 0:
    print(a, "is even.")
else:
    print(a, "is odd.")
