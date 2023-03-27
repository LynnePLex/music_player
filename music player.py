import tkinter as tk
import fnmatch
import os
import pygame 
import mixer

#The canvas UI
canvas = tk.Tk()
canvas.title("TPex Music Player - Lynne")
canvas.geometry("600x800")
canvas.config(bg = 'black')

#The music file path
rootpath = "C:\\Users\Lynne\Desktop\Music"
pattern = "*.mp3"



#The buttons file images
prev_img = tk.PhotoImage(file = 'prev_img.png')
next_img = tk.PhotoImage(file = 'next_img.png')
stop_img = tk.PhotoImage(file = 'stop_img.png')
play_img = tk.PhotoImage(file = 'play_img.png')
pause_img = tk.PhotoImage(file = 'pause_img.png')

def select():
    label.config(text = listBox.get('anchor'))
    mixer.music.load(rootpath + '\\' + listBox.get('anchor'))
    mixer.music.play()

#Shows all mp3 file in a list
listBox = tk.Listbox(canvas, fg = "red", bg = "black",  width = 100, font = ('ThaleahFat', 14))
listBox.pack(padx = 15, pady = 15)

#This displays the music title
label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow', font =('ThaleahFat'))
label.pack(pady = 15)

#The buttons box UI
top = tk.Frame(canvas, bg = 'black')
top.pack(padx = 10, pady = 5, anchor = 'center')

#Buttons
prevButton = tk.Button(canvas, text = 'Prev', image = prev_img, bg = 'black', borderwidth = 0)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text = 'Stop', image = stop_img, bg = 'black', borderwidth = 0)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = 'Play', image = play_img, bg = 'black', borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text = 'Pause', image = pause_img, bg = 'black', borderwidth = 0)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = 'Next', image = next_img, bg = 'black', borderwidth = 0)
nextButton.pack(pady = 15, in_ = top, side = 'left')

#File paths
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()