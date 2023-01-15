"""
4.2 Write a program using user define function to
print fibonacci series.
"""

def fibonacci_series(n):
    if n < 0:
        pass
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

value = int(input("Enter no : "))
if value < 0:
    exit("Invalid value!")
fibonacci_series(value)

