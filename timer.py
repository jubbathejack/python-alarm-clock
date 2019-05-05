#!/usr/bin/env python3

import datetime
from pygame import mixer, mixer_music

print("Please enter a time in 24H format like HH:MM:SS.")
userTime = input()

while userTime != datetime.datetime.now().strftime("%H:%M:%S"):
    pass
else:
    print("Alarm!")
    mixer.init()
    mixer_music.load("alarm.wav")
    mixer_music.play()
    while mixer.music.get_busy():
        continue
    exit(0)
