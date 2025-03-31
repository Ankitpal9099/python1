# Practical Example: 3) Write a Python program to create a file and write a string into it. 

file_name = 'my_file.txt'
text_to_write = 'This is a string that will be written to the file.'
with open(file_name, 'w') as file:
    file.write(text_to_write)
print(f'The string has been written to {file_name}.')