from tkinter import *
import sqlite3
import re

conn = sqlite3.connect('phonebook.db')
curs = conn.cursor()

class Search(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x350+400+150")
        self.title("Поиск")
        self.resizable(False, False)

        self.top = Frame(self, height=100, bg='blue')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=250, bg='#c2c0ba')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Поиск контакта', font='arial 20 bold', bg='blue', fg='white')
        self.heading.place(x=210, y=45)
        self.top_image = PhotoImage(file='icons/accounts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=130, y=18)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.place(x=220, y=40)
        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.place(x=220, y=90)
        self.entry_comment = Entry(self.bottom, width=30, bd=4)
        self.entry_comment.place(x=220, y=140)

        #Кнопки поиска
        nameButton = Button(self.bottom, text="   Поиск по имени   ", font='arial 20 bold')
        nameButton.place(x=10, y=43)
        surnameButton = Button(self.bottom, text="Поиск по фамилии ", font='arial 20 bold')
        surnameButton.place(x=10, y=93)
        numberButton = Button(self.bottom, text="  Поиск по номеру  ", font='arial 20 bold')
        numberButton.place(x=10, y=143)

        quitButton = Button(self.bottom, text="  Выход  ", font='arial 20 bold', command=self.destroy)
        quitButton.place(x=230, y=200)

    def exit(self):
        self.destroy()