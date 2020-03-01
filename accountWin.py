from tkinter import *

class Accounts (Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("450x450+400+150")
        self.title("Контакты")
        self.resizable(False, False)
