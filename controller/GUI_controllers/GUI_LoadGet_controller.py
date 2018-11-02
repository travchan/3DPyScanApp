from tkinter import *

from view import LoadGet_UI
from view import main_frame
# from .GUI_butt_functions import Cancel_func
# from .GUI_deposit_controller import dep_controller
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
        self.option = 'adas'
        self.acc_id = 'adad'

        main_frame.current_frame = LoadGet_UI(self.master)
        # if self.option == "Withdraw":
        #     main_frame.current_frame.cheq_but.config(command=lambda: self.To_withdraw_cheq(self.option))
        #     main_frame.current_frame.save_but.config(command=lambda: self.To_withdraw_save(self.option))
        # elif self.option == "Deposit":
        #     main_frame.current_frame.cheq_but.config(command=lambda: self.To_deposit_cheq(self.option))
        #     main_frame.current_frame.save_but.config(command=lambda: self.To_deposit_save(self.option))
        #
        # main_frame.current_frame.can_but.config(command=lambda: self.Cancel(self.master))


    # def To_withdraw_cheq(self, option):
    #     account = "Chequing"
    #     main_frame.current_ctr = with_controller(self.master, option, account, self.acc_id)
    #
    # def To_withdraw_save(self, option):
    #     account = "Savings"
    #     main_frame.current_ctr = with_controller(self.master, option, account, self.acc_id)
    #
    # def To_deposit_cheq(self, option):
    #     account = "Chequing"
    #     main_frame.current_ctr = dep_controller(self.master, option, account, self.acc_id)
    #
    # def To_deposit_save(self, option):
    #     account = "Savings"
    #     main_frame.current_ctr = dep_controller(self.master, option, account, self.acc_id)
    #
    # def Cancel(self, master):
    #     Cancel_func(master, self.acc_id)

if __name__ == "__main__":
    root = Tk()
    frame = CorS_UI(root)
    ui = LoadGet_controller(root)
    mainloop()
