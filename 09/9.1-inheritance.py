"""
Write a program to demonstrate use of inheritance by using simple example.
"""


class Animal:
    def showAnimal(self, name):
        print("Animal is", name)

class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
class Cat(Animal):
    def meows(self):
        print("Cat meows")
        
dog = Dog()
dog.showAnimal("Dog")
dog.bark()

cat = Cat()
cat.showAnimal("Cat")
cat.meows()