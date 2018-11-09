from tkinter import *

class login_error():

    def __init__(self):
        self.master = Tk()
        self.screenW = str(int(self.master.winfo_screenwidth()/7))
        self.screenH = str(int(self.master.winfo_screenheight()/6))
        self.master.geometry(self.screenW + "x" + self.screenH)
        self.master.resizable(0, 0)
        self.master.title("Login Error")

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=0)
        self.master.grid_columnconfigure(0, weight=1)

        # -------------------FRAMES---------------------------------
        self.title_frame = Frame(self.master, width=self.screenW)
        self.mid_frame = Frame(self.master, width=self.screenW)
        self.botbut_frame = Frame(self.master, width=self.screenW)

        self.title_frame.grid(row=0, sticky='nsew')
        self.mid_frame.grid(row=1, sticky='nsew')
        self.botbut_frame.grid(row=2, sticky='nsew')

        # -------------------MID FRAME------------------------------
        # makes boarders to center the input frame
        self.mid_frame.grid_rowconfigure(0, weight=1)
        self.mid_frame.grid_rowconfigure(3, weight=1)

        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(3, weight=1)

        self.error_msg = Label(self.mid_frame, text="Login Failed. \n Invalid Email or Password")

        self.error_msg.grid(row=1, column=0, sticky=E, padx=2, pady=2)

        # -------------BOTTOM FRAME ---------------------------------------------
        self.botbut_frame.grid_rowconfigure(0, weight=1)
        self.botbut_frame.grid_rowconfigure(2, weight=1)

        self.botbut_frame.grid_columnconfigure(0, weight=0)
        self.botbut_frame.grid_columnconfigure(1, weight=1)
        self.botbut_frame.grid_columnconfigure(2, weight=0)

        self.ok_but = Button(self.botbut_frame, text='Ok', width=8)
        self.ok_but.grid(row=1, column=1, padx=30, pady=15)


if __name__ == "__main__":
    login_error()
    mainloop()