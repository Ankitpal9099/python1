# List1 = ['apple', 'banana', 'mango']
# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement.
# Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using
# the break statement.



# ----------------------------------------------------------------------------
# Practical Example: 1
print("-----------Practical Example: 1 ---------------")
print("-----------Practical Example: 1 ---------------")
list1 = ['apple', 'banana', 'mango']
for i in list1:
    if i=='banana':
        continue
    print([i])




# ----------------------------------------------------------------------------
# Practical Example: 2
print("-----------Practical Example: 2 ---------------")
list1 = ['apple', 'banana', 'mango']
for i in list1:
    print([i])
    if i=='banana':
        break