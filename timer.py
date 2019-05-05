#!/usr/bin/env python3

import datetime

print("Please enter a time in 24H format like HH:MM:SS.")
userTime = input()

while userTime != datetime.datetime.now().strftime("%H:%M:%S"):
    pass
else:
    print("Alarm!")
    exit(0)
