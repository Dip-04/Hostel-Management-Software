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


class report:

    def __init__(self, root3):

        self.root3 = root3
        self.root3.geometry("1260x638+255+150")
        self.root3.iconbitmap(
            'E:\python\Hostel Management Software\images\icon.ico')
        self.root3.title("HOSTEL MANAGEMENT SOFTWARE")

        self.var_search = StringVar()
        self.var_ent_search = StringVar()

        l = Label(self.root3, bd=10, relief=RIDGE, text="ROOM ALLOCATION", fg='YELLOW', bg='black',
                  font=("times new roman", 18, 'bold', 'underline'))
        l.pack(side=TOP, fill=X)



        labelframe1 = LabelFrame(self.root3, text='View Details and Search System',
                                 font=("times new roman", 12, "bold"),
                                 bd=2, relief=RIDGE, padx=2, bg='light yellow')
        labelframe1.place(x=0, y=50, width=1250, height=580)

        Label(labelframe1, text="Search by:-", font=('arial', 12, 'bold'), bg='red', fg='white').grid(row=0, column=0,
                                                                                                      sticky=W)
        search = ttk.Combobox(labelframe1, font=("times new roman", 12, 'bold'),
                              width=24, state="readonly", textvariable=self.var_search)
        search['value'] = ('Select', 'ROOM_NO', 'MOBILE_NO')
        search.grid(row=0, column=1, padx=2)
        ttk.Entry(labelframe1, width=20, font=(
            'arial', 10, 'bold'), textvariable=self.var_ent_search).grid(row=0, column=2, padx=2)
        Button(labelframe1, text='BACK', font=('arial', 10, 'bold'),
               bg='grey', fg='black', command=lambda: self.back()).grid(row=0, column=5, padx=2)
        Button(labelframe1, text='Search', font=('arial', 10, 'bold'),
               bg='blue', fg='white', command=lambda: self.search()).grid(row=0, column=3, padx=1)
        Button(labelframe1, text='Show all', font=('arial', 10, 'bold'),
               bg='blue', fg='white', command=lambda: self.fetchreport()).grid(row=0, column=4, padx=1)
        xf = Frame(labelframe1, bd=3, relief=RIDGE)
        xf.place(x=0, y=40, width=1230, height=500)
        x = ttk.Scrollbar(xf, orient=HORIZONTAL)
        y = ttk.Scrollbar(xf, orient=VERTICAL)
        self.student_tabel = ttk.Treeview(xf, columns=(
            'FIRST_NAME', 'LAST_NAME', 'MAIL', 'MOBILE_NO', 'ROOM_NO', 'SUBJECT', 'DESCRIPTION', 'REPORT_NO', 'TIME',
            'DATE'), xscrollcommand=x.set, yscrollcommand=y.set)
        x.pack(side=BOTTOM, fill=X)
        y.pack(side=RIGHT, fill=Y)
        x.config(command=self.student_tabel.xview)
        y.config(command=self.student_tabel.yview)
        self.student_tabel.heading('FIRST_NAME', text='FIRST_NAME')
        self.student_tabel.heading('LAST_NAME', text='LAST_NAME')
        self.student_tabel.heading('MAIL', text='MAIL')
        self.student_tabel.heading('MOBILE_NO', text='MOBILE_NO')
        self.student_tabel.heading('ROOM_NO', text='ROOM_NO')
        self.student_tabel.heading('SUBJECT', text='SUBJECT')
        self.student_tabel.heading('DESCRIPTION', text='DESCRIPTION')
        self.student_tabel.heading('REPORT_NO', text='REPORT_NO')
        self.student_tabel.heading('TIME', text='TIME')
        self.student_tabel.heading('DATE', text='DATE')
        self.student_tabel.column('FIRST_NAME', width=100)
        self.student_tabel.column('LAST_NAME', width=100)
        self.student_tabel.column('MAIL', width=100)
        self.student_tabel.column('MOBILE_NO', width=100)
        self.student_tabel.column('ROOM_NO', width=100)
        self.student_tabel.column('SUBJECT', width=100)
        self.student_tabel.column('DESCRIPTION', width=100)
        self.student_tabel.column('REPORT_NO', width=100)
        self.student_tabel.column('TIME', width=100)
        self.student_tabel.column('DATE', width=100)
        self.student_tabel['show'] = 'headings'
        self.student_tabel.pack(fill=BOTH, expand=1)
        self.fetchreport()


    def fetchreport(self):
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select * from report")
        row = my_cusror.fetchall()
        if len(row) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in row:
                self.student_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()








    def search(self):
        conn = mysql.connector.connect(host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute(
            "select * from report where " + str(self.var_search.get()) + "='" + str(self.var_ent_search.get()) + "'")
        row = my_cusror.fetchall()
        if len(row) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in row:
                self.student_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    def back(self):
        self.root3.destroy()



if __name__ == "__main__":
    root3 = Tk()
    obj = report(root3)

    root3.mainloop()