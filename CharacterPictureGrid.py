
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid2 = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.', '.', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]



def pictureGrid(gridData):
    for i in range(6):
        for x in range(9):
            print(gridData[x][i], end='')
            if x == 8:
                print()
                continue
            
def betterGrid(gridData):
    for i in range(len(gridData[0])):
        for x in range(len(gridData)):
            print(gridData[x][i], end="")
            if x == (len(gridData) - 1):
                print()

#pictureGrid(grid)
betterGrid(grid2)
