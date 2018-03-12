#! python3
# Script will accept a list of list of strings and organize the table for output.


tableData = [['apples', 'oranges', 'cherries', 'banana', 'mango', 'plums'],
             ['Alice', 'Bob', 'Carol', 'David', 'Mike', 'Todd'],
             ['dogs', 'cats', 'moose', 'goose', 'tiger', 'elephant']]

def printTable(table):
    colWidths = [0] * len(table)

    for i in range(len(table)):
        maxWidth = 0
        for v in range(len(table[i])):
            if maxWidth < len(table[i][v]):
                maxWidth = len(table[i][v])
        colWidths[i] = maxWidth

    for i in range(len(table[0])):
        for v in range(len(table)):
            print(table[v][i].rjust(colWidths[v]), end = ' ')
        print('\n')

printTable(tableData)

#print(len(tableData[0][0]))
#print(tableData[0][1])
