import os
import shutil

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error opening file: {e}")

def create_file_or_folder(path):
    if '.' in os.path.basename(path):
        try:
            with open(path, 'w') as file:
                file.write('')
            print(f"File {path} successfully created.")
        except Exception as e:
            print(f"Error creating file: {e}")
    else:
        try:
            os.makedirs(path)
            print(f"Folder {path} successfully created.")
        except Exception as e:
            print(f"Error creating folder: {e}")

def move_file_or_folder(source, destination):
    try:
        shutil.move(source, destination)
        print(f"{source} successfully moved to {destination}.")
    except FileNotFoundError:
        print(f"{source} not found.")
    except Exception as e:
        print(f"Error moving: {e}")

def main():
    while True:
        print("\nChoose an action:")
        print("1. Open file")
        print("2. Create file/folder")
        print("3. Move file/folder")
        print("4. Exit")

        choice = input("Enter the action number: ")

        if choice == '1':
            file_path = input("Enter the file name: ")
            open_file(file_path)
        elif choice == '2':
            path = input("Enter the path and name of the file/folder: ")
            create_file_or_folder(path)
        elif choice == '3':
            source = input("Enter the source path: ")
            destination = input("Enter the destination path: ")
            move_file_or_folder(source, destination)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

