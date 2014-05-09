import boards

def main():
    MAX_HITS = 17
    enemyDead = False
    playerDead = False
    hitsOnEnemy = 0
    hitsOnPlayer = 0
    turn = 1
    
    n = boards.selectRand() #Select two random boards
    enemyBoard = boards.makeEnemyBoard()
    enemyLocations = boards.selectBoard(n[0])
    playerBoard = boards.selectBoard(n[1])
    
    print("----BATTLESHIP----")
        
    while not playerDead and not enemyDead:
        boards.printBoards(enemyBoard, playerBoard)
        print("Turn " + str(turn))
        row = int(input("Guess row: ")) - 1
        col = int(input("Guess coloumn: ")) - 1
        
        #Player choice evaluated
        if enemyLocations[row][col] == "o":
            #It's a hit!
            enemyBoard[row][col] = "*"
            hitsOnEnemy += 1
            
        else:
            if(row < 0 or row > boards.BOARD_SIZE - 1) or (col < 0 or col > boards.BOARD_SIZE - 1):
                print("Oops, that's not even in the ocean.")
            elif(enemyBoard[row][col] == "X" or enemyBoard[row][col] == "*"):
                print("You guessed that one already.")
            else:
                #It's a miss
                enemyBoard[row][col] = "X"        
        
        #Check if either player is dead
        if hitsOnEnemy == MAX_HITS:
            enemyDead = True
        elif hitsOnPlayer == MAX_HITS:
            playerDead = True
        
        turn += 1
        
        #Make true for testing purposes
        enemyDead = True
    
    if enemyDead:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

main()