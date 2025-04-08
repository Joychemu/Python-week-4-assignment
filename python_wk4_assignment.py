filename = input("Enter the filename to read: ")
try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File read successfully.")
        modified_content = modify_content(content)
        new_examplefile = f"modified_{filename}"

        with open(new_filename, 'w') as file:
            file.write(modified_content)
            print(f" Modified content written to '{new_filename}'.")

except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
