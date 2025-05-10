import os

# Specify the directory path
directory_path = '/new folder'

# Get the list of all files and directories in the specified directory
entries = os.listdir(directory_path)

# Iterate over the entries and print them
for entry in entries:
    print(entry)
