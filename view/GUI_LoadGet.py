from tkinter import *
from .GUI_baseUI import UI


class LoadGet_UI(UI):

    """
        The chequing or savigns page
        Has 2 buttons cheq or savigns
    """

    def __init__(self, master, img):
        super().__init__(master, img)


        # ------------------MID FRAME ----------------------------------
        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(2, weight=1)

        self.mid_frame.grid_rowconfigure(0, weight=0)
        self.mid_frame.grid_rowconfigure(1, weight=1)

        self.CS_frame = Frame(self.mid_frame)

        self.header_label = Label(self.mid_frame, text='', font=("TkDefaultFont", 12, 'bold'))

        self.get_but = Button(self.CS_frame, text='Get Scans', width=10)
        self.load_but = Button(self.CS_frame, text='Load Scans', width=10)

        self.header_label.grid(row=0, column=1, pady=10)
        self.CS_frame.grid(row=1, column=1)
        self.get_but.grid(row=0, column=0, padx=20)
        self.load_but.grid(row=0, column=1, padx=20)

        # -------------Bottom FRAME ---------------------------------------------
        self.botbut_frame.grid_rowconfigure(0, weight=1)
        self.botbut_frame.grid_rowconfigure(2, weight=1)

        self.botbut_frame.grid_columnconfigure(0, weight=1)
        self.botbut_frame.grid_columnconfigure(1, weight=0)

        self.can_but = Button(self.botbut_frame, text='Exit', width=10)
        self.can_but.grid(row=1, column=1, padx=30, pady=15)


if __name__ == "__main__":
    root = Tk()
    LoadGet_UI(root)
    mainloop()
