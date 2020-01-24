import serial
import pyvesc
import time
import tkinter

import threading


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


class oneLongBoi:

    def __init__(self, name, port):
        self.name = name
        self.fsesc = port

        self.dutyCycle = 5000
        self.running = True

        self.previous_Time = time.time()

    def stop(self):
        self.running = False

    def setDutyCycle_BarackObama(self, value):
        self.dutyCycle = value

    def increaseSpeed(self):
        self.dutyCycle += 1

    def decreaseSpeed(self):
        self.dutyCycle -= 1

    @threaded
    def run(self):

        while self.running:
            # print(self.dutyCycle)
            if (time.time() != self.previous_Time):
                package = self.dutyPackage(self.dutyCycle)
                self.fsesc.write(package)
                self.fsesc.flush()

            self.previous_Time = time.time()

    @staticmethod
    def dutyPackage(voltage) -> bytes:
        slowDutyCycleF = pyvesc.SetDutyCycle(voltage)  # prints value of my_msg.duty_cycle
        sendSDCF = pyvesc.encode(slowDutyCycleF)
        return sendSDCF


