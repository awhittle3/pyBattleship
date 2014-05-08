#Makes the enemy board that the player sees
def makeEnemyBoard(size):
    board = []
    #Print ~ for unknown ocean spaces
    for x in range(size):
        board.append('~' * size)
    return board

#Makes the player's board with pre-arranged ships
def makePlayerBoard(size):
    x = '~' #Empty ocean
    o = 'o' #Ships
    board = [[x,x,x,x,x,x,x,x,x,x],
             [x,o,o,x,x,x,x,x,x,x],
             [x,x,x,x,x,x,x,x,x,x],
             [x,o,x,x,x,x,x,x,x,x],
             [x,o,x,o,o,o,x,x,x,x],
             [x,o,x,x,x,x,x,x,x,x],
             [x,o,x,x,x,x,x,x,x,o],
             [x,o,x,x,x,x,x,x,x,o],
             [x,x,x,x,o,o,o,o,x,o],
             [x,x,x,x,x,x,x,x,x,x],]
    return board
    
#Prints two boards
def printBoards(board1, board2):
    grid = []
    
    size1 = len(board1)
    size2 = len(board2)
    #Boards should be the same size
    if size1 != size2:
        print("Error: Player and enemy boards not same size")
    
    #Create a grid line string
    for x in range(size1 + 1):
        grid.append("+")
    gridLine = " ".join(grid)
    
    #Print boards with gridlines
    for line in board1:
        print(gridLine)
        print(" " + " ".join(line))
    print(gridLine)
    
    for line in board2:
        print(gridLine)
        print(" " + " ".join(line))
    print(gridLine)