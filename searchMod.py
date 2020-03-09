from tkinter import *
import sqlite3
import re
from details import Details
from tkinter import messagebox as mb

conn = sqlite3.connect('phonebook.db')
curs = conn.cursor()
conn.create_function('regexp', 2, lambda x, y: 1 if re.search(x, y) else 0)

class Search(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x650+400+150")
        self.title("Поиск")
        self.resizable(False, False)

        self.top = Frame(self, height=100, bg='blue')
        self.top.pack(fill=X)
        self.search_frame = Frame(self, height=150, bg='#c2c0ba')
        self.search_frame.pack(fill=X)
        self.mid = Frame(self, height=250, bg='#c2c0ba')
        self.mid.pack(fill=X)
        self.bottom = Frame(self, height=150, bg='#c2c0ba')
        self.bottom.pack(fill=X)


        self.heading = Label(self.top, text='Поиск контакта', font='arial 20 bold', bg='blue', fg='white')
        self.heading.place(x=210, y=45)
        self.top_image = PhotoImage(file='icons/accounts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=130, y=18)

        self.entry_name = Entry(self.search_frame, width=30, bd=4)
        self.entry_name.place(x=220, y=10)
        self.entry_surname = Entry(self.search_frame, width=30, bd=4)
        self.entry_surname.place(x=220, y=60)
        self.entry_number = Entry(self.search_frame, width=30, bd=4)
        self.entry_number.place(x=220, y=110)


        #Кнопки поиска
        name_button = Button(self.search_frame, text="   Поиск по имени   ", font='arial 20 bold', command=self.search_by_name)
        name_button.place(x=10, y=13)
        surname_button = Button(self.search_frame, text="Поиск по фамилии ", font='arial 20 bold', command=self.search_by_surname)
        surname_button.place(x=10, y=63)
        number_button = Button(self.search_frame, text="  Поиск по номеру  ", font='arial 20 bold', command=self.search_by_number)
        number_button.place(x=10, y=113)

        details_button = Button(self.bottom, text="          Детали          ", font='arial 20 bold', command = self.show_details)
        details_button.place(x=180, y=20)
        clean_button = Button(self.bottom, text="          Очистить          ", font='arial 20 bold', command = self.clean)
        clean_button.place(x=170, y=60)
        quit_button = Button(self.bottom, text="         Выход         ", font='arial 20 bold', command=self.destroy)
        quit_button.place(x=190, y=100)

        self.scroll = Scrollbar(self.mid, orient=VERTICAL)
        self.listBox = Listbox(self.mid, width=58, height=15)
        self.listBox.grid(row=0, column=0, padx=(2, 0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky=N + S)


    def exit(self):
        self.destroy()

    def search_by_name(self):
        name = self.entry_name.get()
        result = curs.execute("select * from phonebook where person_name regexp (?)", (name,))
        count = 0
        for i in result:
            self.listBox.insert(count,str(i[1]) + " " + str(i[2]) + " " + str(i[3]))
            count += 1

    def search_by_surname(self):
        surname = self.entry_surname.get()
        result = curs.execute("select * from phonebook where person_surname regexp (?)", (surname,))
        count = 0
        for i in result:
            self.listBox.insert(count, str(i[1]) + " " + str(i[2]) + " " + str(i[3]))
            count += 1

    def search_by_number(self):
        number = self.entry_number.get()
        match = re.fullmatch(r'\D+', number)
        if match == None:
            result = curs.execute("select * from phonebook where tel_number regexp (?)", (number,))
            count = 0
            for i in result:
                self.listBox.insert(count, str(i[1]) + " " + str(i[2]) + " " + str(i[3]))
                count += 1
        else:
            mb.showerror("Ошибка!", "Проверьте правильность написания номера!", icon='warning')

    def show_details(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]

        details_page = Details(person_id)
        self.destroy()

    def clean(self):
        self.listBox.delete(0,END)
        self.entry_name.delete(0,END)
        self.entry_surname.delete(0, END)
        self.entry_number.delete(0, END)