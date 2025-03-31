# • Write a Python program to open a file in write mode, write some text, and then close it. 
# Define the name of the file
file_name = 'simple.txt'
with open(file_name, 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a sample text written to the file.\n')
    file.write('Goodbye!\n')
print(f'Text has been written to {file_name}.')