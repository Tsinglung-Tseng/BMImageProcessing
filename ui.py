from tkinter import *
import sys
# sys.path('./')
from binary import Otsu
from config import SHOW


class App:
    def __init__(self, window):
        label = Label(window, text="Hello GUI!")
        label.grid(row=0, column=1, sticky=W)

        def print_selection(i):
            label.config(text=f"You have selected {i}")

        def run_otsu(img):
            return Otsu(img)

        gray_level_slider = Scale(
            window,
            label="Gray Scale",
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=200,
            showvalue=0,
            tickinterval=64,
            command=print_selection,
        )
        gray_level_slider.grid(row=1, column=1)

        bt_otsu = Button(window, text='Otsu', width = 22, command=)
        bt_otsu.grid(row=2, column=1, sticky=W)


window = Tk()
window.title("ImageProcessing")
window.geometry("500x300")
display = App(window)
window.mainloop()
