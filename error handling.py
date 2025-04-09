def handle_user_file():
    filename = input("Enter the name of the file you want to read: ")
    try:
        with open(filename, 'r') as file:
            print("File content:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
