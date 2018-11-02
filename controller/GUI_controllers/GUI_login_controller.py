
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
        main_frame.current_frame = login_UI()
        # main_frame.current_frame.login_but.config(command=lambda: self.Enter())


    # def Enter(self):
    #     acc_id = str(main_frame.current_frame.account_entry.get())
    #     pin = str(main_frame.current_frame.pin_entry.get())
    #     if login_model().check_login(acc_id, pin) == 0:
    #         main_frame.current_ctr = option_controller(self.master, acc_id)
    #     else:
    #         message = 'Incorrect Login'
    #         messagebox.showinfo(title='Error', message=message)


if __name__ == "__main__":
    root = Tk()
    frame = login_UI(root)
    # ui = login_controller(root, frame)
    mainloop()