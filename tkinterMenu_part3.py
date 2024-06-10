import tkinter
from tkinter import Tk, Menu, messagebox
def changepassword():
    print("Change password pressed")
    # you may import another file here
    # or write code to change password.

def welcome():
    messagebox.showinfo("welcome ...", "Welcome to demo on using menu. "
                                       "Use this demo to build your own . Do not copy ....  ")
def createnew():
    print("create a new account ... ")
def createMenu():

    win = Tk()
    win.geometry('450x280')
    win.title('Demo - Using menu')

    # create a menubar
    menubar = Menu(win)
    win.config(menu=menubar)

    # create the file_menu
    file_menu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Accounts", menu=file_menu, underline=0)
    # add menu items to the File menu
    file_menu.add_command(label='New', command=lambda : createnew())
    file_menu.add_command(label='Open...')
    file_menu.add_command(label='Remove')
    file_menu.add_command(label="change password", command=lambda:changepassword())
    file_menu.add_command(label='Exit', command=win.destroy)
    file_menu.add_separator()

    # create the Help menu
    play_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Play", menu=play_menu, underline=0)
# you may add more options for Play menu here
    help_menu = Menu(menubar, tearoff=0)

 # add a submenu
    sub_menu = Menu(file_menu, tearoff=0)
    sub_menu.add_command(label='Font')
    sub_menu.add_command(label='Colours')

    # add the File menu to the menubar
    file_menu.add_cascade(label="Preferences", menu=sub_menu)

    menubar.add_cascade(label="settings")
    file_menu.add_separator()

    # add Exit menu item

    help_menu.add_command(label='Welcome', command=lambda : welcome())
    help_menu.add_command(label='About...')
    # add the Help menu to the menubar


    menubar.add_cascade(label="Help", menu=help_menu, underline=0)
    win.mainloop()


if __name__=="__main__":
    createMenu()