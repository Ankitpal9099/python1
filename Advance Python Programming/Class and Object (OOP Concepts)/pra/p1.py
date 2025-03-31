#  Write a Python program to create a class and access the properties
# of the class using an object. 

class abc:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")
            
abc1=abc("ankit",22,"male")
abc1.display()
abc2=abc("raj",22,"male")
abc2.display()
            
