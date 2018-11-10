from tkinter import *
from .GUI_baseUI import UI


class login_UI(UI):

    """
        The login page
        has 2 entry fields for account # and pin
        pin is restricted to 4 characters by StringVar, trace and textvariable
        that allows it to be checked by limitEntry Size with every key press
    """


    def __init__(self, master, img):
        super().__init__(master, img)


        # ------------------MID FRAME ----------------------------------
        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(2, weight=1)

        self.mid_frame.grid_rowconfigure(1, weight=1)

        self.header_label = Label(self.mid_frame, text='Enter Email', font=("TkDefaultFont", 12))
        self.header_label.grid(row=0, column=1, pady=10)

        # #----------------ENTRY FRAME---------------------------------
        # makes boarders to center the input frame
        self.var = IntVar()
        self.var.set(0)

        self.account_frame = Frame(self.mid_frame)
        self.account_frame.grid(row=1, column=1)
        self.account_frame.grid_rowconfigure(0, weight=1)
        self.account_frame.grid_rowconfigure(4, weight=1)

        self.account_label = Label(self.account_frame, text='Email :')
        self.account_entry = Entry(self.account_frame, width=30)
        self.pin_label = Label(self.account_frame, text='Password :')
        self.pin_entry = Entry(self.account_frame, width=30, show="*")

        self.account_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.account_entry.grid(row=1, column=1, sticky=E, padx=5, pady=5)
        self.pin_label.grid(row=2, column=0, sticky=E, padx=5, pady=5)
        self.pin_entry.grid(row=2, column=1, sticky=E, padx=5, pady=5)


        self.radio_but_all = Radiobutton(self.account_frame, text="All Scans", variable=self.var, value=0, indicatoron=1)
        self.radio_but_new = Radiobutton(self.account_frame, text="New Scans", variable=self.var, value=1, indicatoron=1)
        self.radio_but_new.select()

        self.radio_but_all.grid(row=3, column=1, sticky=E, padx=5, pady=10)
        self.radio_but_new.grid(row=3, column=0, sticky=E, padx=5, pady=10)


        # -------------Bottom FRAME ---------------------------------------------
        self.botbut_frame.grid_rowconfigure(0, weight=1)
        self.botbut_frame.grid_rowconfigure(2, weight=1)

        self.botbut_frame.grid_columnconfigure(1, weight=1)

        self.can_but = Button(self.botbut_frame, text='Cancel', width=10)
        self.can_but.grid(row=1, column=0, padx=30, pady=15)

        self.get_but = Button(self.botbut_frame, text='Get Scans', width=10)
        self.get_but.grid(row=1, column=2, padx=30, pady=15)


if __name__ == "__main__":
    root = Tk()
    img = ""
    login_UI(root, img)
    mainloop()
