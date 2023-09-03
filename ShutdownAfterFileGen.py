import os
import time
import sys

def count_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return len(files)
    except FileNotFoundError:
        return 0

def main():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    initial_file_count = count_files_in_folder(current_folder)

    print(f"There are currently {initial_file_count} files in the folder.")

    try:
        num_files_to_wait_for = int(input("Enter the number of files to wait for: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sys.exit(1)

    while True:
        current_file_count = count_files_in_folder(current_folder)

        if current_file_count >= initial_file_count + num_files_to_wait_for:
            break

        time.sleep(5)

    abort = input("Files have increased. Do you want to abort? (yes/no): ").lower()
    if abort == 'yes':
        print("Aborting.")
        time.sleep(10)
        print("Aborted.")
    else:
        print("Shutting down the computer...")
        os.system("shutdown /s /t 1")

if __name__ == "__main__":
    main()
