# • Practical Example 3: Write a Python program to find a specific string in the list using a simple
# for loop and if condition.


fruits = ['apple', 'banana', 'mango', 'orange', 'grape']
string = input("Enter the fruit you want to find: ")
found = False
for fruit in fruits:
    if fruit == string:
        found = True
        break
if found:
    print(f"{string} is in the list.")
else:
    print(f"{string} is not in the list.")