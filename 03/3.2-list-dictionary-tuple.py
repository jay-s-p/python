# 3.2 Write a program to learn different types of structures (list, dictionary, tuple) in python. Display all information of student.

print("List :-")
numbers = [0, 123, 1, 2, 3, 4]
print("Before :", numbers)
numbers.pop(1)  # remove element at specified index
numbers.append(5)  # Add element to the end
print("After :", numbers)

print("\nDictionary :-")
students = {"name": "Jay", "age": 20, "roll_no": 52, "gender": "Male"}
print("Before :", students)
students.pop("age")
students.popitem()
print("After :", students)

print("\nTuple :-")
numbers = (5, 2, 5, 9, 1, 6, 3, 5)
print("numbers :", numbers)
print("numbers.count(5) :", numbers.count(5))
print("numbers.index(3) :", numbers.index(3))
