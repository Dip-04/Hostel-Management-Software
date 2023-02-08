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


class Addroom:

    def __init__(self, root4):
        self.root4 = root4
        self.root4.geometry("1260x638+255+150")
        self.root4.iconbitmap(
            'E:\python\Hostel Management Software\images\icon.ico')
        self.root4.title("HOSTEL MANAGEMENT SOFTWARE")
        self.var_hostelno = StringVar()
        self.var_roomtype = StringVar()
        self.var_floor = StringVar()
        self.var_roomno = StringVar()
        self.search = StringVar()
        self.var_ent_search=StringVar()
        self.var_hno=StringVar()
        self.var_hno.set(self.var_hostelno.get()+self.var_roomno.get())




        l = Label(self.root4, bd=10, relief=RIDGE, text="ROOM ADDING DEPARTMENT", fg='YELLOW', bg='black',
                  font=("times new roman", 18, 'bold', 'underline'))
        l.pack(side=TOP, fill=X)
        labelframe = LabelFrame(self.root4, text='Add Room ', font=("times new roman", 12, "bold"), bd=2,
                                relief=RIDGE,
                                padx=2, bg='sky blue')
        labelframe.place(x=0, y=40, width=455, height=355)
        Label(labelframe, text="Hostel No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(
            row=0,
            column=0,
            sticky=W)
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly",textvariable=self.var_hostelno)
        ca['value'] = ('Select', 'A', 'B', 'C', 'D', 'E', 'F')
        ca.current(0)
        ca.grid(row=0, column=1)

        Label(labelframe, text="Room Type: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=1,
                                                                                                                  column=0,
                                                                                                                  sticky=W)
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly",textvariable=self.var_roomtype)
        ca['value'] = ('Select', 'Double Bed', 'Triple Bed')
        ca.current(0)
        ca.grid(row=1, column=1)
        Label(labelframe, text="Floor: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=2,
                                                                                                              column=0,
                                                                                                              sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_floor)
        nen.grid(row=2, column=1)
        Label(labelframe, text="Room No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=3,
                                                                                                          column=0,
                                                                                                          sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_roomno)
        nen.grid(row=3, column=1)
        Label(labelframe, text="H_NO: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=4,
                                                                                                          column=0,
                                                                                                          sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25, textvariable=self.var_hno,state='readonly')
        nen.grid(row=4, column=1)
        Button(labelframe, text='genrate', font=('arial', 10, 'bold'), bg='black', fg='gold', width=11,command=lambda :self.gen()).grid(row=4, column=2)

        btf = Frame(labelframe, bd=3, relief=RIDGE)
        btf.place(x=0, y=290, width=400, height=35)
        Button(btf, text='Add', font=('arial', 10, 'bold'), bg='black', fg='gold', width=11,command=lambda :self.Add_data()).grid(row=0, column=0)
        Button(btf, text='Update', font=('arial', 10, 'bold'), bg='black', fg='gold', width=11,command=lambda :self.Update()).grid(row=0, column=1)
        Button(btf, text='Delete', font=('arial', 10, 'bold'), bg='black', fg='gold', width=11,command=lambda :self.delete()).grid(row=0, column=2)
        Button(btf, text='Clear', font=('arial', 10, 'bold'), bg='black', fg='gold', width=11,command=lambda :self.reset()).grid(row=0, column=3)






        labelframe1 = LabelFrame(self.root4, text='View Details and Search System',
                                 font=("times new roman", 12, "bold"),
                                 bd=2, relief=RIDGE, padx=2, bg='light yellow')
        labelframe1.place(x=455, y=40, width=600, height=355)

        Label(labelframe1, text="Search by:-", font=('arial', 12, 'bold'), bg='red', fg='white').grid(row=0, column=0,
                                                                                                      sticky=W)
        search = ttk.Combobox(labelframe1, font=("times new roman", 12, 'bold'),
                              width=24, state="readonly",textvariable=self.search)
        search['value'] = ('Select', 'ROOM_NO', 'H_NO')
        search.grid(row=0, column=1, padx=2)
        ttk.Entry(labelframe1, width=20, font=(
            'arial', 10, 'bold'),textvariable=self.var_ent_search).grid(row=0, column=2, padx=2)
        Button(labelframe1, text='BACK', font=('arial', 10, 'bold'),
               bg='grey', fg='black',command=lambda :self.back()).grid(row=0, column=5, padx=2)
        Button(labelframe1, text='Search', font=('arial', 10, 'bold'),
               bg='blue', fg='white',command=lambda :self.search1()).grid(row=0, column=3, padx=1)
        Button(labelframe1, text='Show all', font=('arial', 10, 'bold'),
               bg='blue', fg='white',command=lambda :self.fetchdata()).grid(row=0, column=4, padx=1)
        xf = Frame(labelframe1, bd=3, relief=RIDGE)
        xf.place(x=0, y=40, width=580, height=280)
        x = ttk.Scrollbar(xf, orient=HORIZONTAL)
        y = ttk.Scrollbar(xf, orient=VERTICAL)
        self.student_tabel = ttk.Treeview(xf, columns=(
            'HOSTEL_NO', 'ROOM_TYPE', 'FLOOR', 'ROOM_NO','H_NO'), xscrollcommand=x.set, yscrollcommand=y.set)
        x.pack(side=BOTTOM, fill=X)
        y.pack(side=RIGHT, fill=Y)
        x.config(command=self.student_tabel.xview)
        y.config(command=self.student_tabel.yview)
        self.student_tabel.heading('HOSTEL_NO', text='HOSTEL_NO')
        self.student_tabel.heading('ROOM_TYPE', text='ROOM_TYPE')
        self.student_tabel.heading('FLOOR', text='FLOOR')
        self.student_tabel.heading('ROOM_NO', text='ROOM_NO')
        self.student_tabel.heading('H_NO', text='H_NO')


        self.student_tabel.column('HOSTEL_NO', width=100)
        self.student_tabel.column('ROOM_TYPE', width=100)
        self.student_tabel.column('FLOOR', width=100)
        self.student_tabel.column('ROOM_NO', width=100)
        self.student_tabel.column('H_NO', width=100)


        self.student_tabel['show'] = 'headings'
        self.student_tabel.pack(fill=BOTH, expand=1)
        self.student_tabel.bind("<ButtonRelease-1>",self.get_curser)

        self.fetchdata()

        img1 = Image.open(r"E:\python\Hostel Management Software\images\HOSTEL1.jpg")
        img1 = img1.resize((290, 240), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)
        p1 = Label(self.root4, image=self.photo1, bd=4, relief=RIDGE)
        p1.place(x=0, y=395, width=310, height=240)

        img2 = Image.open(r"E:\python\Hostel Management Software\images\HOSTEL2.jpg")
        img2 = img2.resize((290, 240), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)
        p2 = Label(self.root4, image=self.photo2, bd=4, relief=RIDGE)
        p2.place(x=310, y=395, width=290, height=240)

        img3 = Image.open(r"E:\python\Hostel Management Software\images\HOSTEL3.jpg")
        img3 = img3.resize((290, 240), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)
        p3 = Label(self.root4, image=self.photo3, bd=4, relief=RIDGE)
        p3.place(x=600, y=395, width=290, height=240)

        img4 = Image.open(r"E:\python\Hostel Management Software\images\HOSTEL4.jpg")
        img4 = img4.resize((370, 240), Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(img4)
        p4 = Label(self.root4, image=self.photo4, bd=4, relief=RIDGE)
        p4.place(x=890, y=395, width=370, height=240)

        img5 = Image.open(r"E:\python\Hostel Management Software\images\HOSTEL5.webp")
        img5 = img5.resize((250, 395), Image.ANTIALIAS)
        self.photo5 = ImageTk.PhotoImage(img5)
        p5 = Label(self.root4, image=self.photo5, bd=4, relief=RIDGE)
        p5.place(x=1054, y=40, width=250, height=355)

        def time():
            string = strftime("%H:%M:%S %p \n %d/%m/%Y")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(labelframe, font="times 12 bold")
        lbl.grid(row=0, column=2)
        time()

    def Add_data(self):
        if self.var_hostelno.get() == "" and self.var_roomtype.get()=="" and self.var_floor.get()=="" and self.var_roomno.get()=="" and self.var_hno.get()=="":

            messagebox.showerror(
                "ERROR !!!!", "ALL FIELDS ARE REQUIRED",
                parent=self.root4)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username='root', password='Test@123', database='hostel')
                my_cusror = conn.cursor()
                query = "insert into adds (HOSTEL_NO,ROOM_TYPE,FLOOR,ROOM_NO,H_NO) values(%s,%s,%s,%s,%s)"
                arg = (self.var_hostelno.get(), self.var_roomtype.get(), self.var_floor.get(), self.var_roomno.get(),self.var_hno.get())
                my_cusror.execute(query, arg)
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo('Room ',
                                    f'ADDED SUCCUSEFULLY \n______________________________________________________________\n',
                                    parent=self.root4)
            except Exception as es:
                messagebox.showerror("ERROR", f"DUE TO:{str(es)}")

    def fetchdata(self):
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select * from adds")
        row = my_cusror.fetchall()
        if len(row) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in row:
                self.student_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_curser(self,event=" "):
        crow=self.student_tabel.focus()
        con=self.student_tabel.item(crow)
        row=con["values"]
        self.var_hostelno.set(row[0]),
        self.var_roomtype.set(row[1]),
        self.var_floor.set(row[2]),
        self.var_roomno.set(row[3]),
        self.var_hno.set(row[4])




    def Update(self):
        if self.var_roomno.get() == "":

            messagebox.showerror(
                "ERROR !!!!", "ALL FIELDS ARE REQUIRED ",
                parent=self.root4)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username='root', password='Test@123', database='hostel')
                my_cusror = conn.cursor()


                my_cusror.execute("update adds set ROOM_TYPE=%s,FLOOR=%s,ROOM_NO=%s where H_NO=%s",( self.var_roomtype.get(), self.var_floor.get(), self.var_roomno.get(),self.var_hno.get()))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo('ROOM ',
                                    f'UPDATE SUCCUSEFULLY \n______________________________________________________________\n',
                                    parent=self.root4)
            except Exception as es:
                messagebox.showerror("ERROR", f"DUE TO:{str(es)}")

    def delete(self):
        mdelete=messagebox.askyesno("Hostel management software","DO YOU WANT TO DELETE THIS ROOM",parent=self.root4)
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        if  mdelete >0:
            my_cusror = conn.cursor()
            my_cusror.execute("delete from adds where H_NO=%s",(self.var_hno.get(),))
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetchdata()
        conn.close()

    def reset(self):
        self.var_hostelno.set(""),
        self.var_roomtype.set(""),
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_hno.set("")




    def search1(self):
        conn = mysql.connector.connect( host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select * from adds where "+str(self.search.get())+"='"+str(self.var_ent_search.get())+"'")
        row = my_cusror.fetchall()
        if len(row) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in row:
                self.student_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    def back(self):
        self.root4.destroy()

    def gen(self):
        self.var_hno.set(str(self.var_hostelno.get()+self.var_roomno.get()))







if __name__ == "__main__":
    root4 = Tk()
    obj = Addroom(root4)

    root4.mainloop()