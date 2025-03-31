# • Write a Python program to create a class and access its properties using an object

class abc:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name:{self.name}")
        print(f"age{self.age}")
        
abc1=abc("John",25)
abc1.display()
abc2=abc("Doe",30)
abc2.display()
abc3=abc("Smith",35)
abc3.display()
        