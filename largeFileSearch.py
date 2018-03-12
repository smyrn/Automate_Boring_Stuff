#! Python3

# Program to search for large files and print their paths.

import os

# Input from user about where to begin searching
print('Please provide a path to the folder would you like to begin the search for large files?')
rootFolder = input()

if os.path.isdir(rootFolder) and os.path.isabs(rootFolder):
    for foldername, subfolders, filenames in os.walk(rootFolder):
        for filename in filenames:
            fileSize = os.path.getsize(os.path.join(foldername, filename))
            if fileSize > 13107200:
                print('The file in %s named %s has a size of %s' % (foldername, filename, fileSize))

elif not os.path.isdir(rootFolder):
    print('The provided path is not a folder.')

elif not os.path.isabs(rootFolder):
    print('The entry is not a full path.')
