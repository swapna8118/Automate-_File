import os

# Enter the folder path
folder_path = input("Enter the folder path: ")

# Get all files in the folder
files = os.listdir(folder_path)

# Sort files (optional)
files.sort()

# Counter
count = 1

# Rename each file
for file in files:
    old_path = os.path.join(folder_path, file)

    # Check if it is a file (not a folder)
    if os.path.isfile(old_path):
        # Get the file extension
        extension = os.path.splitext(file)[1]

        # Create new file name
        new_name = f"file_{count}{extension}"
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"{file} --> {new_name}")

        count += 1

print("All files renamed successfully!")