# 12) Write a Python program to demonstrate the use of local and
# global variables in a class.

class abc:
    def __init__(self):
        self.name="John"
        self.age=25
    def display(self):
        print(f"name:{self.name}")
        print(f"age{self.age}")
        x=10
        print(f"Local variable x:{x}")
        self.x=10
        print(f"Global variable x:{self.x}")
abc=abc()
abc.display()