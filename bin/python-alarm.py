#!/usr/bin/env python3

import datetime
import time
import subprocess

print("Please enter a time in 24H format like HH:MM:SS.")
userTime = input()

url = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p'


class Player:
    def __init__(self):
        self.p = None

    def play(self, radio_link):
        self.p = subprocess.Popen(f"mplayer {radio_link} >/dev/null 2>&1", shell=True)

    def stop(self):
        self.p.kill()


player = Player()


try:
    while userTime != datetime.datetime.now().strftime("%H:%M:%S"):
        pass
    else:
        print("Alarm!")
        time_end = time.time() + 60 * 5
        player.play(radio_link=url)
        while time.time() < time_end:
            continue
        else:
            player.stop()
            exit(0)
except KeyboardInterrupt:
    player.stop()
    print("Cancelled by user.")
    exit(1)
