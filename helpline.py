from datetime import datetime
from tkinter import *
import random
import tk as tk
from PIL import ImageTk, Image
from time import strftime
from tkinter import filedialog
import pickle
import mysql.connector
from tkinter import ttk, messagebox


class Help:

    def __init__(self,root6):

        self.root6 = root6
        self.root6.geometry("1260x638+255+150")
        self.root6.iconbitmap('E:\python\Hostel Management Software\images\icon.ico')
        self.root6.title("HOSTEL MANAGEMENT SOFTWARE")
        self.mess=StringVar()



        img = Image.open(r"E:\python\Hostel Management Software\images\help.jpg")
        img = img.resize((1240, 640), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        p = Label(self.root6, image=self.photo, bd=4, relief=RIDGE)
        p.place(x=0, y=0, width=1240, height=640)
        l = Label(p, bd=10, relief=RIDGE, text="HELPLINE NOs", fg='YELLOW', bg='black',
                  font=("times new roman", 18, 'bold', 'underline'))
        l.pack(side=TOP, fill=X)








if __name__ == "__main__":
    root6 = Tk()
    obj = Help(root6)
    root6.mainloop()