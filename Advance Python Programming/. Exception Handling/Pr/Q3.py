# 9) Write a Python program to handle file exceptions and use the finally block for closing the file

def read_file(file_name):
    try:
        file = open(file_name, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An I/O error occurred.")
    finally:
        try:
            file.close()
        except NameError:
            pass 

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    read_file(file_name)