# use "killall python" in the console to end the program

from hal import hal_input_switch as switch
from hal import hal_led as led

import RPi.GPIO as GPIO #import RPi.GPIO module


import socket
import time
from time import sleep

def setup():

    led.init()
    switch.init()
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input




def main():
    i = 0
    x = 0
    runTime = 20
    setup()
    while i < runTime:
        setup()
        swState = switch.read_slide_switch()
        while swState == 1:
            print("5hz")
            led.set_output(0, 1)
            time.sleep(0.1)
            led.set_output(0, 0)
            time.sleep(0.1)
            swState = switch.read_slide_switch()
            # i = i+1
            # if i > runTime:
            #     break

        while swState == 0:
            led.set_output(0, 1)
            time.sleep(0.05)
            led.set_output(0, 0)
            time.sleep(0.05)
            print("10hz")
            x = x + 1
            while x >= 50:
                time.sleep(0.1)
                swState = switch.read_slide_switch()
            swState = switch.read_slide_switch()
            # i = i+1
            # if i > runTime:
            #     break

if __name__ == "__main__":
    main()  