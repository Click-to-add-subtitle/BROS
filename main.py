import time
import serial
import keyboard

from obama import turnyBoi


def main():
    arduinoData = serial.Serial('com4', 9600)

    # inputsAndTurning = turnyBoi(arduinoData)
    # inputsAndTurning.setWPosition(40)


    # to encode:
    # str(chr(value)).encode()

    while True:
        if keyboard.is_pressed('a'):
            arduinoData.write(str(chr(70)).encode())
            time.sleep(.1)
        if keyboard.is_pressed('d'):
            #print(bytes(ord('a')))
            arduinoData.write(str(chr(110)).encode())
            time.sleep(.1)


if __name__ == "__main__":
    main()
