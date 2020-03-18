from tkinter import *
from tkinter import ttk
import sys
from binary import Otsu, Entropy
from config import SHOW, IMG

from try_tab import ConvertFeetMeters


class Binary(ttk.Frame):
    def __init__(self, window):
        ttk.Frame.__init__(self, window)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.working_image = None

        def load_image(event):
            img_key = self.combobox_img.get()
            print(img_key)
            self.working_image = IMG.IO[img_key]

        def print_selection(i):
            self.label.config(text=f"You have selected {i}")
            self.gray_slider = int(i)

        self.combobox_img = ttk.Combobox(self, values=[k for k, _ in IMG.IO.items()])
        self.combobox_img.grid(row=0, column=1)
        self.combobox_img.bind("<<ComboboxSelected>>", load_image)

        self.label = Label(self, text="Please select a threshold.")
        self.label.grid(row=1, column=1, sticky=W)

        self.gray_level_slider = Scale(
            self,
            label="Gray Scale",
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=200,
            showvalue=0,
            tickinterval=64,
            command=print_selection,
        )
        self.gray_level_slider.grid(row=2, column=1)

        self.bt_hist = Button(self, text="Do Binary", width=22, command=self.run_binary)
        self.bt_hist.grid(row=3, column=1, sticky=W)

        self.bt_otsu = Button(self, text="Otsu", width=22, command=self.run_otsu)
        self.bt_otsu.grid(row=4, column=1, sticky=W)

        self.bt_entropy = Button(self, text="Entropy", width=22, command=self.run_entropy)
        self.bt_entropy.grid(row=5, column=1, sticky=W)
        self.show_img()

    def show_img(self):
        self.hist = PhotoImage(file=SHOW.HIST)
        self.hist_label = Label(image=self.hist)
        self.hist_label.image = self.hist
        self.hist_label.grid(row=4, column=2, sticky=W)

        self.origin = PhotoImage(file=SHOW.ORIGIN)
        self.origin_label = Label(image=self.origin)
        self.origin_label.image = self.origin
        self.origin_label.grid(row=0, column=2, sticky=W)

        self.binary = PhotoImage(file=SHOW.BINARY)
        self.binary_label = Label(image=self.binary)
        self.binary_label.image = self.binary
        self.binary_label.grid(row=0, column=6, sticky=W)

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


# window = Tk()
# window.title("ImageProcessing")
# window.geometry("1070x600")
# display = App(window)
# window.mainloop()
def main():
    # Setup Tk()
    global window
    window = Tk()

    # Setup the notebook (tabs)
    notebook = ttk.Notebook(window)
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    notebook.add(frame1, text="Binary")
    notebook.add(frame2, text="Feet to Meters")
    notebook.grid()

    # Create tab frames
    binary = Binary(window=frame1)
    binary.grid()
    feet_meters_calc = ConvertFeetMeters(master=frame2)
    feet_meters_calc.grid()

    # Main loop
    window.mainloop()

if __name__ == "__main__":
    main()