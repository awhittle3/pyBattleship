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
        
        

def targeting(board, target):
    pass