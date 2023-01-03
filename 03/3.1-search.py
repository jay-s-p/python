# 3.1 Write a program to perform searching and sorting in given list.

# Searching

list = ["Jay", "Harshad", "Dhruv", "Mohit", 1, 2, 4, 5, 6]

pos = -1
a = input("Enter value : ")
for i in range(0, len(list)):
    if a == str(list[i]):
        pos = i

if pos == -1:
    print(a, "is not found")
else:
    print(a, "is found at ", pos + 1, "position.")