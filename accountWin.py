from tkinter import *
import sqlite3

conn = sqlite3.connect('phonebook.db')
curs = conn.cursor()


class Accounts (Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("450x450+400+150")
        self.title("Контакты")
        self.resizable(False, False)

        self.top = Frame(self, height=80, bg='blue')
        self.top.pack(fill=X)
        self.mid = Frame(self, height=260, bg='white')
        self.mid.pack(fill=X)
        self.bottom = Frame(self, height=110, bg='grey')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Контакты', font='arial 20 bold', bg='blue', fg='white')
        self.heading.place(x=180, y=25)
        self.top_image = PhotoImage(file='icons/accounts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=100, y=8)

        self.updButton = Button(self.bottom, text=" Редактировать ", font='arial 18 bold')
        self.updButton.place(x=20, y=55)
        self.delButton = Button(self.bottom, text="   Удалить   ", font='arial 18 bold')
        self.delButton.place(x=200, y=55)
        self.quitButton = Button(self.bottom, text="   Выход   ", font='arial 18 bold')
        self.quitButton.place(x=340, y=55)
        self.showButton = Button(self.bottom, text="                Детали                ", font='arial 18 bold')
        self.showButton.place(x=115, y=15)


        self.scroll = Scrollbar(self.mid, orient=VERTICAL, )
        self.listBox = Listbox(self.mid, width=48, height=16)
        self.listBox.grid(row=0, column=0, padx=(2,0))

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        self.scroll.grid(row=0, column=1, sticky=N + S)








