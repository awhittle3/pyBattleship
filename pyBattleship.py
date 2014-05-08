import boards

def main():
    BOARD_SIZE = 10
    enemyBoard = boards.makeEnemyBoard(BOARD_SIZE)
    playerBoard = boards.makePlayerBoard(BOARD_SIZE)
    
    print("BATTLESHIP")
    boards.printBoards(enemyBoard, playerBoard)

main()