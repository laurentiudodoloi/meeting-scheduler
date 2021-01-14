import tkinter
import tkinter.ttk
from app.ui.colors import *
from app.models.users import Users


class UsersPage(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, background=PRIMARY_COLOR, padx=20, pady=20)

        self.users = Users.all()

        self.tree = tkinter.ttk.Treeview(
            master=self,
            height=300,
            columns=("ID", "First name", "Last name")
        )

        self.setup()

    def setup(self):
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='First name')
        self.tree.heading('#2', text='Last name')

        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)

        self.refresh_data()

        self.pack(side=tkinter.TOP)

    def refresh_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for index in range(len(self.users)):
            self.tree.insert(parent='', index='end', iid=self.users[index].id, text=(index + 1), values=(
                self.users[index].first_name,
                self.users[index].last_name
            ))

        self.tree.pack()

    def show(self):
        self.users = Users.all()

        self.refresh_data()

        self.pack()

    def hide(self):
        self.pack_forget()
