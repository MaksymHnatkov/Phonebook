from tkinter import *
from tkinter import messagebox as mb
import sqlite3

conn = sqlite3.connect('phonebook.db')
curs = conn.cursor()

class AddAccounts (Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x450+400+150")
        self.title("Создание контакта")
        self.resizable(False, False)

        self.top = Frame(self, height=80, bg='blue')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=370, bg='#c2c0ba')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Создание контакта', font='arial 20 bold', bg='blue', fg='white')
        self.heading.place(x=160, y=25)
        self.top_image = PhotoImage(file='icons/accounts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=80, y=8)

        # Имя
        self.label_name = Label(self.bottom, text="Имя", font='arial 15', fg='white', bg='#c2c0ba')
        self.label_name.place(x=100, y=43)
        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.place(x=147, y=40)

        # Номер
        self.label_number = Label(self.bottom, text="Номер телефона", font='arial 15', fg='white', bg='#c2c0ba')
        self.label_number.place(x=7, y=83)
        self.entry_number = Entry(self.bottom, width=30, bd=4)
        self.entry_number.place(x=147, y=80)

        # Комментарии
        self.label_comment = Label(self.bottom, text="Комментарии", font='arial 15', fg='white', bg='#c2c0ba')
        self.label_comment.place(x=32, y=123)
        self.entry_comment = Text(self.bottom, width=39, height=8, bd=2)
        self.entry_comment.place(x=147, y=120)

        # Кнопки
        saveButton = Button(self.bottom, text="  Сохранить контакт  ", font='arial 20 bold', command=self.add_contact)
        saveButton.place(x=170, y=275)
        quitButton = Button(self.bottom, text="  Выход  ", font='arial 20 bold', command=self.destroy)
        quitButton.place(x=230, y=315)

    def exit(self):
        self.destroy()

    def add_contact(self):
        answer = mb.askyesno(title="Сохранить", message="Сохранить данные?")
        if answer == True:
            name = self.entry_name.get()
            self.entry_name.delete(0, END)
            number = self.entry_number.get()
            self.entry_number.delete(0, END)
            comment = self.entry_comment.get(1.0, 'end -1c')
            self.entry_comment.delete(END)


















