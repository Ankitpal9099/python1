# • Practical Example 1: How does the Python code structure work?

def add(a, b):
    return a + b
def sub(a, b):
    return a-b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def exp(a, b):
    return a ** b
def main():
    print("welcome to the calculator")
    print(" slelect operation")
    print("1.add ")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.mod")
    print("6.exp")
    choice = input("enter choice 1/2/3/4/5/6")
    a = int(input("enter a"))
    b = int(input("enter b"))
    if choice == '1':
        print("addition of a and b is", add(a, b))
    elif choice == '2':
        print("subtraction of a and b is", sub(a, b))
    elif choice == '3':
        print("multiplication of a and b is", mul(a, b))
    elif choice == '4':
        if b != 0:
            print("division of a and b is", div(a, b))
    elif choice == '5':
            print("modulus of a and b is", mod(a, b))
    elif choice == '6':
            print("exponentiation of a and b is", exp(a, b))
    else:
            print("invalid choice")
if __name__ == "__main__":
    main()
    
    