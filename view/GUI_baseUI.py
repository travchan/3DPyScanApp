from tkinter import *

class UI:

    """
        The base UI where other UI inherits from.
        has an outline with 4 rows, the middle one having weight to it
        Top row has the title "BANK OF D.H.E" and the underline to seperate the title block
    """

    def __init__(self, master):
        # self.ATM = ATM()
        self.master = master
        self.screenW = '480'
        self.screenH = '320'
        # self.master.title('ATM')
        # self.master.resizable(0, 0)

        # weight makes it so that the row or column is stretched to fill empty space left over in master frame
        # in this case row
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)
        # row 2 is the section inbetween the title bock and the bottom buttons
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=0)

        # -------------------FRAMES---------------------------------
        self.title_frame = Frame(self.master, width=self.screenW)
        self.title_divide = Frame(self.master, width=self.screenW, height=4, background='black')
        self.mid_frame = Frame(self.master, width=self.screenW)
        self.botbut_frame = Frame(self.master, width=self.screenW)

        # stretches the frames to the max (screenW)
        self.title_frame.grid(row=0, sticky='nsew')
        self.title_divide.grid(row=1, sticky='nsew')
        self.mid_frame.grid(row=2, sticky='nsew')
        self.botbut_frame.grid(row=3, sticky='nsew')

        # self.title_frame.config(background="red")
        # self.botbut_frame.config(background="pink")

        # #----------------TITLE FRAME--------------------------------
        # makes boarders to center the title label
        self.title_frame.grid_rowconfigure(0, weight=1)
        self.title_frame.grid_rowconfigure(2, weight=1)

        self.title_label = Label(self.title_frame, text='Bank of D.H.E', font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=1, column=1, padx=10, pady=10)



if __name__ == "__main__":
    root = Tk()
    UI(root)
    mainloop()
