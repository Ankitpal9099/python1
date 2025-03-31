#  Write a Python program to show method overriding. 

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"
dog = Dog()
cat = Cat()
print(dog.speak())  
print(cat.speak())  
animal = Animal()
print(animal.speak()) 