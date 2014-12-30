""" **Alarm Clock**
    A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
"""

import os
import time


def sound():
    for i in range(2):  # number of repeats
        for j in range(9):  # number of beeps
            os.system('beep')  # sound
        time.sleep(2)  # pause between beeps


def alarm(n):
    print()
    print("Wait time:", n, "seconds.")
    time.sleep(n)

    sound()


