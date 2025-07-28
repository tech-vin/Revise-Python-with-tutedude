# Task 2: Write and Append Data to a file
FILE_PATH = 'files/output.txt'

def write_to_file():
    try:
        data = input("Enter text to write in the file: ")
        with open(FILE_PATH, 'w') as file:
            file.write(data, '\n')
    except Exception as ep:
        print(ep)

def append_to_file():
    try:
        data = input("Enter additional text to append: ")
        with open(FILE_PATH, 'a') as file:
            file.write(data)
    except Exception as ep:
        print(ep)

def read_from_file():
    try:
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
        for line in lines:
            print(f"Final content of {FILE_PATH}: \n{line}", end='')
    except Exception as ep:
        print(ep)


FILE_PATH = 'files/output.txt'

def write_to_file():
    try:
        data = input("Enter text to write in the file: ")
        with open(FILE_PATH, 'w') as file:
            file.write(data + '\n')  # Ensure newline
        print("Initial data written successfully.")
    except Exception as ep:
        print(f"Error writing to file: {ep}")

def append_to_file():
    try:
        more_data = input("Enter additional text to append: ")
        with open(FILE_PATH, 'a') as file:
            file.write(more_data + '\n')  # Ensure newline
        print("Additional data appended successfully.")
    except Exception as ep:
        print(f"Error appending to file: {ep}")

def read_file():
    try:
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
        print(f"\nFinal content of {FILE_PATH}:\n")
        for line in lines:
            print(line, end='')  # Avoid double newlines
    except Exception as ep:
        print(f"Error reading file: {ep}")

# Run all steps
write_to_file()
append_to_file()
read_file()
