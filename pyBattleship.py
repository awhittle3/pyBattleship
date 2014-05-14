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
    
    #Print legend
    print("~ is empty ocean")
    print("o are your ships")
    print("X are misses")
    print("* are hits")
    input("Press enter to continue")
    
    print("\n----BATTLESHIP----")
        
    while not playerDead and not enemyDead:
        boards.printBoards(enemyBoard, playerBoard)
        print("Turn " + str(turn))
        i = userInput()
        
        #Player choice evaluated
        if(i[0] < 0 or i[0] > boards.BOARD_SIZE - 1) or (i[1] < 0 or i[1] > boards.BOARD_SIZE - 1):
            print("Oops, that's not even in the ocean.")
        elif(enemyBoard[i[0]][i[1]] == "X" or enemyBoard[i[0]][i[1]] == "*"):
                print("You guessed that one already.")
        elif enemyLocations[i[0]][i[1]] == "o":
            #It's a hit!
            enemyBoard[i[0]][i[1]] = "*"
        else:
            #It's a miss
            enemyBoard[i[0]][i[1]] = "X"        
        
        #Enemy turn
        if targetingMode == False:
            #Guess a random location
            target = enemyAI.guessing(playerBoard)
            if target != [99,99]:
                targetingMode = True #Ship was hit, target ship
        else:
            #Try to sink a targeted ship
            target = enemyAI.targeting(playerBoard, target)
            if target == [99,99]:
                targetingMode = False #Set to null, ship was sunk
        
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

def userInput():
    try:
        row = int(input("Guess row: ")) - 1
        col = int(input("Guess coloumn: ")) - 1
        n = [row,col]
    except(ValueError):
        print("Error: Input is not a number")
        n = userInput()
    
    return n

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