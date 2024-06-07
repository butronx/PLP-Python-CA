# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("Second line with numbers: 42, 7.5, 100\n")
        file.write("Another line to write.\n")
        print("File 'my_file.txt' created successfully.")
except Exception as e:
    print(f"Error creating file: {e}")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied while trying to read the file.")
except Exception as e:
    print(f"Error reading file: {e}")
finally:
    print("\nFile reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")
        print("File 'my_file.txt' appended successfully.")
except Exception as e:
    print(f"Error appending to file: {e}")
finally:
    print("File appending process completed.")
