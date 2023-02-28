"""
Write a program to create a file of random
numbers then separate even and odd numbers
in separate file.
"""

try:
    numbers = open("./numbers.txt", "w")
    for i in range(5):
        numbers.write(input("Enter value : ") + " ")
except Exception as e:
    print("ERROR :", e)
finally:
    numbers.close()

try:
    numbers = open("./numbers.txt", "r")
    odd = open("./odd.txt", "w")
    even = open("./even.txt", "w")
    # print(numbers.read())
    # print(str(numbers.read()).split(" "))
    for i in numbers.read().split():
        if i == "":
            continue
        elif int(i) % 2 == 0:
            even.write(i+" ")
        else:
            odd.write(i+" ")

except Exception as e:
    print("ERROR :", e)
finally:
    numbers.close()
    odd.close()
    even.close()
