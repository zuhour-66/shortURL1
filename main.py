from tkinter import *
import clipboard
import validators
from pyshorteners import Shortener

def Shorten():
    link = e.get()
    valid = validators.url(link)
    if valid:
        short = Shortener().tinyurl.short(link)
        win.configure(bg="blue")
        win.destroy()
        show_shortened_window(short)
    else:
        l.config(text="Invalid Address")

def Copy():
    clipboard.copy(shortened_link.cget("text"))
    c = Label(win2, text="Copied", font=(20))
    c.pack()
    win2.after(2000, c.destroy)

def show_shortened_window(short):
    global win2, l, shortened_link
    win2 = Tk()
    win2.title("Shortened URL")
    win2.geometry("400x100")
    win2.configure(bg="#E9967A")

    l = Label(win2, text="Shortened URL:", font=(20))
    l.pack()

    shortened_link = Label(win2, text=short, font=(20))
    shortened_link.pack(side=LEFT)

    copy_button = Button(win2, text="Copy", command=Copy)
    copy_button.pack(side=LEFT)

    win2.mainloop()

win = Tk()
win.title("URL Shortener")
win.geometry("400x100")
win.configure(bg="pink")

e = Entry(win, font=(20))
e.pack(side=LEFT)

shorten_button = Button(win, text="Shorten", command=Shorten)
shorten_button.pack(side=LEFT)

win.mainloop()

