import serial
import pyvesc
import time
import threading
import keyboard
import inputs

from Controls.FSESC import oneLongBoi


def main():
    motorPort = serial.Serial('COM3', 115200, timeout=0.1)
    jesus = oneLongBoi("bruh", motorPort)
    dutyCycleint = 8000
    jesus.setDutyCycle_BarackObama(dutyCycleint)
    print(time.asctime())

    # caramel Frappuccino, extra hot,with one inch of foam...

    while True:
        if keyboard.is_pressed("w"):
            jesus.run()
        if keyboard.is_pressed("s"):
            jesus.stop()
        if keyboard.is_pressed("e"):
            jesus.increaseSpeed()

        if keyboard.is_pressed("q"):
            jesus.decreaseSpeed()

        if keyboard.is_pressed("p"):
            jesus.stop()
            break


if __name__ == "__main__":
    main()

