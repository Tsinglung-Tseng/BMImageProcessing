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
        self.create_widgets()

    def create_widgets(self):
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


class Filtering(ttk.Frame):
    def __init__(self, window):
        ttk.Frame.__init__(self, window)
        self.grid()
        self.create_widgets() 
    
    def create_widgets(self):
        self.working_image = None
        
        def load_image(event):
            img_key = self.combobox_img.get()
            print(img_key)
            self.working_image = IMG.IO[img_key]
            
        def load_kernel_direction(event):
            self.kernel_direction = self.combobox_direction.get()
            print(f"Load direction: {self.kernel_direction}")

        def load_kernel_type(event):
            self.kernel_type = self.combobox_kernel_type.get()
            print(f"Load direction: {self.kernel_type}")
            
        self.label_p = Label(self, text="Please select a picture.")
        self.label_p.grid(row=0, column=1, sticky=W)

        self.combobox_img = ttk.Combobox(self, values=[k for k, _ in IMG.IO.items()])
        self.combobox_img.grid(row=1, column=1)
        self.combobox_img.bind("<<ComboboxSelected>>", load_image)

        self.label_d = Label(self, text="Please select direction.")
        self.label_d.grid(row=2, column=1, sticky=W)

        self.combobox_direction = ttk.Combobox(self, values=['x', 'y'])
        self.combobox_direction.grid(row=3, column=1)
        self.combobox_direction.bind("<<ComboboxSelected>>", load_kernel_direction)

        self.label_t = Label(self, text="Please select filter type.")
        self.label_t.grid(row=4, column=1, sticky=W)

        self.combobox_kernel_type = ttk.Combobox(self, values=['roberts', 'prewitt', 'sobel'])
        self.combobox_kernel_type.grid(row=5, column=1)
        self.combobox_kernel_type.bind("<<ComboboxSelected>>", load_kernel_type)

        self.bt_hist = Button(self, text="Do Fitering", width=22, command=self.run_filtering)
        self.bt_hist.grid(row=6, column=1, sticky=W)

    def run_filtering(self):
        import matplotlib.pyplot as plt
        from filtering import convolution, Kernel, Image

        img = self.working_image()
        plt.figure()
        plt.imshow(img, cmap='gray')
        plt.title("Origin Image")
        plt.savefig(SHOW.ORIGIN)

        plt.figure()
        print(self.kernel_direction)
        print(self.kernel_type)
        filtered_img = convolution(Image(img), Kernel())
        plt.imshow(filtered_img, cmap='gray')
        plt.title("Filtered Image")
        plt.savefig(SHOW.FILTERED)
        self.show_img()

    def show_img(self):
        self.origin = PhotoImage(file=SHOW.ORIGIN)
        self.origin_label = Label(image=self.origin)
        self.origin_label.image = self.origin
        self.origin_label.grid(row=0, column=2, sticky=W)

        self.filtered = PhotoImage(file=SHOW.FILTERED)
        self.filtered_label = Label(image=self.filtered)
        self.filtered_label.image = self.filtered
        self.filtered_label.grid(row=0, column=6, sticky=W)



def main():
    # Setup Tk()
    global window
    window = Tk()

    # Setup the notebook (tabs)
    notebook = ttk.Notebook(window)
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    notebook.add(frame1, text="Binary")
    notebook.add(frame2, text="Filtering")
    notebook.grid()

    # Create tab frames
    binary = Binary(window=frame1)
    binary.grid()
    filtering = Filtering(window=frame2)
    filtering.grid()

    # Main loop
    window.mainloop()

if __name__ == "__main__":
    main()