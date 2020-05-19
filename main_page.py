from tkinter import *
from tkinter import ttk
from ui import App as Binary
from try_tab import ConvertFeetMeters


def main():
    # Setup Tk()
    # global window
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
