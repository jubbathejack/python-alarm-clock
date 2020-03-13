#!/usr/bin/env python3

import datetime
import time
import subprocess

print("Please enter a time in 24H format like HH:MM:SS.")
userTime = input()

url = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p'


class Player:
    def __init__(self):
        pass

    def load(self, url):
        subprocess.run(["mpc", "add", url])

    def play(self):
        subprocess.run(["mpc", "play", "1"])

    def stop(self):
        subprocess.run(["mpc", "stop"])

    def delete(self):
        subprocess.run(["mpc", "del", "1"])


player = Player()


try:
    while userTime != datetime.datetime.now().strftime("%H:%M:%S"):
        pass
    else:
        print("Alarm!")
        time_end = time.time() + 60 * 5
        player.load(url=url)
        player.play()
        while time.time() < time_end:
            continue
        else:
            player.stop()
            player.delete()
            exit(0)
except KeyboardInterrupt:
    player.stop()
    player.delete()
    print("Cancelled by user.")
    exit(1)
