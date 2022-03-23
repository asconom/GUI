import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # CONFIGURE THE MAIN WINDOW
        self.main_window.geometry("500x200")
        self.main_window.title("Label Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # create three intvar objects to use with the checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # set the intvar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.top_frame, text="Option 1", variable=self.cb_var1
        )

        self.cb2 = tkinter.Checkbutton(
            self.top_frame, text="Option 2", variable=self.cb_var2
        )

        self.cb3 = tkinter.Checkbutton(
            self.top_frame, text="Option 3", variable=self.cb_var3
        )

        self.mybutton = tkinter.Button(
            self.button_frame, text="Click Me!", command=self.do_something
        )

        self.quit_button = tkinter.Button(
            self.button_frame, text="Quit", command=self.main_window.destroy
        )

        self.mybutton.pack(side="left")
        self.quit_button.pack(side="left")

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")
        self.button_frame.pack(side="top")
        # self.mybutton.pack(side="top")
        # self.quit_button.pack(side="top")

        tkinter.mainloop()

    def do_something(self):
        self.message = "You have selected:\n"

        if self.cb_var1.get() == 1:
            self.message += "1\n"
        if self.cb_var2.get() == 1:
            self.message += "2\n"
        if self.cb_var3.get() == 1:
            self.message += "3\n"

        tkinter.messagebox.showinfo("Response", self.message)

        # keeps display looped until you close out of the window


my_gui = MyGUI()

print("moving on....")
