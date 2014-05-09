import boards

def main():
    BOARD_SIZE = 10
    alive = True
    
    enemyBoard = boards.makeEnemyBoard(BOARD_SIZE)
    playerBoard = boards.makePlayerBoard(BOARD_SIZE)
    
    print("----BATTLESHIP----")
    boards.printBoards(enemyBoard, playerBoard)
    
    while alive:
        row = int(input("Guess row: "))
        col = int(input("Guess coloumn: "))
        
        #Make false for testing purposes
        alive = False

main()