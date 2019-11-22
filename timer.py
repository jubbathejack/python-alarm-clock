#!/usr/bin/env python3

import datetime
import vlc
import time

print("Please enter a time in 24H format like HH:MM:SS.")
userTime = input()

url = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p'

while userTime != datetime.datetime.now().strftime("%H:%M:%S"):
    pass
else:
    print("Alarm!")
    time_end = time.time() + 60 * 5
    instance = vlc.MediaPlayer(url)
    while time.time() < time_end:
        instance.play()
    else:
        instance.stop()
        exit(0)
