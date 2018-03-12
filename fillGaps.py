#! Python3

#Program will close gaps in numbered filenames or insert gaps for new files to be inserted.

import os, shutil, re

def closeGap(filePath):
    #set absolute path variables
    absFilePath = os.path.abspath(filePath)
    fileName = os.path.basename(absFilePath)
    dirName = os.path.dirname(absFilePath)

    #set regex filename pattern
    filePattern = re.compile(r'^(\D+)(\d+)(\D+)$')

    #create regex variable based on the submitted filename
    baseMatch = filePattern.search(fileName)

    #change to the requested directory and establish a list of file
    os.chdir(dirName)
    fileList = os.listdir()

    #create an empty list for files that match the filename regex
    matchingFiles = []

    #iterate thru the list of files finding regex filename matches and writing them to list
    for file in fileList:
        fileListMatch = filePattern.search(file)
        if  fileListMatch != None:
            if baseMatch.group(1) == fileListMatch.group(1) and baseMatch.group(3) == fileListMatch.group(3):
                matchingFiles.append(fileListMatch.group(0))

    #find the number of the highest numbered file
    highestFile = filePattern.search(matchingFiles[-1])

    #compare number of files that have filename matches against the highest numbered file, if not equal then there are gaps
    if len(matchingFiles) != int(highestFile.group(2)):
        print('There is a gap in the files.')
        
        #create variable to pad file numbers and rename files based on iteration
        for i in range(len(matchingFiles)):
            numPad = len(baseMatch.group(2)) - len(str(i+1))
            shutil.move(dirName + '\\' + matchingFiles[i], dirName + '\\' + baseMatch.group(1) + '0' * numPad + str(i+1) + baseMatch.group(3))
    else:
        print('There are no gaps.')
                         

def openGap(filepath):

    absFilePath = os.path.abspath(filepath)
    baseName = os.path.basename(filepath)
    dirName = os.path.dirname(filepath)

    filePattern = re.compile(r'(^\D+)(\d+)(.\D+$)')

    mo = filePattern.search(baseName)

    os.chdir(dirName)
    fileList = os.listdir()

    matchFileList = []

    for file in fileList:
        mo2 = filePattern.search(file)
        if mo2 != None:
            if mo.group(1) == mo2.group(1) and mo.group(3) == mo2.group(3):
                matchFileList.append(mo2.group(0))

    for i in range((len(matchFileList) - 1),0,-1):
        mo3 = filePattern.search(matchFileList[i])
        nextNum = int(mo3.group(2)) + 1
        numPad = len(mo3.group(2)) - len(str(int(mo3.group(2)) + 1))
        if mo.group(2) != mo3.group(2):
            shutil.move(dirName + '\\' + matchFileList[i], dirName + '\\' + mo.group(1) + '0' * numPad + str(nextNum) + mo.group(3))
        else:
            shutil.move(dirName + '\\' + matchFileList[i], dirName + '\\' + mo.group(1) + '0' * numPad + str(nextNum) + mo.group(3))
            print('Gap created at ' + baseName)
            break


print('Would you like to CLOSE a filename gap, or OPEN a filename gap?')
gapType = input()
if gapType.lower() == 'close':
    print('What is the path of the file were you would like to begin searching for and closing gaps?')
    closeInput = input()
    closeGap(closeInput)
elif gapType.lower() == 'open':
    print('What is the path of the file were you would like a gap to be opened?')
    openInput = input()
    openGap(openInput)
else:
    print('That is not an acceptable value, please enter CLOSE or OPEN.')
