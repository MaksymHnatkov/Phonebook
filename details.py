from tkinter import *
from updAccount import Update
from tkinter import messagebox as mb
import sqlite3

conn = sqlite3.connect('phonebook.db')
curs = conn.cursor()


class Details(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry("550x450+400+150")
        self.title("Детали")
        self.resizable(False, False)

        query = "select * from phonebook where person_id = '{}'".format(person_id)
        result = curs.execute(query).fetchone()
        self.person_id = person_id
        person_name = result[1]
        person_surname = result[2]
        person_number = result[3]
        comment = result[4]

        self.top = Frame(self, height=100, bg='blue')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=350, bg='#c2c0ba')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='      Детали контакта', font='arial 20 bold', bg='blue', fg='white')
        self.heading.place(x=160, y=35)
        self.top_image = PhotoImage(file='icons/accounts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=80, y=18)

        # Имя
        self.label_name = Label(self.bottom, text="Имя", font='arial 15', fg='white', bg='#c2c0ba')
        self.label_name.place(x=98, y=43)
        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0,person_name)
        self.entry_name.config(state = 'disabled')
        self.entry_name.place(x=147, y=40)

        # Фамилия
        self.label_surname = Label(self.bottom, text="Фамилия", font='arial 15', fg='white', bg='#c2c0ba')
        self.label_surname.place(x=62, y=83)
        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.config(state='disabled')
        self.entry_surname.place(x=147, y=80)

        # Номер
        self.label_number = Label(self.bottom, text="Номер телефона", font='arial 15', fg='white', bg='#c2c0ba')
        self.label_number.place(x=7, y=123)
        self.entry_number = Entry(self.bottom, width=30, bd=4)
        self.entry_number.insert(0, person_number)
        self.entry_number.config(state='disabled')
        self.entry_number.place(x=147, y=120)

        # Комментарии
        self.label_comment = Label(self.bottom, text="Комментарии", font='arial 15', fg='white', bg='#c2c0ba')
        self.label_comment.place(x=32, y=163)
        self.entry_comment = Entry(self.bottom, width=30, bd=4)
        self.entry_comment.insert(0, comment)
        self.entry_comment.config(state='disabled')
        self.entry_comment.place(x=147, y=160)

        # Кнопки
        saveButton = Button(self.bottom, text="  Редактировать  ", font='arial 20 bold', command=self.update_function)
        saveButton.place(x=190, y=205)
        delButton = Button(self.bottom, text="  Удалить  ", font='arial 20 bold', command= self.delete_person)
        delButton.place(x=222, y=250)
        quitButton = Button(self.bottom, text="  Выход  ", font='arial 20 bold', command=self.destroy)
        quitButton.place(x=230, y=295)

    def update_function(self):
        person_id = self.person_id
        updatepage = Update(person_id)
        self.destroy()

    def delete_person(self):
        person_id = self.person_id
        query = "delete from phonebook where person_id = {}".format(person_id)
        answer = mb.askyesno(title="Удалить", message="Удалить контакт?")
        if answer == True:
            try:
                curs.execute(query)
                conn.commit()
                mb.showinfo("Success", "Контакт удалён")
                self.destroy()

            except Exception as e:
                mb.showerror("Ошибка!", str(e))
