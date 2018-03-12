tableData = [['apples', 'oranges', 'cherries', 'banana', 'mango', 'plums'],
             ['Alice', 'Bob', 'Carol', 'David', 'Mike', 'Todd'],
             ['dogs', 'cats', 'moose', 'goose', 'tiger', 'elephant']]

def printTable(dataLists):
    colWidths = [0] * len(dataLists)
    for i in colWidths:
        colWidths = max(dataLists[i], key=len)
           
    y = len(colWidths)
        
    for x in range(len(dataLists[0])):
        print(str(dataLists[0][x]).rjust(y) + str(dataLists[1][x]).rjust(y) + str(dataLists[2][x]).rjust(y))


printTable(tableData)
