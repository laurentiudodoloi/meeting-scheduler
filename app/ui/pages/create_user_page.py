import tkinter
import tkinter.ttk
import tkinter.messagebox
from app.ui.colors import *

from app.models.users import Users


class CreateUserPage(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, background=PRIMARY_COLOR, padx=20, pady=20)

        self.first_name_field = None
        self.last_name_field = None

        self.setup()

    def setup(self):
        header_text = tkinter.Label(
            master=self,
            text="Create new user",
            background=PRIMARY_COLOR,
            font=("Verdana", 12),
            justify=tkinter.LEFT,
            fg="#fff",
            anchor='w'
        )
        header_text.pack(fill=tkinter.X)

        first_name_row = tkinter.Frame(master=self, bg=PRIMARY_COLOR)
        first_name_row.pack(fill=tkinter.X)

        first_name_label = tkinter.Label(
            master=first_name_row,
            text="First name",
            font=("Verdana", 10),
            fg="#fff",
            bg=PRIMARY_COLOR,
            width=12
        )
        first_name_label.pack(side=tkinter.LEFT, padx=5, pady=5)
        self.first_name_field = tkinter.Entry(master=first_name_row, width=48)

        self.first_name_field.pack(side=tkinter.LEFT, padx=5)

        last_name_row = tkinter.Frame(master=self, bg=PRIMARY_COLOR)
        last_name_row.pack(fill=tkinter.X)

        last_name_label = tkinter.Label(
            master=last_name_row,
            text="Last name",
            fg="#fff",
            font=("Verdana", 10),
            bg=PRIMARY_COLOR,
            width=12
        )
        last_name_label.pack(side=tkinter.LEFT, padx=5, pady=5)

        self.last_name_field = tkinter.Entry(master=last_name_row, width=48)
        self.last_name_field.pack(side=tkinter.LEFT, padx=5)

        submit_button = tkinter.Button(
            self,
            text="Save user",
            width=12,
            fg="#fff",
            background=BUTTON_COLOR,
            command=self.create_user
        )
        submit_button.pack(side=tkinter.RIGHT)

    def validate(self):
        if not self.first_name_field.get():
            tkinter.messagebox.showerror(title="Error occured", message="First name field cannot be empty")
            return False

        if not self.last_name_field.get():
            tkinter.messagebox.showerror(title="Error occured", message="Last name field cannot be empty")
            return False

        return True

    def clear_form(self):
        self.first_name_field.delete(0, 'end')
        self.last_name_field.delete(0, 'end')

    def create_user(self):
        if not self.validate():
            self.clear_form()
            return False

        Users.create(self.first_name_field.get(), self.last_name_field.get())

        tkinter.messagebox._show(title="Operation done", message="The user has been created successfully")
        self.clear_form()

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()
