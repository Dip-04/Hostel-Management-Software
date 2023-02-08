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
class Roomallocation:

    def __init__(self, root3):

        self.root3 = root3
        self.root3.geometry("1260x638+255+150")
        self.root3.iconbitmap(
            'E:\python\Hostel Management Software\images\icon.ico')
        self.root3.title("HOSTEL MANAGEMENT SOFTWARE")
        self.var_contact=StringVar()
        self.var_checkout=StringVar()
        self.var_hostelno=StringVar()
        self.var_roomty=StringVar()
        self.var_available=StringVar()
        self.var_messno=StringVar()
        self.var_month=StringVar()
        self.var_cost=StringVar()
        self.var_time=StringVar()
        self.var_search = StringVar()
        self.var_ent_search = StringVar()
        self.date = StringVar()
        
        l = Label(self.root3, bd=10, relief=RIDGE, text="ROOM ALLOCATION", fg='YELLOW', bg='black',
                  font=("times new roman", 18, 'bold', 'underline'))
        l.pack(side=TOP, fill=X)
        self.date.set(strftime("%d/%m/%Y"))
        labelframe = LabelFrame(self.root3, text='Room Booking', font=("times new roman", 12, "bold"), bd=2,
                                relief=RIDGE,
                                padx=2, bg='sky blue')
        labelframe.place(x=0, y=40, width=455, height=355)

        Label(labelframe, text="Student Phone No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=0,
                                                                                                               column=0,
                                                                                                               sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_contact)
        nen.grid(row=0, column=1)
        Label(labelframe, text="Check in Date: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=1,
                                                                                                              column=0,
                                                                                                              sticky=W)
        Label(labelframe, text="Check out Date: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=2,
                                                                                                                  column=0,
                                                                                                                  sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_checkout)
        nen.grid(row=2, column=1)
        Button(labelframe,text='Fetch Data', font=('arial', 10, 'bold'),bg='black',fg='gold',command=lambda :self.fetchcontact()).grid(row=0,column=2)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.date,state='readonly')
        nen.grid(row=1, column=1)
        Label(labelframe, text="Hostel No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                sticky=W)
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),textvariable=self.var_hostelno,
                          width=8, state="readonly")
        ca['value'] = ('Select','A','B','C','D','E','F')
        ca.current(0)
        ca.grid(row=3,column=1)
        Label(labelframe, text="Room Type: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=4,
                                                                                                                column=0,
                                                                                                                sticky=W)
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select ROOM_TYPE from adds")
        row1 = my_cusror.fetchall()
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),textvariable=self.var_roomty,
                          width=8, state="readonly")
        ca['value'] =row1
        ca.current(0)
        ca.grid(row=4, column=1)
        Label(labelframe, text="Available Room: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=5,
                                                                                                              column=0,
                                                                                                              sticky=W)
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select H_NO from adds")
        row = my_cusror.fetchall()
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly", textvariable=self.var_available)
        ca['value'] =row
        ca.current(0)
        ca.grid(row=5, column=1)

        Label(labelframe, text="Mess No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=6,
                                                                                                             column=0,
                                                                                                             sticky=W)
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly",textvariable=self.var_messno)
        ca['value'] = ('Select', '1', '2', '3')
        ca.current(0)
        ca.grid(row=6,column=1)

        Label(labelframe, text="No. of Days: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=7,
                                                                                                         column=0,
                                                                                                         sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_month,state='readonly')
        nen.grid(row=7, column=1)
        Label(labelframe, text="Total Cost: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=8,
                                                                                                          column=0,
                                                                                                          sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,state='readonly',textvariable=self.var_cost)
        nen.grid(row=8, column=1)

        # TIME
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly",textvariable=self.var_time)
        ca['value'] = (strftime('%H:%M'))
        ca.current(0)
        ca.place(x=3900, y=1000)
        ca1 = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                           width=8, state="readonly")
        ca1['value'] = (strftime('%d/%m/%Y'))
        ca1.current(0)
        ca1.place(x=3900, y=1000)
        Button(labelframe, text='Bill', font=('arial', 10, 'bold'),command=lambda :self.total(), bg='black', fg='gold', width=11
               ).grid(row=8, column=2)
        btf = Frame(labelframe, bd=3, relief=RIDGE)
        btf.place(x=0, y=290, width=400, height=35)
        Button(btf, text='Save', font=('arial', 10, 'bold'), bg='black', fg='gold',command=lambda :self.Add_data(), width=11
               ).grid(row=0, column=0)
        Button(btf, text='Update', font=('arial', 10, 'bold'),
               bg='black', fg='gold', width=11,command=lambda :self.Update()).grid(row=0, column=1)
        Button(btf, text='Delete', font=('arial', 10, 'bold'),
               bg='black', fg='gold', width=11,command=lambda :self.delete()).grid(row=0, column=2)
        Button(btf, text='Reset', font=('arial', 10, 'bold'),
               bg='black', fg='gold', width=11,command=lambda :self.reset()).grid(row=0, column=3)

        labelframe1 = LabelFrame(self.root3, text='View Details and Search System',
                                 font=("times new roman", 12, "bold"),
                                 bd=2, relief=RIDGE, padx=2, bg='light yellow')
        labelframe1.place(x=0, y=390, width=1250, height=240)

        Label(labelframe1, text="Search by:-", font=('arial', 12, 'bold'), bg='red', fg='white').grid(row=0, column=0,
                                                                                                      sticky=W)
        search = ttk.Combobox(labelframe1, font=("times new roman", 12, 'bold'),
                              width=24, state="readonly",textvariable=self.var_search)
        search['value'] = ('Select', 'AVAILABLE_ROOM', 'MOBILE_NO')
        search.grid(row=0, column=1, padx=2)
        ttk.Entry(labelframe1, width=20, font=(
            'arial', 10, 'bold'),textvariable=self.var_ent_search).grid(row=0, column=2, padx=2)
        Button(labelframe1, text='BACK', font=('arial', 10, 'bold'),
               bg='grey', fg='black',command=lambda :self.back()).grid(row=0, column=5, padx=2)
        Button(labelframe1, text='Search', font=('arial', 10, 'bold'),
               bg='blue', fg='white',command=lambda :self.search()).grid(row=0, column=3, padx=1)
        Button(labelframe1, text='Show all', font=('arial', 10, 'bold'),
               bg='blue', fg='white',command=lambda :self.fetchroom()).grid(row=0, column=4, padx=1)
        xf = Frame(labelframe1, bd=3, relief=RIDGE)
        xf.place(x=0, y=40, width=1230, height=170)
        x = ttk.Scrollbar(xf, orient=HORIZONTAL)
        y = ttk.Scrollbar(xf, orient=VERTICAL)
        self.student_tabel = ttk.Treeview(xf, columns=(
            'MOBILE_NO', 'CHECK_IN', 'CHECK_OUT', 'HOSTEL_NO', 'ROOM_TYPE', 'AVAILABLE_ROOM', 'MESS_NO', 'DAYS', 'COST','TIME'), xscrollcommand=x.set, yscrollcommand=y.set)
        x.pack(side=BOTTOM, fill=X)
        y.pack(side=RIGHT, fill=Y)
        x.config(command=self.student_tabel.xview)
        y.config(command=self.student_tabel.yview)
        self.student_tabel.heading('MOBILE_NO', text='MOBILE_NO')
        self.student_tabel.heading('CHECK_IN', text='CHECK_IN')
        self.student_tabel.heading('CHECK_OUT', text='CHECK_OUT')
        self.student_tabel.heading('HOSTEL_NO', text='HOSTEL_NO')
        self.student_tabel.heading('ROOM_TYPE', text='ROOM_TYPE')
        self.student_tabel.heading('AVAILABLE_ROOM', text='AVAILABLE_ROOM')
        self.student_tabel.heading('MESS_NO', text='MESS_NO')
        self.student_tabel.heading('DAYS', text='MONTHS')
        self.student_tabel.heading('COST', text='COST')
        self.student_tabel.heading('TIME', text='TIME')
        self.student_tabel.column('MOBILE_NO', width=100)
        self.student_tabel.column('CHECK_IN', width=100)
        self.student_tabel.column('CHECK_OUT', width=100)
        self.student_tabel.column('HOSTEL_NO', width=100)
        self.student_tabel.column('ROOM_TYPE', width=100)
        self.student_tabel.column('AVAILABLE_ROOM', width=100)
        self.student_tabel.column('MESS_NO', width=100)
        self.student_tabel.column('DAYS', width=100)
        self.student_tabel.column('COST', width=100)
        self.student_tabel.column('TIME', width=100)
        self.student_tabel['show'] = 'headings'
        self.student_tabel.pack(fill=BOTH, expand=1)
        self.student_tabel.bind("<ButtonRelease-1>",self.get_curser)
        self.fetchroom()

    def fetchcontact(self):
         if self.var_contact.get()=="":
            messagebox.showerror("Error!!!!!!","Please Enter Contact No.......",parent=self.root3)
         else:
          conn = mysql.connector.connect( host="localhost", username='root', password='Test@123', database='hostel')
          my_cusror = conn.cursor()
          my_cusror.execute("select FIRST_NAME from students where MOBILE_NO=%s ",(self.var_contact.get(),))
          row = my_cusror.fetchone()
          if row ==None:
              messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
          else:
              conn.commit()
              conn.close()
              showframedata = Frame(self.root3, bd=5, relief=RIDGE,bg='black').place(x=456, y=40, width=808, height=355)
              hi=Label(self.root3,text='Name:', font=('arial', 10, 'bold','underline'),bg='black',fg='white')
              hi.place(x=470,y=50)
              Label(self.root3,text=row, font=('arial', 10, 'bold'),bg='black',fg='white').place(x=520,y=50)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123', database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select MOBILE_NO from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Mobile No:', font=('arial', 10, 'bold','underline'), bg='black', fg='white')
                  hi.place(x=470, y=80)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=540, y=80)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                                 database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select EMAIL from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                      messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                      conn.commit()
                      conn.close()
                      hi = Label(self.root3, text='Email ID:', font=('arial', 10, 'bold','underline'), bg='black', fg='white')
                      hi.place(x=470, y=110)
                      Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=530, y=110)
              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select GENDER from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Gender:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=470, y=140)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=530, y=140)
              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select DOCUMENT from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Document:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=470, y=170)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=545, y=170)
              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select DOCUMENT_NO from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Document No:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=470, y=200)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=565, y=200)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select DOB from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='DOB:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=470, y=230)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=515, y=230)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select CITY from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='City:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=470, y=260)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=510, y=260)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select STATE from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='State:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=470, y=290)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=520, y=290)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select PINCODE from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Pincode:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=470, y=320)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=530, y=320)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select ADDRESS from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Address:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=470, y=350)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=530, y=350)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select COLLAGE_NAME from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='College:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=750, y=50)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=810, y=50)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select SEMESTER from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Semester:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=750, y=80)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=820, y=80)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select YEAR from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Year:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=750, y=110)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=790, y=110)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select APPLICATION_NO from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Application No:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=750, y=140)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=850, y=140)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select DATE from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Date of Applying:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=750, y=170)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=870, y=170)

              conn = mysql.connector.connect(host="localhost", username='root', password='Test@123',
                                             database='hostel')
              my_cusror = conn.cursor()
              my_cusror.execute("select TIME from students where MOBILE_NO=%s ", (self.var_contact.get(),))
              row = my_cusror.fetchone()
              if row == None:
                  messagebox.showerror("Error!!!!!!", "NOT FOUND .......", parent=self.root3)
              else:
                  conn.commit()
                  conn.close()
                  hi = Label(self.root3, text='Time of Applying:', font=('arial', 10, 'bold', 'underline'), bg='black',
                             fg='white')
                  hi.place(x=750, y=200)
                  Label(self.root3, text=row, font=('arial', 10, 'bold'), bg='black', fg='white').place(x=870, y=200)

          def time():
              string = strftime("%H:%M:%S %p \n %d/%m/%Y")
              lbl.config(text=string)
              lbl.after(1000, time)

          lbl = Label(self.root3, font="times 12 bold")
          lbl.place(x=1150, y=50)
          time()

    def Add_data(self):
              if self.var_contact.get() == "":

                  messagebox.showerror(
                      "ERROR !!!!", "ALL FIELDS ARE REQUIRED \n             OR           \nInitial Amount >=500 ",
                      parent=self.root3)
              else:
                  try:
                      conn = mysql.connector.connect(
                          host="localhost", username='root', password='Test@123', database='hostel')
                      my_cusror = conn.cursor()
                      query = "insert into rooms (MOBILE_NO,CHECK_IN,CHECK_OUT,HOSTEL_NO,ROOM_TYPE,AVAILABLE_ROOM,MESS_NO,DAYS,COST,TIME) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                      arg = (self.var_contact.get(), self.date.get(), self.var_checkout.get(), self.var_hostelno.get(),
                             self.var_roomty.get(), self.var_available.get(), self.var_messno.get(), self.var_month.get(),
                             self.var_cost.get(), self.var_time.get())
                      my_cusror.execute(query, arg)
                      conn.commit()
                      self.fetchroom()
                      conn.close()
                      messagebox.showinfo('Student Details',
                                          f'ADDED SUCCUSEFULLY \n______________________________________________________________\n',
                                          parent=self.root3)
                  except Exception as es:
                      messagebox.showerror("ERROR", f"DUE TO:{str(es)}")

    def fetchroom(self):
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select * from rooms")
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

        self.var_contact.set(row[0]),
        self.date.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_hostelno.set(row[3]),
        self.var_roomty.set(row[4]),
        self.var_available.set(row[5]),
        self.var_messno.set(row[6]),
        self.var_month.set(row[7]),
        self.var_cost.set(row[8]),
        self.var_time.set(row[9]),

    def Update(self):
        if self.var_contact.get() == "":

            messagebox.showerror(
                "ERROR !!!!", "ALL FIELDS ARE REQUIRED \n             OR           \nInitial Amount >=500 ",
                parent=self.root3)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username='root', password='Test@123', database='hostel')
                my_cusror = conn.cursor()


                my_cusror.execute("update rooms set CHECK_IN=%s,CHECK_OUT=%s,HOSTEL_NO=%s,ROOM_TYPE=%s,AVAILABLE_ROOM=%s,MESS_NO=%s,DAYS=%s,COST=%s,TIME=%s,where MOBILE_NO=%s",( self.date.get(), self.var_checkout.get(), self.var_hostelno.get(),
                             self.var_roomty.get(), self.var_available.get(), self.var_messno.get(), self.var_month.get(),
                             self.var_cost.get(), self.var_time.get(),self.var_contact.get()))
                conn.commit()
                self.fetchroom()
                conn.close()
                messagebox.showinfo('Room Details',
                                    f'UPDATE SUCCUSEFULLY \n______________________________________________________________\n',
                                    parent=self.root3)
            except Exception as es:
                messagebox.showerror("ERROR", f"DUE TO:{str(es)}",parent=self.root3)

    def delete(self):
            mdelete = messagebox.askyesno("Hostel management software", "DO YOU WANT TO DELETE THIS STUDENT",
                                          parent=self.root3)
            conn = mysql.connector.connect(
                host="localhost", username='root', password='Test@123', database='hostel')
            if mdelete > 0:
                my_cusror = conn.cursor()
                my_cusror.execute("delete from rooms where MOBILE_NO=%s", (self.var_contact.get(),))
            else:
                if not mdelete:
                    return
            conn.commit()
            self.fetchroom()
            conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.date.set(""),
        self.var_checkout.set(""),
        self.var_hostelno.set(""),
        self.var_roomty.set(""),
        self.var_available.set(""),
        self.var_messno.set(""),
        self.var_month.set(""),
        self.var_cost.set(""),
        self.var_time.set(""),

    def search(self):
        conn = mysql.connector.connect( host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select * from rooms where "+str(self.var_search.get())+"='"+str(self.var_ent_search.get())+"'")
        row = my_cusror.fetchall()
        if len(row) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in row:
                self.student_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    def back(self):
        self.root3.destroy()


    def total(self):
        indate=self.date.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_month.set(abs(outdate-indate).days)

        if self.var_roomty.get()=='Double Bed':
            q1=float(450)
            q2=float(self.var_month.get())
            q3=float(q1*q2)
            q4 = "RS. " + str(q3)
            self.var_cost.set(q4)
        elif self.var_roomty.get()=='Triple Bed':
                q1 = float(500)
                q2 = float(self.var_month.get())
                q3 = float(q1 * q2)
                q4="RS. "+str(q3)
                self.var_cost.set(q4)


if __name__ == "__main__":
    root3 = Tk()
    obj = Roomallocation(root3)

    root3.mainloop()