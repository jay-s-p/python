"""
4.1 Write a program using user define function to
print factorial series.
"""


def factorial_iterative(value):
    fact = 1
    while value > 1:
        fact *= value
        value -= 1
    return fact


def factorial_recursion(value):
    return 1 if (value == 0 or value == 1) else value * factorial_recursion(value - 1)


value = int(input("Enter no : "))
if value < 0:
    exit("Invalid value!")
for i in range(0, value + 1):
    ans = factorial_recursion(i)
    print(i, ans if (ans != -1) else "Invalid value")