from app.app import Application
import tkinter


def app_start():
    root = tkinter.Tk()
    root.geometry("1200x600+300+150")
    Application(root).pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
    root.mainloop()


if __name__ == '__main__':
    app_start()
