# 3.2 Write a program to learn different types of structures (list, dictionary, tuple) in python. Display all information of student.

print("List :-")
studentList = ["Jay Parmar", "B.tech", "CE"]
print("Before :", studentList)
studentList.append(2112028)
studentList.insert(1, 52)
print("After :", studentList)

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
