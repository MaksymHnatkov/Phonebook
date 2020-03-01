from tkinter import *
from accountWin import Accounts


class Application(object):
    def __init__(self, master):
        self.master = master

        self.top = Frame(master, height=150, bg='blue')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='white')
        self.bottom.pack(fill=X)

        # Иконка
        self.top_image = PhotoImage(file='icons/phonebook.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='blue')
        self.top_image_label.place(x=130, y=30)

        # Дизайн
        self.heading = Label(self.top, text='Телефонная книга', font='arial 24 bold', bg='blue', fg='white')
        self.heading.place(x=220, y=50)
        self.prod = Label(self.bottom, text=' Developed by M.Hnatkov ', font='arial 12 bold', bg='white', fg='grey')
        self.prod.place(x=255, y=350)

        # Кнопки
        self.addButton = Button(self.bottom, text=" Создать контакт ", font='arial 26 bold')
        self.addButton.place(x=210, y=70)
        self.searchButton = Button(self.bottom, text=" Найти контакт ", font='arial 26 bold', command = self.my_accounts)
        self.searchButton.place(x=226, y=150)
        self.quitButton = Button(self.bottom, text=" Выход ", font='arial 26 bold')
        self.quitButton.place(x=274, y=230)

    def my_accounts(self):
        accounts = Accounts()


def main():
    root = Tk()
    app = Application(root)
    root.title("Телефонная книга by Hnatkov Maksym")
    root.geometry('650x550+350+200')
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
