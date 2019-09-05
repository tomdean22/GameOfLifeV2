from tkinter import Tk
from tkinter import Canvas, LabelFrame, Frame
from tkinter import Label, Button
from tkinter import X, CENTER, LEFT, RIGHT, BOTH, BOTTOM, TOP
from tkinter import RAISED, GROOVE, SUNKEN, FLAT

from collections import namedtuple
from functools import partial

from myApp.game import ROWS, COLUMNS
from myApp.game import Game

MASTER_SZ = M_WIDTH, M_HEIGHT = 620, 500

DARK = "#111a1e"
LIGHT = "#142229"
GREEN = "#6cd777"

LF_dark = partial(LabelFrame, bd=3, relief=GROOVE, bg=DARK, fg=GREEN)
L_dark = partial(Label, bd=3, relief=GROOVE, bg=DARK, fg=GREEN)

master = Tk()



def main():
    baseFrame = LF_dark(master, padx=3, pady=3)

    titleFrame = LF_dark(baseFrame)
    title = L_dark(titleFrame, bd=0, text="The Game of Life", font="Silom 36 bold").pack()
    titleFrame.pack(fill=X, pady=(0,3), side=TOP)
    
    gameFrame = Canvas(baseFrame, bg=LIGHT)
    w, h = 600, 380
    for i in range(0, w, 10):
        gameFrame.create_line([(i, 0), (i, h)], tag='grid_line')

    for i in range(0, h, 10):
        gameFrame.create_line([(0, i), (w, i)], tag='grid_line')

    gameFrame.pack(expand="yes", fill=BOTH, pady=3, padx=3)
    gameFrame.bind('<Configure>', func=get_info)
    gameFrame.bind('<Button-1>', func=lambda: p)

    seedBtnFrame = LF_dark(baseFrame)
    seedBtn = Button(seedBtnFrame, text="FEED ME", bd=0, bg=DARK, fg=GREEN, command=master.quit,
                     highlightcolor=DARK, highlightbackground=DARK, highlightthickness=0)
    seedBtn.pack(side=BOTTOM, pady=3)
    seedBtnFrame.pack(fill=BOTH, side=BOTTOM, pady=(3,0))


    baseFrame.pack(fill=BOTH, expand="yes")

    master.update()
    master.resizable(False, False)
    master.geometry(f"{M_WIDTH}x{M_HEIGHT}+50+250")
    # master.after(4000, lambda: master.quit())
    master.mainloop()


    

def get_info(event):
    w = event.width
    h = event.height

    print(f"Width: {w}, Height: {h}")
