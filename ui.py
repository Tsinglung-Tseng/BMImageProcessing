from tkinter import *
from tkinter import ttk
import sys
from binary import Otsu, Entropy
from config import SHOW, IMG


class App:
    def __init__(self, window):
        self.working_image = None

        def load_image(event):
            img_key = combobox_img.get()
            print(img_key)
            self.working_image = IMG.IO[img_key]

        def print_selection(i):
            label.config(text=f"You have selected {i}")
            self.gray_slider = int(i)

        combobox_img = ttk.Combobox(window, values=[k for k, _ in IMG.IO.items()])
        combobox_img.grid(row=0, column=1)
        combobox_img.bind("<<ComboboxSelected>>", load_image)

        label = Label(window, text="Please select a threshold.")
        label.grid(row=1, column=1, sticky=W)

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
        gray_level_slider.grid(row=2, column=1)

        bt_hist = Button(window, text="Do Binary", width=22, command=self.run_binary)
        bt_hist.grid(row=3, column=1, sticky=W)

        bt_otsu = Button(window, text="Otsu", width=22, command=self.run_otsu)
        bt_otsu.grid(row=4, column=1, sticky=W)

        bt_entropy = Button(window, text="Entropy", width=22, command=self.run_entropy)
        bt_entropy.grid(row=5, column=1, sticky=W)
        self.show_img()

    def show_img(self):
        hist = PhotoImage(file=SHOW.HIST)
        hist_label = Label(image=hist)
        hist_label.image = hist
        hist_label.grid(row=4, column=2, columnspan=4, rowspan=4)

        origin = PhotoImage(file=SHOW.ORIGIN)
        origin_label = Label(image=origin)
        origin_label.image = origin
        origin_label.grid(row=0, column=2, rowspan=4)

        binary = PhotoImage(file=SHOW.BINARY)
        binary_label = Label(image=binary)
        binary_label.image = binary
        binary_label.grid(row=0, column=6, columnspan=4, rowspan=4)

    def run_otsu(self):
        print("otsu runs")
        Otsu(self.working_image())()
        self.show_img()

    def run_entropy(self):
        print("entropy runs")
        Entropy(self.working_image())()
        self.show_img()

    def run_binary(self):
        print("manual binary rnus")
        Otsu(self.working_image())(self.gray_slider)
        self.show_img()


window = Tk()
window.title("ImageProcessing")
window.geometry("1070x600")
display = App(window)
window.mainloop()
