# • Write a Python program to demonstrate handling multiple exceptions. 
print("Simple Calculator")
try:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    result=num1/num2
    print(f"the result is {result}")
    
except ZeroDivisionError:
    print("Division by zero is not allowed.")
    
