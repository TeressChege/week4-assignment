#Reading and writing file
with open("tesss.txt", "r") as file:
    data=file.read()
modified_data=data.upper()
with open("tesss.txt","w") as file:
    file.write(modified_data)
print(modified_data)

#Error handling
filename = input("Enter the filename: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File successfully read:")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
