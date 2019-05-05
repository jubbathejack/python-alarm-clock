#!/usr/bin/env python3

import datetime
import pygame

print("Please enter a time in 24H format like HH:MM:SS.")
userTime = input()

while userTime != datetime.datetime.now().strftime("%H:%M:%S"):
    pass
else:
    print("Alarm!")
    pygame.mixer.init()
    pygame.mixer_music.load("alarm.wav")
    pygame.mixer_music.play()
    while pygame.mixer.music.get_busy():
        continue
    exit(0)
