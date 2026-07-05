import os

# Specify the directory path you want to list
directory_path = '/'

# List all files and directories in the specified path
contentents = os.listdir(directory_path)

#print each file and directory name
for item in contentents:
    print(item)