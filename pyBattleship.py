import boards

def main():
    playerDead = False
    enemyDead = False
    
    enemyBoard = boards.makeEnemyBoard()
    enemyLocations = boards.setupEnemyBoard()
    playerBoard = boards.makePlayerBoard()
    
    print("----BATTLESHIP----")
    boards.printBoards(enemyBoard, playerBoard)
    
    while not playerDead and not enemyDead:
        row = int(input("Guess row: "))
        col = int(input("Guess coloumn: "))
        
        #Make true for testing purposes
        enemyDead = True
    
    if enemyDead:
        print("You win!")
    else:
        print("You lose!")

main()