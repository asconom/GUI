import tkinter
from turtle import left


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # CONFIGURE THE MAIN WINDOW
        self.main_window.geometry("500x200")
        self.main_window.title("Label Demo")

        
        self.label1 = tkinter.Label(self.main_window, text="Hello World!")

        self.label2 = tkinter.Label(self.main_window, text="This is my GUI program")

        self.label1.pack(side="top")
        self.label2.pack(side="bottom")

        tkinter.mainloop()
        # keeps display looped until you close out of the window


my_gui = MyGUI()

print("moving on....")
