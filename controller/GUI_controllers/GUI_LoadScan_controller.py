from tkinter import *
from tkinter.filedialog import askopenfilename

from view import LoadScan_UI
from view import main_frame
from model import ModelClassifier


class LoadScan_controller:

    """
        The Chequing or savings GUI controller.
        It creates the Chequing or savings UI
        Contains functions that the UI's buttons will use.

        decides which account is subjected to the option of withdraw or deposit
    """


    def __init__(self, master):
        self.master = master
        self.img = './view/BCIT_Logo.png'


        main_frame.current_frame = LoadScan_UI(self.master, self.img)
        main_frame.current_frame.Open_but.config(command=lambda: self.openFile())
        main_frame.current_frame.can_but.config(command=lambda: self.Exit())

    def openFile(self):
        filename = askopenfilename(initialdir="C:/Users/public/scans/", title="Select a file")
        main_frame.current_frame.log_File_Path.set(filename)
        ModelClassifier(filename).classify()




    def Exit(self):
        from .GUI_LoadGet_controller import LoadGet_controller
        LoadGet_controller(self.master)


if __name__ == "__main__":
    root = Tk()
    frame = CorS_UI(root)
    ui = LoadGet_controller(root)
    mainloop()
