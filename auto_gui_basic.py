import datetime
import os
import time
import tkinter as tk
from tkinter.ttk import *
import threading
import shutil

# functions

def start_function():

    def ok():
        window_1.destroy()
        selection = userinput_1.get()
        if selection == "1":
            file_path = userinput_2.get()
            delete_time = userinput_3.get()
            print("Performing the operation....")
            while True:
                date_and_time = datetime.datetime.now()
                time = date_and_time.strftime("%H:%M:%S")
                if time == delete_time:
                    try:
                        os.unlink(file_path)
                        print("Operation Successful!")
                        window_2 = tk.Tk()
                        window_2.geometry("300x100")
                        window_2.resizable(False, False)
                        Label_4 = Label(window_2, text="Operation Successful.", font="bold").place(x=60, y=10)
                        Button_2 = Button(window_2, text="Ok", command=window_2.destroy).place(x=100, y=50)
                        window_2.mainloop()
                    except FileNotFoundError:
                        print("The file path that has been entered is invalid. Please enter a valid file path and try "
                                  "again.")
                    except PermissionError:
                        print("You don't have sufficient rights to perform this operation.")
                    finally:
                        break
                else:
                    continue

        elif selection == "2":
            folder_path = userinput_2.get()
            delete_time = userinput_3.get()
            print("Performing the operation....")
            while True:
                date_and_time = datetime.datetime.now()
                time = date_and_time.strftime("%H:%M:%S")
                if time == delete_time:
                    try:
                        shutil.rmtree(folder_path)
                        print("Operation Successful.")
                        window_2 = tk.Tk()
                        window_2.geometry("300x100")
                        window_2.resizable(False, False)
                        Label_4 = Label(window_2,text="Operation Successful.", font="bold").place(x=60, y=10)
                        Button_2 = Button(window_2,text="Ok", command=window_2.destroy).place(x=100, y=50)
                        window_2.mainloop()
                    except FileNotFoundError:
                        print("The folder doesn't exist in the path provided. Please check the path once again")
                    except PermissionError:
                        print("You don't have sufficient rights to perform this action.")
                    finally:
                        break
        else:
            print("you have to enter either 1 or 2 only.")

    window_1 = tk.Tk()
    window_1.geometry("300x100")
    window_1.resizable(False, False)
    Label_1 = Label(window_1, text="During the action, app will become unresponsive.")
    Label_2 = Label(window_1, text="But the process will be carried out in background.")
    Label_3 = Label(window_1, text="Press ok to continue.")
    Button_1 = Button(window_1, text="Ok", command=ok)
    Label_1.place(x=0, y=10)
    Label_2.place(x=0, y=30)
    Label_3.place(x=0, y=50)
    Button_1.place(x=110, y=70)
    window_1.mainloop()


    ending()


# Gui design

window = tk.Tk()
window.title("Auto Delete")
window.geometry("600x600")
window.resizable(False, False)
title_1 = tk.Label(text="Welcome to auto delete program",
                   font="bold")
                #background="black",
                #foreground="white"

title_2 = tk.Label(text="Select which operation you would like to perform: ")
                   #background="black",
                   #foreground="white"

title_3 = tk.Label(text="1.Delete a file")
                   #background="black",
                   #foreground="white"

title_4 = tk.Label(text="2.Delete a folder")
                   #background="black",
                   #foreground="white"

title_5 = tk.Label(text="Enter your choice: ")
                   #background="black",
                   #foreground="white"

title_6 = tk.Label(text="Enter the path to file/folder to be deleted: ")

title_7 = tk.Label(text="Enter the time to delete the file/folder: ")
title_8 = tk.Label(text="Note: Time to be entered in 24 hour format only. ex- 22:59:00",
                   fg="purple",
                   font="bold",
                   height=0)


btn_1 = Button(text="Start!", command=start_function)
                  #bg="black",
                  #fg="white"

btn_2 = Button(text="Exit", command=window.destroy)
                  #bg="black",
                  #fg="white")

btn_1.config(width=98)
btn_2.config(width=98)

userinput_1 = Entry(width=2)
userinput_2 = Entry(width=50)
userinput_3 = Entry(width=25)
title_1.place(x=200, y=10)
title_2.place(x=2, y=30)
title_3.place(x=2, y=50)
title_4.place(x=2, y=70)
title_5.place(x=2, y=90)
title_6.place(x=2, y=115)
title_7.place(x=2, y=140)
title_8.place(x=2, y=160)
btn_1.place(x=0, y=208)
btn_2.place(x=0, y=236)
userinput_1.place(x=105, y=90)
userinput_2.place(x=225, y=115)
userinput_3.place(x=210, y=140)
window.mainloop()
