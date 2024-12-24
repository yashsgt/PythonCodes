# Write python progrm to print the contents of directory using the os module.  
# Search online for the function which does that.
import os

# Specify the directory you want to list
directory_path = '/'
# List all files and directories in the specified path
contents = os.listdir(directory_path)
        
print(f"Contents of the directory '{directory_path}':")
for item in contents:
            print(item)
    
       