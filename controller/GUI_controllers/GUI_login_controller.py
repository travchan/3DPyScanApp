
from tkinter import *
from tkinter import messagebox

# from model.GUI_model.GUI_login_model import login_model
from view import login_UI
from view import main_frame

# from .GUI_option_controller import option_controller


class login_controller:

    """
        The login GUI controller.
        It creates the login UI
        Contains functions that the UI's buttons will use.

        gets the login info
    """

    def __init__(self):
        self.UI = login_UI()
        self.UI.can_but.config(command=lambda: self.exit())


    def exit(self):
        self.UI.master.destroy()


if __name__ == "__main__":
    # root = Tk()
    frame = login_UI()
    # ui = login_controller(root, frame)
    mainloop()