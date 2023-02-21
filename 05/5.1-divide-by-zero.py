"""
Handle divide by zero exception.
"""

try:
    x = int(input("Enter first  no. : "))
    y = int(input("Enter second no. : "))
    z = x / y
except ZeroDivisionError:
    print("Division by zero error!")
except:
    print("An error occurred!")
else:
    print(x, "/", y, "=", z)
