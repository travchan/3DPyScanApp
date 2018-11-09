
from tkinter import *
from tkinter import messagebox

# from model.GUI_model.GUI_login_model import login_model
from view import login_UI
from view import main_frame
from view import login_error
from view import login_success

# from .GUI_option_controller import option_controller

from model import MailParser

class login_controller:

    """
        The login GUI controller.
        It creates the login UI
        Contains functions that the UI's buttons will use.

        gets the login info
    """

    def __init__(self):
        self.UI = login_UI()
        self.UI.get_but.config(command=self._login)
        self.UI.can_but.config(command=lambda: self.exit())

    def _login(self):
        user_email = str(self.UI.account_entry.get())
        user_pass = str(self.UI.pin_entry.get())

        mail = MailParser(user_email, user_pass)
        log_status = mail.getMail()
        
        if log_status == None:
            self.error = login_error()
            self.error.ok_but.config(command=lambda: self.error.master.destroy())
        else:
            self.success = login_success()
            self.success.ok_but.config(command=lambda: self.success.master.destroy())
            self.exit()

    def exit(self):
        self.UI.master.destroy()


if __name__ == "__main__":
    # root = Tk()
    frame = login_UI()
    # ui = login_controller(root, frame)
    mainloop()