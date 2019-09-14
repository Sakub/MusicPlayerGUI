from tkinter import *
import pygame
root = Tk()
root.title("Music Player by SakubDev")
root.geometry("205x340")


file = "./Music/dobryChlopak.mp3"



def playSong():
    print("Nothing special here")
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    


def stopSong():
    print("Nothing special here")
    pygame.mixer.music.stop()



PlayBtn = Button(root, width=5, height=3, text="Play", command=playSong)
StopBtn = Button(root, width=5, height=3, text="Stop", command=stopSong)
SongName = Label(root, text="Song Name")

PlayBtn.pack(fill="x")
StopBtn.pack(fill="x")
SongName.pack(fill="both", expand="yes")

root.mainloop()
