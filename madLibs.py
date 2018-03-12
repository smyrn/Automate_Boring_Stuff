#! Python3

# Chapter 8 - Mad Libs


import os, re

# Prompts user for filename and opens it if it exists
print('What is the name of the Mad Libs file?')
madLibFilename = input()


if os.path.exists(os.getcwd() + '\\' + madLibFilename):
    openMadLibFile = open(os.getcwd() + '\\' + madLibFilename)
    readFile = openMadLibFile.read()
else:
    print('That file does not exist')


# Set regex pattern to find sentence structure pieces in file
madLibRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
originalStructure = madLibRegex.findall(readFile)
updatedStructure = madLibRegex.findall(readFile)

for i in range(len(originalStructure)):
    if originalStructure[i] == 'ADJECTIVE':
        print('Enter an ' + originalStructure[i].lower() + ':')
    elif originalStructure[i] != 'ADJECTIVE':
        print('Enter a ' + originalStructure[i].lower() + ':')
    piece = input()
    del updatedStructure[i]
    updatedStructure.insert(i, piece)

splitFileRegex = re.compile(r'\w+|\.|\s')

splitFile = splitFileRegex.findall(readFile)
           
for x in range(len(originalStructure)):
    for y in range(len(splitFile)):
        if splitFile[y] == originalStructure[x]:
            del splitFile[y]
            splitFile.insert(y, updatedStructure[x])
            break

completeFile = ''.join(splitFile)

# Print final text to screen
print(completeFile)

# Save final text to new file
finalFile = open(os.getcwd() + '\\' + madLibFilename.replace('.txt','') + 'Complete.txt', 'w')
finalFile.write(completeFile)
finalFile.close()
