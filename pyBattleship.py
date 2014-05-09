import boards

def main():
    alive = True
    
    enemyBoard = boards.makeEnemyBoard()
    enemyLocations = boards.setupEnemyBoard()
    playerBoard = boards.makePlayerBoard()
    
    print("----BATTLESHIP----")
    boards.printBoards(enemyBoard, playerBoard)
    
    while alive:
        row = int(input("Guess row: "))
        col = int(input("Guess coloumn: "))
        
        #Make false for testing purposes
        alive = False

main()