#! Python3

# Program will search through a directory for files with a particular
# extension and copy them from their location to a new folder

import os, re, shutil

# Take input about what folder to search & what file extension
print("What is the directory of the folder you'd like to search?")
rootFolder = input()

print("What file extension would you like to search for?")
extension = input()

# Take input about what the new folder should be called
print("What is the full path of your new folder?")
newFolder = input()

# Walk through the directory searching for specific files, copy to new folder
if not os.path.exists(newFolder):
    os.mkdir(newFolder)

if os.path.exists(rootFolder):
    absFolder = os.path.abspath(rootFolder)
    extRegex = re.compile(extension)
    for root, dirs, files in os.walk(rootFolder):
        for file in files:
            if extRegex.search(file):
                print(root + '\\' + file + ' will be copied to ' + newFolder)
                shutil.copy(root + '\\' + file, newFolder)
        
else:
    print("That folder does not exist.")
