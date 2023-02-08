from tkinter import *
import random
import tk as tk
from PIL import ImageTk, Image
from time import strftime
from tkinter import filedialog
import pickle
import mysql.connector
from tkinter import ttk, messagebox


class Emp:

    def __init__(self, root7):

        self.root7 = root7
        self.root7.geometry("1260x638+255+150")
        self.root7.iconbitmap(
            'E:\python\Hostel Management Software\images\icon.ico')
        self.root7.title("HOSTEL MANAGEMENT SOFTWARE")

        # VARIABELS
        self.var_name = StringVar()
        self.var_father = StringVar()
        self.var_last = StringVar()
        self.var_address = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_document = StringVar()
        self.var_document_no = StringVar()
        self.var_sem = StringVar()
        self.var_year = StringVar()
        self.var_college = StringVar()
        self.var_mother = StringVar()
        self.var_mobile_no = StringVar()
        self.var_email = StringVar()
        self.var_gname = StringVar()
        self.var_city = StringVar()
        self.var_state = StringVar()
        self.var_pincode = StringVar()
        self.var_gaddress = StringVar()
        self.var_gmobile = StringVar()
        self.var_gmail = StringVar()
        self.var_gdoc = StringVar()
        self.var_pmobile = StringVar()
        self.var_pmail = StringVar()
        self.var_pdoc = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_empno=StringVar()
        self.var_search=StringVar()
        self.var_ent_search=StringVar()

        x=random.randint(100000,999999)
        self.var_empno.set(str(x))
        l = Label(self.root7, bd=10, relief=RIDGE, text="ADD EMPLOYEE DETAILS", fg='YELLOW', bg='black',
                  font=("times new roman", 18, 'bold', 'underline'))
        l.pack(side=TOP, fill=X)
        # students details
        labelframe = LabelFrame(self.root7, text='Employee Details', font=("times new roman", 12, "bold"), bd=2, relief=RIDGE,
                                padx=2, bg='sky blue')
        labelframe.place(x=0, y=40, width=585, height=715)

        Label(labelframe, text="First Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=0,
                                                                                                               column=0,
                                                                                                               sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_name )
        nen.grid(row=0, column=1)
        Label(labelframe, text="Middle Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=1, column=0,
                                                                                                              sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_father)
        nen.grid(row=1, column=1)
        Label(labelframe, text="Last Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=2,
                                                                                                                column=0,
                                                                                                                sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_last)
        nen.grid(row=2, column=1)

        Label(labelframe, text="Mobile No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=3, column=0,
                                                                                                              sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_mobile_no)
        nen.grid(row=3, column=1)
        Label(labelframe, text="Email Id: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=4, column=0,
                                                                                                             sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_email)
        nen.grid(row=4, column=1)
        Label(labelframe, text="City: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=5, column=0,
                                                                                                         sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_city)
        nen.grid(row=5, column=1)
        Label(labelframe, text="State: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=6, column=0,
                                                                                                          sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_state)
        nen.grid(row=6, column=1)
        Label(labelframe, text="Pincode: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=7, column=0,
                                                                                                            sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_pincode)
        nen.grid(row=7, column=1)
        Label(labelframe, text="Address: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=8, column=0,
                                                                                                            sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_address)
        nen.grid(row=8, column=1)
        Label(labelframe, text="Gender: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=9, column=0,
                                                                                                           sticky=W)
        gen = ttk.Combobox(labelframe, font=(
            'arial', 10, 'bold'), width=23, state="readonly",textvariable=self.var_gender)
        gen['values'] = ("Male", "Female", "Other")
        gen.grid(row=9, column=1)
        Label(labelframe, text="DOB: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=10, column=0,
                                                                                                        sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_dob)
        nen.grid(row=10, column=1)

        doc = Label(labelframe, text='Documents:', font=(
            'arial', 10, 'bold'), bg='sky blue').grid(row=11, column=0, sticky=W)
        doc1 = ttk.Combobox(labelframe, font=('arial', 10, 'bold'),
                            width=23, state="readonly",textvariable=self.var_document)
        doc1['value'] = ('Select', 'Aadhar Card', 'PAN Card',
                         'Driving Licence', 'Voter ID')
        doc1.grid(row=11, column=1)
        Label(labelframe, text="Document No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=12,
                                                                                                                column=0,
                                                                                                                sticky=W)
        de = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_document_no)
        de.grid(row=12, column=1)

        # TIME
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly",textvariable=self.var_time)
        ca['value'] = (strftime('%H:%M'))
        ca.current(0)
        ca.place(x=3900, y=1000)
        ca1 = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                           width=8, state="readonly",textvariable=self.var_date)
        ca1['value'] = (strftime('%d/%m/%Y'))
        ca1.current(0)
        ca1.place(x=3900, y=1000)
        Label(labelframe, text="Application No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(
            row=13,
            column=0,
            sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25, textvariable=self.var_empno,state="readonly")
        nen.grid(row=13, column=1)

        btf = Frame(labelframe, bd=3, relief=RIDGE)
        btf.place(x=0, y=540, width=400, height=35)
        Button(btf, text='Add', font=('arial', 10, 'bold'), bg='black', fg='gold', width=11,
               command=lambda: self.Add_data()).grid(row=0, column=0)
        Button(btf, text='Update', font=('arial', 10, 'bold'),
               bg='black', fg='gold', width=11,command=lambda :self.Update()).grid(row=0, column=1)
        Button(btf, text='Delete', font=('arial', 10, 'bold'),
               bg='black', fg='gold', width=11,command=lambda :self.delete()).grid(row=0, column=2)
        Button(btf, text='Reset', font=('arial', 10, 'bold'),
               bg='black', fg='gold', width=11,command=lambda :self.reset()).grid(row=0, column=3)
        labelframe1 = LabelFrame(self.root7, text='View Details and Search System', font=("times new roman", 12, "bold"),
                                 bd=2, relief=RIDGE, padx=2, bg='light yellow')
        labelframe1.place(x=585, y=40, width=675, height=620)

        Label(labelframe1, text="Search by:-", font=('arial', 12, 'bold'), bg='red', fg='white').grid(row=0, column=0,
                                                                                                      sticky=W)
        search = ttk.Combobox(labelframe1, font=("times new roman", 12, 'bold'),
                              width=24, state="readonly",textvariable=self.var_search)
        search['value'] = ('Select', 'APPLICATION_NO', 'MOBILE_NO')
        search.grid(row=0, column=1, padx=2)
        ttk.Entry(labelframe1, width=20, font=(
            'arial', 10, 'bold'),textvariable=self.var_ent_search).grid(row=0, column=2, padx=2)
        Button(labelframe1, text='BACK', font=('arial', 10, 'bold'),
               bg='grey', fg='black',command=lambda :self.back()).grid(row=0, column=5, padx=2)
        Button(labelframe1, text='Search', font=('arial', 10, 'bold'),
               bg='blue', fg='white',command=lambda :self.search()).grid(row=0, column=3, padx=1)
        Button(labelframe1, text='Show all', font=('arial', 10, 'bold'),
               bg='blue', fg='white',command=lambda :self.fetchdata()).grid(row=0, column=4, padx=1)
        xf = Frame(labelframe1, bd=3, relief=RIDGE)
        xf.place(x=0, y=50, width=670, height=520)
        x = ttk.Scrollbar(xf, orient=HORIZONTAL)
        y = ttk.Scrollbar(xf, orient=VERTICAL)

        self.student_tabel = ttk.Treeview(xf, columns=(
            'FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME', 'MOBILE_NO', 'EMAIL', 'CITY', 'STATE', 'PINCODE',
            'ADDRESS', 'GENDER', 'DOB' ,'DOCUMENT', 'DOCUMENT_NO','TIME','DATE','EMPLOYEE_NO'), xscrollcommand=x.set, yscrollcommand=y.set)
        x.pack(side=BOTTOM, fill=X)
        y.pack(side=RIGHT, fill=Y)
        x.config(command=self.student_tabel.xview)
        y.config(command=self.student_tabel.yview)
        self.student_tabel.heading('FIRST_NAME', text='FIRST_NAME')
        self.student_tabel.heading('LAST_NAME', text='LAST_NAME')
        self.student_tabel.heading('MIDDLE_NAME', text='MIDDLE_NAME')
        self.student_tabel.heading('MOBILE_NO', text='MOBILE_NO')
        self.student_tabel.heading('EMAIL', text='EMAIL')
        self.student_tabel.heading('CITY', text='CITY')
        self.student_tabel.heading('STATE', text='STATE')
        self.student_tabel.heading('PINCODE', text='PINCODE')
        self.student_tabel.heading('ADDRESS', text='ADDRESS')
        self.student_tabel.heading('GENDER', text='GENDER')
        self.student_tabel.heading('DOB', text='DOB')
        self.student_tabel.heading('DOCUMENT', text='DOCUMENT')
        self.student_tabel.heading('DOCUMENT_NO', text='DOCUMENT_NO')
        self.student_tabel.heading('EMPLOYEE_NO', text='EMPLOYEE_NO')
        self.student_tabel.heading('TIME', text='TIME')
        self.student_tabel.heading('DATE', text='DATE')


        self.student_tabel.column('FIRST_NAME', width=100)
        self.student_tabel.column('LAST_NAME', width=100)
        self.student_tabel.column('MIDDLE_NAME', width=100)
        self.student_tabel.column('MOBILE_NO', width=100)
        self.student_tabel.column('EMAIL', width=100)
        self.student_tabel.column('CITY', width=100)
        self.student_tabel.column('STATE', width=100)
        self.student_tabel.column('PINCODE', width=100)
        self.student_tabel.column('ADDRESS', width=100)
        self.student_tabel.column('GENDER', width=100)
        self.student_tabel.column('DOB', width=100)
        self.student_tabel.column('DOCUMENT', width=100)
        self.student_tabel.column('DOCUMENT_NO', width=100)
        self.student_tabel.column('EMPLOYEE_NO', width=100)
        self.student_tabel['show'] = 'headings'
        self.student_tabel.pack(fill=BOTH, expand=1)
        self.student_tabel.bind("<ButtonRelease-1>",self.get_curser)
        self.fetchdata()


        def time():
            string = strftime("%H:%M:%S %p \n %d/%m/%Y")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(labelframe, font="times 12 bold")
        lbl.grid(row=0, column=2)
        time()

    def Add_data(self):
        if self.var_name.get() == "":

            messagebox.showerror(
                "ERROR !!!!", "ALL FIELDS ARE REQUIRED \n        ", parent=self.root7)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username='root', password='Test@123', database='hostel')
                my_cusror = conn.cursor()
                query="insert into employee (FIRST_NAME,MIDDLE_NAME,LAST_NAME,MOBILE_NO,EMAIL,CITY,STATE,PINCODE,ADDRESS,GENDER,DOB,DOCUMENT,DOCUMENT_NO,TIME,DATE,EMPLOYEE_NO) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                arg=(self.var_name.get(),self.var_father.get(),self.var_last.get(),self.var_mobile_no.get(),self.var_email.get(),self.var_city.get(),self.var_state.get(),self.var_pincode.get(),self.var_address.get(),self.var_gender.get(),self.var_dob.get(),self.var_document.get(),self.var_document_no.get(),self.var_time.get(),self.var_date.get(),self.var_empno.get())
                my_cusror.execute(query, arg)
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo('Employee Details', f'ADDED SUCCUSEFULLY \n______________________________________________________________\n', parent=self.root7)
            except Exception as es:
                 messagebox.showerror("ERROR", f"DUE TO:{str(es)}")

    def fetchdata(self):
           conn = mysql.connector.connect(
               host="localhost", username='root', password='Test@123', database='hostel')
           my_cusror = conn.cursor()
           my_cusror.execute("select * from employee")
           row=my_cusror.fetchall()
           if len(row)!=0:
               self.student_tabel.delete(*self.student_tabel.get_children())
               for i in row:
                   self.student_tabel.insert("",END,values=i)
               conn.commit()
           conn.close()



    def get_curser(self,event=" "):
        crow=self.student_tabel.focus()
        con=self.student_tabel.item(crow)
        row=con["values"]

        self.var_name.set(row[0]),
        self.var_father.set(row[1]),
        self.var_last.set(row[2]),
        self.var_mobile_no.set(row[3]),
        self.var_email.set(row[4]),
        self.var_city.set(row[5]),
        self.var_state.set(row[6]),
        self.var_pincode.set(row[7]),
        self.var_address.set(row[8]),
        self.var_gender.set(row[9]),
        self.var_dob.set(row[10]),
        self.var_document.set(row[11]),
        self.var_document_no.set(row[12]),
        self.var_time.set(row[13]),
        self.var_date.set(row[14]),
        self.var_empno.set(row[15])


    def Update(self):
        if self.var_name.get() == "":

            messagebox.showerror(
                "ERROR !!!!", "ALL FIELDS ARE REQUIRED \n     ",
                parent=self.root7)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username='root', password='Test@123', database='hostel')
                my_cusror = conn.cursor()


                my_cusror.execute("update employee set FIRST_NAME=%s,MIDDLE_NAME=%s,LAST_NAME=%s,MOBILE_NO=%s,EMAIL=%s,CITY=%s,STATE=%s,PINCODE=%s,ADDRESS=%s,GENDER=%s,DOB=%s,DOCUMENT=%s,DOCUMENT_NO=%s,TIME=%s,DATE=%s where EMPLOYEE_NO=%s",(self.var_name.get(), self.var_father.get(), self.var_last.get(),
                       self.var_mobile_no.get(), self.var_email.get(), self.var_city.get(), self.var_state.get(),
                       self.var_pincode.get(), self.var_address.get(), self.var_gender.get(), self.var_dob.get(),
                        self.var_document.get(),
                       self.var_document_no.get(), self.var_time.get(), self.var_date.get(),self.var_empno.get()))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo('Employee Details',
                                    f'UPDATE SUCCUSEFULLY \n______________________________________________________________\n',
                                    parent=self.root7)
            except Exception as es:
                messagebox.showerror("ERROR", f"DUE TO:{str(es)}")

    def delete(self):
        mdelete=messagebox.askyesno("Hostel management software","DO YOU WANT TO DELETE THIS EMPLOYEE",parent=self.root7)
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        if  mdelete >0:
            my_cusror = conn.cursor()
            my_cusror.execute("delete from employee where EMPLOYEE_NO=%s",(self.var_empno.get(),))
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetchdata()
        conn.close()

    def reset(self):
        self.var_name.set(""),
        self.var_father.set(""),
        self.var_last.set(""),
        self.var_mobile_no.set(""),
        self.var_email.set(""),
        self.var_city.set(""),
        self.var_state.set(""),
        self.var_pincode.set(""),
        self.var_address.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_document.set(""),
        self.var_document_no.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        x = random.randint(100000, 999999)
        self.var_empno.set(str(x))

    def search(self):
        conn = mysql.connector.connect( host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select * from employee where "+str(self.var_search.get())+"='"+str(self.var_ent_search.get())+"'")
        row = my_cusror.fetchall()
        if len(row) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in row:
                self.student_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    def back(self):
        self.root7.destroy()







if __name__ == "__main__":
    root7 = Tk()
    obj = Emp(root7)

    root7.mainloop()
