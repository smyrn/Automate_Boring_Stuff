#! Python3

# Program to open all .txt files in a folder, search for any line that matches
# a user supplied regex, and print the results on the screen.

import os, re

while True:
    print(r'Please provide a path to the folder like C:\path\to\folder')
    folderPath = input()
    if os.path.exists(folderPath) == False:
        print('That path does not exist.')
        break
    elif os.path.isdir(folderPath) == False:
        print('That path goes to something other than a folder.')
        break
    else:
        os.chdir(folderPath)
        fileList = os.listdir()
        
        print(r'Please provide a regular expression pattern to search for:')
        regexInput = input()
        txtRegex = re.compile(regexInput)
        fileRegex = re.compile(r'\.txt$')
        for i in range(len(fileList)):
            if fileRegex.search(fileList[i]):
                textFile = open(os.getcwd() + '\\' + fileList[i])
                readText = textFile.read()
                if not txtRegex.search(readText):
                    continue
                else:
                    print('Match of regex pattern "' + regexInput + '" found in file: ' + fileList[i])
            textFile.close()
        break


