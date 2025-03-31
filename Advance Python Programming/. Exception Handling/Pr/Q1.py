#  7) Write a Python program to handle exceptions in a calculator.

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    while True:
        choice=input("Enter choice: ")
        if choice=='5':
            print("Exiting the calculator... Goodbye!")
            break
        if choice in ['1','2','3','4']:
            num1=get_number("Enter first number: ")
            num2=get_number("Enter second number: ")
            if choice=='1':
                print(f"Result: {num1} + {num2} = {add(num1,num2)}")
            elif choice=='2':
                print(f"Result: {num1} - {num2} = {sub(num1
                ,num2)}")   
            elif choice=='3':
                print(f"Result: {num1} * {num2} = {mul(num1
                ,num2)}")
            elif choice=='4':
                try:
                    print(f"Result: {num1} / {num2} = {div(num1,num2)}")
                except ZeroDivisionError as e:
                    print(e)
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
if __name__=="__main__":
    calculator()
    