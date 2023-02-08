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


class Messstudent:

    def __init__(self,root6):

        self.root6 = root6
        self.root6.geometry("1260x638+255+150")
        self.root6.iconbitmap('E:\python\Hostel Management Software\images\icon.ico')
        self.root6.title("HOSTEL MANAGEMENT SOFTWARE")
        self.mess=StringVar()

        l = Label(self.root6, bd=10, relief=RIDGE, text="MESS SCHEDULE OF THIS MONTH", fg='YELLOW', bg='black',font=("times new roman", 18, 'bold', 'underline'))
        l.pack(side=TOP, fill=X)

        labelframe1 = LabelFrame(self.root6,bd=5, relief=RIDGE, padx=2, bg='light yellow')
        labelframe1.place(x=0, y=40, width=1260, height=500)
        xf = Frame(labelframe1, bd=3, relief=RIDGE)
        xf.place(x=0, y=0, width=1250, height=480)
        x = ttk.Scrollbar(xf, orient=HORIZONTAL)
        y = ttk.Scrollbar(xf, orient=VERTICAL)

        self.student_tabel = ttk.Treeview(xf, columns=(
            'Mess'), xscrollcommand=x.set, yscrollcommand=y.set)
        x.pack(side=BOTTOM, fill=X)
        y.pack(side=RIGHT, fill=Y)
        x.config(command=self.student_tabel.xview)
        y.config(command=self.student_tabel.yview)
        self.student_tabel.heading('Mess', text='Mess')


        self.student_tabel.column('Mess', width=100)


        self.student_tabel['show'] = 'headings'
        self.student_tabel.pack(fill=BOTH, expand=1)
        self.fetchdata()




    def fetchdata(self):
        file=open("mess.txt",'r')
        hii=file.read()

        img = Image.open(hii)
        img = img.resize((1100, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        p = Label(self.student_tabel, image=self.photo)
        p.place(x=15, y=5, width=1100, height=500)





if __name__ == "__main__":
    root6 = Tk()
    obj = Messstudent(root6)
    root6.mainloop()