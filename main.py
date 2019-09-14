from tkinter import *
import pygame
import os
root = Tk()
root.title("Music Player by SakubDev")
root.geometry("205x340")


os.chdir("./Music")
print(os.getcwd)
songList = os.listdir()


playlist = Listbox(root, highlightcolor="blue", selectmode = SINGLE)
print(songList)

for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos += 1

def playSong():
    pygame.mixer.init()
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()


def stopSong():
    pygame.mixer.music.stop()

var = StringVar()
songTitle = Label(root, textvariable = var)

PlayBtn = Button(root, width=5, height=3, text="Play", command=playSong)
StopBtn = Button(root, width=5, height=3, text="Stop", command=stopSong)

PlayBtn.pack(fill="x")
StopBtn.pack(fill="x")
songTitle.pack()
playlist.pack(fill = "both", expand = "yes")

root.mainloop()
