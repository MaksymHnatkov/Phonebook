from tkinter import *
import sqlite3
from tkinter import messagebox as mb
from updAccount import Update
from details import Details

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
        self.bottom = Frame(self, height=110, bg='#c2c0ba')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Контакты', font='arial 20 bold', bg='blue', fg='white')
        self.heading.place(x=180, y=25)
        self.top_image = PhotoImage(file='icons/accounts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=100, y=8)

        self.updButton = Button(self.bottom, text=" Редактировать ", font='arial 18 bold', command = self.update_function)
        self.updButton.place(x=20, y=55)
        self.delButton = Button(self.bottom, text="   Удалить   ", font='arial 18 bold', command = self.delete_person)
        self.delButton.place(x=195, y=55)
        self.quitButton = Button(self.bottom, text="   Выход   ", font='arial 18 bold', command=self.destroy)
        self.quitButton.place(x=340, y=55)
        self.showButton = Button(self.bottom, text="                 Детали                 ", font='arial 18 bold', command = self.show_details)
        self.showButton.place(x=195, y=15)
        self.updButton = Button(self.bottom, text="         Поиск         ", font='arial 18 bold')
        self.updButton.place(x=20, y=15)


        self.scroll = Scrollbar(self.mid, orient=VERTICAL, )
        self.listBox = Listbox(self.mid, width=48, height=16)
        self.listBox.grid(row=0, column=0, padx=(2,0))

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        people = curs.execute('select * from "phonebook"').fetchall()
        count = 0
        for i in people:
            self.listBox.insert(count, str(i[0])+ ". " +str(i[1])+ " " + str(i[2]))
            count += 1

        self.scroll.grid(row=0, column=1, sticky=N + S)

    def exit(self):
        self.destroy()

    def update_function(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]

        updatepage = Update(person_id)

    def show_details(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]

        details_page = Details(person_id)

    def delete_person(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]

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


















