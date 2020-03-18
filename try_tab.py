from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BMICalcApp(ttk.Frame):
    """ This application calculates BMI and returns a value. """

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # text variables
        self.i_height = StringVar()
        self.i_weight = StringVar()
        self.o_bmi = StringVar()

        # labels
        self.label1 = ttk.Label(self, text="Enter your weight:").grid(
            row=0, column=0, sticky=W
        )
        self.label2 = ttk.Label(self, text="Enter your height:").grid(
            row=1, column=0, sticky=W
        )
        self.label3 = ttk.Label(self, text="Your BMI is:").grid(
            row=2, column=0, sticky=W
        )

        # text boxes
        self.textbox1 = ttk.Entry(self, textvariable=self.i_weight).grid(
            row=0, column=1, sticky=E
        )
        self.textbox2 = ttk.Entry(self, textvariable=self.i_height).grid(
            row=1, column=1, sticky=E
        )
        self.textbox3 = ttk.Entry(self, textvariable=self.o_bmi).grid(
            row=2, column=1, sticky=E
        )

        # buttons
        self.button1 = ttk.Button(self, text="Ok", command=self.calculateBmi).grid(
            row=3, column=2, sticky=E
        )
        self.button2 = ttk.Button(
            self, text="Cancel/Quit", command=window.destroy
        ).grid(row=3, column=1, sticky=E)

    def calculateBmi(self):
        try:
            self.weight = float(self.i_weight.get())
            self.height = float(self.i_height.get())
            self.bmi = self.weight / self.height ** 2.0
            self.o_bmi.set(self.bmi)
        except ValueError:
            messagebox.showinfo("Error", "You can only use numbers.")
        finally:
            self.i_weight.set("")
            self.i_height.set("")


class ConvertFeetMeters(ttk.Frame):
    """ Application to convert feet to meters or vice versa. """

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the GUI"""
        # 1 textbox (stringvar)
        self.entry = StringVar()
        self.textBox1 = ttk.Entry(self, textvariable=self.entry).grid(row=0, column=1)

        # 5 labels (3 static, 1 stringvar)
        self.displayLabel1 = ttk.Label(self, text="feet").grid(
            row=0, column=2, sticky=W
        )
        self.displayLabel2 = ttk.Label(self, text="is equivalent to:").grid(
            row=1, column=0
        )
        self.result = StringVar()
        self.displayLabel3 = ttk.Label(self, textvariable=self.result).grid(
            row=1, column=1
        )
        self.displayLabel4 = ttk.Label(self, text="meters").grid(
            row=1, column=2, sticky=W
        )

        # 2 buttons
        self.calculateButton = ttk.Button(
            self, text="Calculate", command=self.convert_feet_to_meters
        ).grid(row=2, column=2, sticky=(S, E))
        # self.quitButton = ttk.Button(self, text="Quit", command=window.destroy).grid(
        #     row=2, column=1, sticky=(S, E)
        # )

    def convert_feet_to_meters(self):
        """Converts feet to meters, uses string vars and converts them to floats"""
        self.measurement = float(self.entry.get())
        self.meters = self.measurement * 0.3048
        self.result.set(self.meters)


def main():
    # Setup Tk()
    global window
    window = Tk()

    # Setup the notebook (tabs)
    notebook = ttk.Notebook(window)
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    notebook.add(frame1, text="BMI Calc")
    notebook.add(frame2, text="Feet to Meters")
    notebook.grid()

    # Create tab frames
    bmi_calc = BMICalcApp(master=frame1)
    bmi_calc.grid()
    feet_meters_calc = ConvertFeetMeters(master=frame2)
    feet_meters_calc.grid()

    # Main loop
    window.mainloop()


if __name__ == "__main__":
    main()
