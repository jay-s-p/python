"""
Handle any user define exception.
"""

class AgeException(Exception):
    def __init__(self):
        super()

try:
    age = int(input("Enter your age : "))
    if age < 18:
        raise AgeException
except AgeException:
    print("You are not eligible to vote :(")
except Exception:
    print("An error occurred!")
else:
    print("You are eligible to vote :)")
