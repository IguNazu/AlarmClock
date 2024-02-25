#for delay

import os
os.add_dll_directory(r'C:\My files\VLC')
import time
import vlc

alarm = int(input("Choose timer(seconds): "))
song = vlc.MediaPlayer("C:\\Users\\IguNazu\\Pictures\\alarm.mp3")

#timer countdown
while alarm != 0:
    print(alarm)
    time.sleep(1)
    alarm -= 1

#alarm
song.play()
input("press any key to continue...")
song.stop()