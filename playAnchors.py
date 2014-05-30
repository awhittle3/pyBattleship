from playSounds import play

BEAT = 500
HALF = int(BEAT/2)
QUART = int(BEAT/4)

def playSong():
    play('C4' ,BEAT*2)
    play('E4', BEAT)
    play('G4', BEAT)
    play('A4', BEAT + 3*QUART)
    play('E4', QUART)
    play('A4', 2*BEAT)
    play('C5', BEAT*2)
    play('D5', BEAT)
    play('G4', BEAT)
    play('C5', BEAT*4)
