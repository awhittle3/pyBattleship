import winsound

#http://www.phy.mtu.edu/~suits/notefreqs.html
scale = {'C4':262, 'C4s':277, 'D4':294, 'D4s':311, 'E4':330, 'F4':349, 'F4s':370, 'G4':392, 'G4s':415, 'A4':440, 'A4s':466, 'B4':494,
         'C5':523, 'C5s':554, 'D5':587, 'D5s':622, 'E5':659, 'F5':698, 'F5s':740, 'G5':784, 'G5s':831, 'A5':880, 'A5s':932, 'B5':988,
         'C6':1047}

def play(sound, duration):
    winsound.Beep(scale[sound], duration)
