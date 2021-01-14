import tkinter
import tkinter.ttk
from app.ui.colors import *
import tkcalendar
import datetime
import time
import tkinter.messagebox

from app.models.users import Users
from app.models.meetings import Meetings


class CreateMeetingPage(tkinter.Frame):
    def __init__(self, parent, **kw):
        super().__init__(master=parent, background=PRIMARY_COLOR, padx=20, pady=20)

        self.users = Users.all()

        self.name_field = None
        self.start_date_field = None
        self.end_date_field = None

        self.users_list = None

        self.setup()

    def setup(self):
        header_text = tkinter.Label(
            master=self,
            text="Create new meeting",
            background=PRIMARY_COLOR,
            font=("Verdana", 12),
            fg="#fff",
            justify=tkinter.LEFT,
            anchor='w'
        )
        header_text.pack(fill=tkinter.X)

        name_row = tkinter.Frame(master=self, bg=PRIMARY_COLOR)
        name_row.pack(fill=tkinter.X)
        name_label = tkinter.Label(
            master=name_row,
            text="Name",
            fg="#fff",
            font=("Verdana", 10),
            bg=PRIMARY_COLOR,
            width=12
        )
        name_label.pack(side=tkinter.LEFT, padx=5, pady=5)

        self.name_field = tkinter.Entry(master=name_row, width=48)
        self.name_field.pack(side=tkinter.LEFT, padx=5)

        start_date_row = tkinter.Frame(master=self, bg=PRIMARY_COLOR)
        start_date_row.pack(fill=tkinter.X)
        start_date_label = tkinter.Label(
            master=start_date_row,
            text="Start date",
            fg="#fff",
            font=("Verdana", 10),
            bg=PRIMARY_COLOR,
            width=12
        )
        start_date_label.pack(side=tkinter.LEFT, padx=5, pady=5)

        self.start_date_field = tkcalendar.DateEntry(master=start_date_row, width=48, date_pattern="y-m-d")
        self.start_date_field.pack(side=tkinter.LEFT, padx=5)

        end_date_row = tkinter.Frame(master=self, bg=PRIMARY_COLOR)
        end_date_row.pack(fill=tkinter.X)
        end_date_label = tkinter.Label(
            master=end_date_row,
            text="End date",
            fg="#fff",
            font=("Verdana", 10),
            bg=PRIMARY_COLOR,
            width=12
        )
        end_date_label.pack(side=tkinter.LEFT, padx=5, pady=5)

        self.end_date_field = tkcalendar.DateEntry(master=end_date_row, width=48, date_pattern="y-m-d")
        self.end_date_field.pack(side=tkinter.LEFT, padx=5)

        select_users_row = tkinter.Frame(master=self, bg=PRIMARY_COLOR, pady=10)
        select_users_row.pack(fill=tkinter.X)

        self.users_list = tkinter.Listbox(
            master=select_users_row,
            bg=LIST_COLOR,
            fg=ACTION_COLOR,
            selectmode=tkinter.MULTIPLE,
            font=("Verdana", 10)
        )
        for user in self.users:
            self.users_list.insert(1, user.first_name + " " + user.last_name)

        self.users_list.pack()

        submit_button = tkinter.Button(
            self,
            text="Save meeting",
            width=12,
            fg="#fff",
            background=BUTTON_COLOR,
            command=self.create_meeting
        )
        submit_button.pack(side=tkinter.RIGHT)

    def validate(self):
        current_date = datetime.datetime.now().__format__("%Y-%m-%d")
        start_date = datetime.datetime.strptime(self.start_date_field.get(), "%Y-%m-%d")
        end_date = datetime.datetime.strptime(self.end_date_field.get(), "%Y-%m-%d")
        print(start_date > end_date)

        if not self.name_field.get():
            tkinter.messagebox.showerror(title="Error occured", message="Name field cannot be empty")
            return False

        if start_date < datetime.datetime.strptime(current_date, "%Y-%m-%d"):
            tkinter.messagebox.showerror(title="Error occured", message="You cannot add meeting in the past")
            return False

        if start_date > end_date:
            tkinter.messagebox.showerror(title="Error occured", message="Start date is greater than end date")
            return False

        exists = Meetings.find_by_name(self.name_field.get())
        if exists:
            tkinter.messagebox.showerror(title="Error occured", message="A meeting with this name already exists")
            return False

        return True

    def clear_form(self):
        self.name_field.delete(0, 'end')

    def create_meeting(self):
        if not self.validate():
            self.clear_form()
            return False

        start_date = time.mktime(datetime.datetime.strptime(self.start_date_field.get(), "%Y-%m-%d").timetuple())
        end_date = time.mktime(datetime.datetime.strptime(self.end_date_field.get(), "%Y-%m-%d").timetuple())

        meeting = Meetings.create(self.name_field.get(), start_date, end_date)

        for i in self.users_list.curselection():
            user = self.users[i]
            Meetings.assign_user(meeting, user)

        tkinter.messagebox._show(title="Operation done", message="The meeting has been created successfully")
        self.clear_form()

    def refresh_data(self):
        self.users_list.delete(0, 'end')
        for user in self.users:
            self.users_list.insert(1, user.first_name + " " + user.last_name)

    def show(self):
        self.users = Users.all()

        self.refresh_data()

        self.pack()

    def hide(self):
        self.pack_forget()
