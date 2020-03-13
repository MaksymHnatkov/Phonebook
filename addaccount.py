from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import re

conn = sqlite3.connect('phonebook.db')
curs = conn.cursor()


class AddAccounts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x450+400+150")
        self.title("Создание контакта")
        self.resizable(False, False)

        self.top = Frame(self, height=120, bg='blue')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=330, bg='#abedbc')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='     Создание контакта', font='arial 20 bold', bg='blue', fg='white')
        self.heading.place(x=160, y=45)
        self.top_image = PhotoImage(file='/Users/HomelessRacoon/PycharmProjects/Phonebook/icons/accounts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=80, y=18)

        # Имя
        self.label_name = Label(self.bottom, text="Имя", font='arial 15', fg='black', bg='#abedbc')
        self.label_name.place(x=98, y=43)
        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.place(x=147, y=40)

        # Фамилия
        self.label_surname = Label(self.bottom, text="Фамилия", font='arial 15', fg='black', bg='#abedbc')
        self.label_surname.place(x=62, y=83)
        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.place(x=147, y=80)

        # Номер
        self.label_number = Label(self.bottom, text="Номер телефона", font='arial 15', fg='black', bg='#abedbc')
        self.label_number.place(x=7, y=123)
        self.entry_number = Entry(self.bottom, width=30, bd=4)
        self.entry_number.place(x=147, y=120)

        # Комментарии
        self.label_comment = Label(self.bottom, text="Комментарии", font='arial 15', fg='black', bg='#abedbc')
        self.label_comment.place(x=32, y=163)
        self.entry_comment = Entry(self.bottom, width=30, bd=4)
        self.entry_comment.place(x=147, y=160)

        # Кнопки
        saveButton = Button(self.bottom, text="  Сохранить контакт  ", font='arial 20 bold', command=self.add_contact)
        saveButton.place(x=170, y=235)
        quitButton = Button(self.bottom, text="  Выход  ", font='arial 20 bold', command=self.destroy)
        quitButton.place(x=230, y=285)

    def exit(self):
        self.destroy()

    def add_contact(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        number = self.entry_number.get()
        comment = self.entry_comment.get()
        match = re.fullmatch(r'\D+', number)

        if name != "" and number != "":
            answer = mb.askyesno(title="Сохранить", message="Сохранить данные?")
            try:
                if answer == True and match == None:
                    query = "insert into 'phonebook' (person_name, person_surname, tel_number, comments) values(?,?,?,?)"
                    curs.execute(query, (name.upper(), surname.upper(), str(number), comment))
                    self.entry_name.delete(0, END)
                    self.entry_surname.delete(0, END)
                    self.entry_number.delete(0, END)
                    self.entry_comment.delete(0, END)
                    conn.commit()
                    mb.showinfo("Сохранение", "Контакт успешно добавлен", icon='info')
                elif match != None:
                    mb.showerror("Ошибка!", "Проверьте правильность написания номера!", icon='warning')
                    self.entry_number.delete(0, END)



            except Exception as e:
                mb.showerror("Ошибка!", str(e))
        else:
            mb.showerror("Ошибка!", "Заполните поля Имя и Номер телефона!", icon='warning')




















