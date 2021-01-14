import settings
import os

import tkinter
import tkinter.ttk
from app.ui.colors import *

from app.ui.pages.users_page import UsersPage
from app.ui.pages.meetings_page import MeetingsPage
from app.ui.pages.create_meeting_page import CreateMeetingPage
from app.ui.pages.create_user_page import CreateUserPage


class Application(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__()

        self.master.title(os.getenv("APP_NAME"))

        self.parent = parent

        self.root_frame = tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.navigation = tkinter.Frame(
            parent=self.root_frame,
            height=40,
            background=SECONDARY_COLOR,
            padx=20,
            pady=10
        )
        self.content_frame = tkinter.Frame(parent=self.root_frame, background=PRIMARY_COLOR, padx=20, pady=20)

        self.setup_navigation()

        self.navigation.pack(fill=tkinter.X, side=tkinter.TOP, expand=False)
        self.content_frame.pack(fill=tkinter.BOTH, expand=True, side=tkinter.LEFT)

        self.users_page = UsersPage(self.content_frame)
        self.meetings_page = MeetingsPage(self.content_frame)
        self.create_meeting_page = CreateMeetingPage(self.content_frame)
        self.create_user_page = CreateUserPage(self.content_frame)

        self.pages = [
            self.users_page,
            self.meetings_page,
            self.create_meeting_page,
            self.create_user_page
        ]

        self.switch_page(self.meetings_page)

    def setup_navigation(self):
        new_meeting_button = tkinter.Button(
            master=self.navigation,
            text="New meeting",
            width=12,
            background=BUTTON_COLOR,
            fg="#fff",
            command=lambda: self.switch_page(self.create_meeting_page)
        )
        new_user_button = tkinter.Button(
            master=self.navigation,
            text="New user",
            width=12,
            background=BUTTON_COLOR,
            fg="#fff",
            command=lambda: self.switch_page(self.create_user_page)
        )
        meetings_button = tkinter.Button(
            master=self.navigation,
            text="Meetings",
            width=12,
            background=BUTTON_COLOR,
            fg="#fff",
            command=lambda: self.switch_page(self.meetings_page)
        )
        users_button = tkinter.Button(
            master=self.navigation,
            text="Users",
            width=12,
            background=BUTTON_COLOR,
            fg="#fff",
            command=lambda: self.switch_page(self.users_page)
        )

        meetings_button.pack(side=tkinter.RIGHT)
        users_button.pack(side=tkinter.RIGHT)
        new_meeting_button.pack(side=tkinter.RIGHT)
        new_user_button.pack(side=tkinter.RIGHT)

    def hide_pages(self):
        for page in self.pages:
            page.pack_forget()

    def switch_page(self, current_page):
        self.hide_pages()

        current_page.show()
