from tkinter import *

from view import LoadGet_UI
from view import main_frame

from .GUI_login_controller import login_controller
# from .GUI_withdraw_controller import with_controller


class LoadGet_controller:

    """
        The Chequing or savings GUI controller.
        It creates the Chequing or savings UI
        Contains functions that the UI's buttons will use.

        decides which account is subjected to the option of withdraw or deposit
    """


    def __init__(self, master):
        self.master = master
        self.img = './view/BCIT_Logo.png'


        main_frame.current_frame = LoadGet_UI(self.master, self.img)
        main_frame.current_frame.get_but.config(command=lambda: self.openEmail())
        # main_frame.current_frame.load_but.config(command=lambda: self.To_withdraw_save(self.option))
        main_frame.current_frame.can_but.config(command=lambda: self.Exit())

    def openEmail(self):
        login_controller()

    def Exit(self):
        self.master.master.destroy()

if __name__ == "__main__":
    root = Tk()
    frame = CorS_UI(root)
    ui = LoadGet_controller(root)
    mainloop()
