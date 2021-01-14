import tkinter
import tkinter.ttk
from app.ui.colors import *
from app.models.meetings import Meetings


class MeetingsPage(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, background=PRIMARY_COLOR, padx=20, pady=20)

        self.meetings = Meetings.all_sorted()

        self.tree = tkinter.ttk.Treeview(
            master=self,
            height=300,
            columns=("ID", "Name", "Start date", "End date", "Participants")
        )

        self.setup()

    def setup(self):
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='Start date')
        self.tree.heading('#3', text='End date')
        self.tree.heading('#4', text='Participants')

        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.tree.column('#3', stretch=tkinter.YES)
        self.tree.column('#4', stretch=tkinter.YES)

        self.refresh_data()

    def refresh_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for index in range(len(self.meetings)):
            participants = Meetings.participants(self.meetings[index])

            self.tree.insert(parent='', index='end', iid=self.meetings[index].id, text=(index + 1), values=(
                self.meetings[index].name,
                self.meetings[index].start_date.strftime("%A, %d %B, %H:%M"),
                self.meetings[index].end_date.strftime("%A, %d %B, %H:%M"),
                ", ".join([x.first_name for x in participants])
            ))

        self.tree.pack()

    def show(self):
        self.meetings = Meetings.all_sorted()

        self.refresh_data()

        self.pack()

    def hide(self):
        self.pack_forget()
