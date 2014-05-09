from random import randint

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

board3 = [[x,x,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,x,x],
          [x,o,o,o,o,o,x,x,o,o],
          [x,x,x,x,x,x,x,x,x,x],
          [x,x,o,x,x,x,x,x,x,x],
          [o,x,o,x,x,x,x,x,x,x],
          [o,x,o,x,x,x,x,x,x,x],
          [o,x,o,x,x,x,x,x,x,x],
          [x,x,x,x,x,o,o,o,x,x],
          [x,x,x,x,x,x,x,x,x,x],]

board4 = [[x,x,x,x,x,x,x,x,x,x],
          [o,x,x,x,x,x,x,x,x,x],
          [o,x,x,x,x,o,o,o,o,x],
          [o,x,x,x,x,x,x,x,x,x],
          [o,x,x,x,o,o,x,x,x,x],
          [o,x,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,x,o],
          [x,x,x,o,x,x,x,x,x,o],
          [x,x,x,o,x,x,x,x,x,o],
          [x,x,x,o,x,x,x,x,x,x],]

board5 = [[o,x,x,x,x,x,x,x,x,x],
          [o,x,x,x,x,x,o,o,o,o],
          [x,x,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,x,x],
          [x,x,x,o,o,o,o,o,x,x],
          [x,x,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,o,x,x],
          [x,x,x,o,o,o,x,o,x,x],
          [x,x,x,x,x,x,x,o,x,x],
          [x,x,x,x,x,x,x,x,x,x],]

#Select two different random numbers
def selectRand():
    i = 5 #number of boards available
    n = [randint(1,i), randint(1,i)]
    if n[0] == n[1]:
        n = selectRand()
    return n

#Select a board from pre-made boards
def selectBoard(n):
    return {
        1 : board1,
        2 : board1,
        3 : board3,
        4 : board4,
        5 : board5
        }.get(n, board1)

#Makes the enemy board that the player sees
def makeEnemyBoard():
    board = []
    #Print ~ for unknown ocean spaces
    for x in range(BOARD_SIZE):
        board.append(['~'] * BOARD_SIZE)
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