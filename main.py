from tkinter import *
from accountWin import Accounts
from addaccount import AddAccounts
from searchMod import Search

class Application(object):
    def __init__(self, master):
        self.master = master

        self.top = Frame(master, height=150, bg='blue')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#abedbc')
        self.bottom.pack(fill=X)

        # Иконка
        self.top_image = PhotoImage(file='icons/phonebook.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=130, y=30)

        # Дизайн
        self.heading = Label(self.top, text='Телефонная книга', font='arial 24 bold', bg='blue', fg='white')
        self.heading.place(x=220, y=50)
        self.prod = Label(self.bottom, text=' Developed by M.Hnatkov ', font='arial 12 bold', bg='#abedbc', fg='grey')
        self.prod.place(x=255, y=350)

        # Кнопки
        self.addButton = Button(self.bottom, text="     Создать контакт     ", font='arial 26 bold', command=self.add_account)
        self.addButton.place(x=180, y=70)
        self.searchButton = Button(self.bottom, text="     Просмотреть контакты     ", font='arial 26 bold', command = self.my_accounts)
        self.searchButton.place(x=135, y=140)
        self.findButton = Button(self.bottom, text="    Найти контакт    ", font='arial 26 bold', command=self.search)
        self.findButton.place(x=200, y=210)
        self.quitButton = Button(self.bottom, text=" Выход ", font='arial 26 bold', command=self.master.destroy)
        self.quitButton.place(x=272, y=280)

    def exit(self):
        self.master.destroy()
    def my_accounts(self):
        accounts = Accounts()
    def add_account(self):
        add_contact = AddAccounts()
    def search(self):
        search_page = Search()


def main():
    root = Tk()
    app = Application(root)
    root.title("Телефонная книга by Hnatkov Maksym")
    root.geometry('650x550+350+200')
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
