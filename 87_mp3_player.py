""" 87**Mp3 Player**
    A simple program for playing your favorite music files. Add features you though are missing from
    your favorite music player.
"""
import mp3play

mp3 = mp3play.load(file)
mp3.play()

# Let it play for up to 30 seconds, then stop it.
import time
# time.sleep(30, mp3.seconds())
# mp3.stop()