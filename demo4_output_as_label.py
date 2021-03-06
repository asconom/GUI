import tkinter
import tkinter.messagebox


class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # CONFIGURE THE MAIN WINDOW
        self.main_window.geometry("500x200")
        self.main_window.title("Input Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(
            self.top_frame, text="Enter a distance in Kilometers:"
        )
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.description_label = tkinter.Label(
            self.mid_frame, text="Converted to miles:"
        )
        self.miles_var = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.miles_var)

        self.description_label.pack(side="left")
        self.miles_label.pack(side="left")

        self.calcbutton = tkinter.Button(
            self.button_frame, text="Convert", command=self.convert
        )

        self.quit_button = tkinter.Button(
            self.button_frame, text="Quit", command=self.main_window.destroy
        )

        self.calcbutton.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack(side="top")
        self.mid_frame.pack(side="top")
        self.bottom_frame.pack(side="top")
        self.button_frame.pack(side="bottom")
        # self.mybutton.pack(side="top")
        # self.quit_button.pack(side="top")

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo * 0.6214), 2)
        self.miles_var.set(miles)

        # keeps display looped until you close out of the window


kilo_gui = KiloConverterGUI()

print("moving on....")
