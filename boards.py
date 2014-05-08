def makeEnemyBoard(size):
    board = []
    for x in range(size):
        board.append('~' * size)
    return board

def makePlayerBoard(size):
    x = '~'
    o = 'o'
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
    

def printBoards(board1, board2):
    grid = []
    
    size1 = len(board1)
    size2 = len(board2)
    if size1 != size2:
        print("Error: Player and enemy boards not same size")
        
    for x in range(size1 + 1):
        grid.append("+")
    gridLine = " ".join(grid)
    
    for line in board1:
        print(gridLine)
        print(" " + " ".join(line))
    print(gridLine)
    
    for line in board2:
        print(gridLine)
        print(" " + " ".join(line))
    print(gridLine)