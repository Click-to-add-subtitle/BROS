import time

import keyboard
import pyvesc
from Controls.FSESC import oneLongBoi


class ayylmao:

    def __init__(self):
        self.running = True
        self.dutycycle = 5000

    def stop(self):
        if keyboard.is_pressed("s"):  # if key 'q' is pressed
            self.running = False

    def forward(self, value):
        if keyboard.is_pressed("w"):
            self.dutycycle = value
            self.running = True

    def faster(self):
        self.running = True
        if keyboard.is_pressed("p"):
            self.dutycycle += 100

    def slower(self):
        self.running = True
        if keyboard.is_pressed("o"):
            self.dutycycle -= 100
