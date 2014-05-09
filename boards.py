BOARD_SIZE = 10
x = '~' #Empty ocean
o = 'o' #Ships

board1 = [[x,x,x,x,x,x,x,x,x,x],
          [x,o,o,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,x,x],
          [x,o,x,x,x,x,x,x,x,x],
          [x,o,x,o,o,o,x,x,x,x],
          [x,o,x,x,x,x,x,x,x,x],
          [x,o,x,x,x,x,x,x,x,o],
          [x,o,x,x,x,x,x,x,x,o],
          [x,x,x,x,o,o,o,o,x,o],
          [x,x,x,x,x,x,x,x,x,x],]

board2 = [[x,x,x,o,o,o,o,x,x,x],
          [x,x,x,x,x,x,x,x,x,x],
          [x,x,o,x,x,x,x,x,x,x],
          [x,x,o,x,o,x,x,x,x,x],
          [x,x,o,x,o,x,x,x,x,x],
          [x,x,x,x,o,x,x,x,x,x],
          [x,x,x,x,o,x,x,x,x,x],
          [x,x,x,x,o,x,o,o,o,x],
          [x,x,x,x,x,x,x,x,x,x],
          [x,o,o,x,x,x,x,x,x,x],]

#Makes the enemy board that the player sees
def makeEnemyBoard():
    board = []
    #Print ~ for unknown ocean spaces
    for x in range(BOARD_SIZE):
        board.append(['~'] * BOARD_SIZE)
    return board

#Set ships on enemy board, invisible to player
def setupEnemyBoard():
    board = board2
    return board

#Makes the player's board with pre-arranged ships
def makePlayerBoard():
    board = board1
    return board
    
#Prints two boards
def printBoards(board1, board2):
    
    size1 = len(board1)
    size2 = len(board2)
    #Boards should be the same size
    if size1 != size2:
        print("Error: Player and enemy boards not same size")
    
    #Print boards with separator
    for line in board1:
        print(" ".join(line))
    
    print("-" * size1 * 2)
    
    for line in board2:
        print(" ".join(line))