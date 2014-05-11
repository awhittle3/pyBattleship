from random import randint
from boards import BOARD_SIZE

def guessing(board):
    n = selectTarget()
    if board[n[0]][n[1]] == "~":
        #Target was a miss
        board[n[0]][n[1]] = "X"
        n = [99,99] #Return a null target
    elif board[n[0]][n[1]] == "o":
        #A ship was hit
        board[n[0]][n[1]] = "*"
    else:
        n = guessing(board)
    return n

def selectTarget():
    n = []
    n.append(randint(0, BOARD_SIZE - 1))
    n.append(randint(0, BOARD_SIZE - 1))
    
    #Fit random coordinates to smart grid (spaced apart guesses)
    if (n[0] + n[1]) % 2 != 0:
        n[0] += 1
        if n[0] == BOARD_SIZE:
            if n[1]%2 == 0:
                n[0] = 1
                n[1] += 1
            else:
                n[0] = 0
                n[1] += 1
                
            if n[1] == BOARD_SIZE:
                n[0] = 0
                n[1] = 0
                
    return n
        
#Target a ship. i is coordinates of initial hit.
#TO DO: Fix bug where it won't change back to guessing mode
def targeting(board, i):
    if validDirection(i, [0,1], board) == True:
        n = targetingGuess(i, [0,1], board)
    elif validDirection(i, [0,-1], board) == True:
        n = targetingGuess(i, [0,-1], board)
    elif validDirection(i, [1,0], board) == True:
        n = targetingGuess(i, [1,0], board)
    elif validDirection(i, [1,0], board) == True:
        n = targetingGuess(i, [-1,0], board)
    else:
        return [99,99]
    return n

#Guess for a direction
def targetingGuess(i, vector, board):
    n = addVectors(i, vector)
    if board[n[0]][n[1]] == "o":
        #It's a hit!
        board[n[0]][n[1]] = "*"
    elif board[n[0]][n[1]] == "~":
        #It's a miss
        board[n[0]][n[1]] = "X"
    else:
        i = addVectors(i,vector)
        i = targetingGuess(i, vector, board)
    return i

#Takes a target and a vector and checks that direction
def validDirection(i, vector, board):
    n = addVectors(i, vector)
    if (i[0] < 0 or i[0] > (BOARD_SIZE - 1)) or (i[1] < 0 or i[1] > (BOARD_SIZE - 1)):
        return False
    elif board[i[0]][i[1]] == "X":
        return False
    else:
        return True
    
def addVectors(i, j):
    n = []
    n.append(i[0] + j[0])
    n.append(i[1] + j[1])
    return n