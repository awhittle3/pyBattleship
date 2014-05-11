import boards
import enemyAI

def main():
    enemyDead = False
    playerDead = False
    targetingMode = False
    target = [99,99]    #99, 99 is the null target value
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
        if(row < 0 or row > boards.BOARD_SIZE - 1) or (col < 0 or col > boards.BOARD_SIZE - 1):
            print("Oops, that's not even in the ocean.")
        elif(enemyBoard[row][col] == "X" or enemyBoard[row][col] == "*"):
                print("You guessed that one already.")
        elif enemyLocations[row][col] == "o":
            #It's a hit!
            enemyBoard[row][col] = "*"
        else:
            #It's a miss
            enemyBoard[row][col] = "X"        
        
        #Enemy turn
        if targetingMode == False:
            #Guess a random location
            target = enemyAI.guessing(playerBoard)
            if target != [99,99]:
                targetingMode = True #Ship was hit, target ship
        else:
            #Try to sink a targeted ship
            targetingMode = enemyAI.targeting(playerBoard, target)
            if targetingMode == False:
                target = [99,99] #Set to null, ship was sunk
        
        #Check if either player is dead
        if not isAlive(enemyBoard):
            enemyDead = True
        elif not isAlive(playerBoard):
            playerDead = True
        
        turn += 1
        
    #Print game result
    if enemyDead:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

def isAlive(board):
    MAX_HITS = 17
    count = 0
    for line in board:
        for space in line:
            if space == "*":
                count += 1
    if count == MAX_HITS:
        return False
    else:
        return True

main()