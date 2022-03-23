import tkinter
import tkinter.messagebox


class Grades:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # CONFIGURE THE MAIN WINDOW
        self.main_window.geometry("600x300")
        self.main_window.title("Input Demo")
        self.main_window.config(bg="green")
        # Create each frame
        self.test1_frame = tkinter.Frame(self.main_window)

        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.average_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # create input for test 1
        self.prompt_test1 = tkinter.Label(
            self.test1_frame, text="Enter the score for test 1:"
        )
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)

        self.prompt_test1.pack(side="left")
        self.test1_entry.pack(side="left")

        # Create input for Test 2
        self.prompt_test2 = tkinter.Label(
            self.test2_frame, text="Enter the score for test 2:"
        )
        self.test2_entry = tkinter.Entry(self.test2_frame, width=10)

        self.prompt_test2.pack(side="left")
        self.test2_entry.pack(side="left")

        # create input for test 3
        self.prompt_test3 = tkinter.Label(
            self.test3_frame, text="Enter the score for test 3:"
        )
        self.test3_entry = tkinter.Entry(self.test3_frame, width=10)

        self.prompt_test3.pack(side="left")
        self.test3_entry.pack(side="left")

        # Create average
        self.description_label = tkinter.Label(self.average_frame, text="Average")

        self.avg_var = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.average_frame, textvariable=self.avg_var)

        self.description_label.pack(side="left")
        self.avg_label.pack(side="left")

        # Create buttons
        self.avgbutton = tkinter.Button(
            self.button_frame, text="Average", command=self.average
        )

        self.quit_button = tkinter.Button(
            self.button_frame, text="Quit", command=self.main_window.destroy
        )

        self.avgbutton.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack all frames
        self.test1_frame.pack(side="top")
        self.test2_frame.pack(side="top")
        self.test3_frame.pack(side="top")
        self.average_frame.pack(side="top")
        self.button_frame.pack(side="top")
        # self.mybutton.pack(side="top")
        # self.quit_button.pack(side="top")

        tkinter.mainloop()

    def average(self):
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())
        avg = (test1 + test2 + test3) / 3

        self.avg_var.set(round(avg, 2))

        # keeps display looped until you close out of the window


my_gui = Grades()

print("moving on....")
