from tkinter import *

class login_UI():

    """
        The login page
        has 2 entry fields for account # and pin
        pin is restricted to 4 characters by StringVar, trace and textvariable
        that allows it to be checked by limitEntry Size with every key press
    """


    def __init__(self):
        self.master = Tk()
        self.screenW = str(int(self.master.winfo_screenwidth()/4))
        self.screenH = str(int(self.master.winfo_screenheight()/4))
        self.master.geometry(self.screenW + "x" + self.screenH)
        self.master.resizable(0, 0)
        self.master.title('PyScan')

        # self.master.after(1, lambda: self.master.focus_force())

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=0)
        self.master.grid_columnconfigure(0, weight=1)

        # -------------------FRAMES---------------------------------
        self.title_frame = Frame(self.master, width=self.screenW)
        self.mid_frame = Frame(self.master, width=self.screenW)
        self.botbut_frame = Frame(self.master, width=self.screenW)

        # self.title_frame.configure(background='black')



        # stretches the frames to the max (screenW)
        self.title_frame.grid(row=0, sticky='nsew')
        self.mid_frame.grid(row=1, sticky='nsew')
        self.botbut_frame.grid(row=2, sticky='nsew')

        # #----------------TITLE FRAME---------------------------------
        self.title_frame.grid_rowconfigure(0, weight=1)
        self.title_frame.grid_rowconfigure(2, weight=1)
        self.title_frame.grid_columnconfigure(0, weight=1)
        self.title_frame.grid_columnconfigure(2, weight=1)

        self.title_label = Label(self.title_frame, text='Get Scans From Email', font=("Helvetica", 12,))
        self.title_label.grid(row=1, column=1, padx=10, pady=10)

        # #----------------ENTRY FRAME---------------------------------
        # makes boarders to center the input frame
        self.var = IntVar()
        self.var.set(0)
  
        self.mid_frame.grid_rowconfigure(0, weight=1)
        self.mid_frame.grid_rowconfigure(3, weight=1)

        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(3, weight=1)
        
        self.account_label = Label(self.mid_frame, text='Email :')
        self.account_entry = Entry(self.mid_frame, width=30)
        self.pin_label = Label(self.mid_frame, text='Password :')
        self.pin_entry = Entry(self.mid_frame, width=30, show="*")
        self.radio_but_all = Radiobutton(self.mid_frame, text="All Scans", variable=self.var, value=0, indicatoron=1)
        self.radio_but_new = Radiobutton(self.mid_frame, text="New Scans", variable=self.var, value=1, indicatoron=1)
        self.radio_but_new.select()

        self.account_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.account_entry.grid(row=1, column=1, sticky=E, padx=5, pady=5)
        self.radio_but_all.grid(row=3, column=1, sticky=E, padx=5, pady=5)
        self.radio_but_new.grid(row=3, column=0, sticky=E, padx=5, pady=5)
        self.pin_label.grid(row=2, column=0, sticky=E, padx=5, pady=5)
        self.pin_entry.grid(row=2, column=1, sticky=E, padx=5, pady=5)

        # -------------Bottom FRAME ---------------------------------------------
        self.botbut_frame.grid_rowconfigure(0, weight=1)
        self.botbut_frame.grid_rowconfigure(2, weight=1)

        self.botbut_frame.grid_columnconfigure(0, weight=0)
        self.botbut_frame.grid_columnconfigure(1, weight=1)
        self.botbut_frame.grid_columnconfigure(2, weight=0)

        self.can_but = Button(self.botbut_frame, text='Cancel', width=10)
        self.can_but.grid(row=1, column=0, padx=30, pady=15)


        self.get_but = Button(self.botbut_frame, text='Get Scans', width=10)
        self.get_but.grid(row=1, column=2, padx=30, pady=15)


if __name__ == "__main__":
    # root = Tk()
    login_UI()
    mainloop()
