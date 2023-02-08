from tkinter import *
import random
import tk as tk
from PIL import ImageTk, Image
from time import strftime
from tkinter import filedialog
import pickle
import mysql.connector
from tkinter import ttk, messagebox


class Student:

    def __init__(self, root2):

        self.root2 = root2
        self.root2.geometry("1260x638+255+150")
        self.root2.iconbitmap(
            'E:\python\Hostel Management Software\images\icon.ico')
        self.root2.title("HOSTEL MANAGEMENT SOFTWARE")

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
        self.var_apno=StringVar()
        self.var_search=StringVar()
        self.var_ent_search=StringVar()

        x=random.randint(100000,999999)
        self.var_apno.set(str(x))
        l = Label(self.root2, bd=10, relief=RIDGE, text="ADD STUDENTS DETAILS", fg='YELLOW', bg='black',
                  font=("times new roman", 18, 'bold', 'underline'))
        l.pack(side=TOP, fill=X)
        # students details
        labelframe = LabelFrame(self.root2, text='Student Details', font=("times new roman", 12, "bold"), bd=2, relief=RIDGE,
                                padx=2, bg='sky blue')
        labelframe.place(x=0, y=40, width=585, height=715)

        Label(labelframe, text="First Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=0,
                                                                                                               column=0,
                                                                                                               sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_name )
        nen.grid(row=0, column=1)
        Label(labelframe, text="Last Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=1, column=0,
                                                                                                              sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_last)
        nen.grid(row=1, column=1)
        Label(labelframe, text="Father Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=2,
                                                                                                                column=0,
                                                                                                                sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_father)
        nen.grid(row=2, column=1)
        Label(labelframe, text="Mother Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_mother)
        nen.grid(row=3, column=1)
        Label(labelframe, text="Mobile No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=4, column=0,
                                                                                                              sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_mobile_no)
        nen.grid(row=4, column=1)
        Label(labelframe, text="Email Id: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=5, column=0,
                                                                                                             sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_email)
        nen.grid(row=5, column=1)
        Label(labelframe, text="City: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=7, column=0,
                                                                                                         sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_city)
        nen.grid(row=7, column=1)
        Label(labelframe, text="State: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=8, column=0,
                                                                                                          sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_state)
        nen.grid(row=8, column=1)
        Label(labelframe, text="Pincode: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=9, column=0,
                                                                                                            sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_pincode)
        nen.grid(row=9, column=1)
        Label(labelframe, text="Address: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=10, column=0,
                                                                                                            sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_address)
        nen.grid(row=10, column=1)
        Label(labelframe, text="Gender: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=11, column=0,
                                                                                                           sticky=W)
        gen = ttk.Combobox(labelframe, font=(
            'arial', 10, 'bold'), width=23, state="readonly",textvariable=self.var_gender)
        gen['values'] = ("Male", "Female", "Other")
        gen.grid(row=11, column=1)
        Label(labelframe, text="DOB: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=12, column=0,
                                                                                                        sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_dob)
        nen.grid(row=12, column=1)
        Label(labelframe, text="Collage Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=13,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_college)
        nen.grid(row=13, column=1)

        Label(labelframe, text="Semester: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=14, column=0,
                                                                                                             sticky=W)
        gen = ttk.Combobox(labelframe, font=(
            'arial', 10, 'bold'), width=23, state="readonly",textvariable=self.var_sem)
        gen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8")
        gen.grid(row=14, column=1)
        Label(labelframe, text="Year: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=15,
                                                                                                         column=0,
                                                                                                         sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_year)
        nen.grid(row=15, column=1)
        doc = Label(labelframe, text='Documents:', font=(
            'arial', 10, 'bold'), bg='sky blue').grid(row=16, column=0, sticky=W)
        doc1 = ttk.Combobox(labelframe, font=('arial', 10, 'bold'),
                            width=23, state="readonly",textvariable=self.var_document)
        doc1['value'] = ('Select', 'Aadhar Card', 'PAN Card',
                         'Driving Licence', 'Voter ID')
        doc1.grid(row=16, column=1)
        Label(labelframe, text="Document No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=17,
                                                                                                                column=0,
                                                                                                                sticky=W)
        de = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_document_no)
        de.grid(row=17, column=1)

        # gradian details
        Label(labelframe, text="Local gradian ", font=('arial', 10, 'bold', 'underline'), pady=6, padx=2, bg="sky blue").grid(
            row=1, column=2)
        Label(labelframe, text="Gradian Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=2,
                                                                                                                 column=2,
                                                                                                                 sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_gname)
        nen.grid(row=2, column=3)
        Label(labelframe, text="Address: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=3, column=2,
                                                                                                            sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_gaddress)
        nen.grid(row=3, column=3)
        Label(labelframe, text="Mobile No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=4, column=2,
                                                                                                              sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_gmobile)
        nen.grid(row=4, column=3)
        Label(labelframe, text="Email Id: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=5, column=2,
                                                                                                             sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_gmail)
        nen.grid(row=5, column=3)

        Label(labelframe, text="Aadhar card No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=7,
                                                                                                                   column=2,
                                                                                                                   sticky=W)
        de = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_gdoc)
        de.grid(row=7, column=3)

        # parents details

        Label(labelframe, text="Parent Contact details ", font=('arial', 10, 'bold', 'underline'), pady=6, padx=2,
              bg="sky blue").grid(
            row=9, column=2)

        Label(labelframe, text="Mobile No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=10,
                                                                                                              column=2,
                                                                                                              sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_pmobile)
        nen.grid(row=10, column=3)
        Label(labelframe, text="Email Id: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=11, column=2,
                                                                                                             sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_pmail)
        nen.grid(row=11, column=3)

        Label(labelframe, text="Aadhar card No: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=12,
                                                                                                                   column=2,
                                                                                                                   sticky=W)
        de = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_pdoc)
        de.grid(row=12, column=3, sticky=E)
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
            column=2,
            sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25, textvariable=self.var_apno,state="readonly")
        nen.grid(row=13, column=3)

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
        labelframe1 = LabelFrame(self.root2, text='View Details and Search System', font=("times new roman", 12, "bold"),
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
            'FIRST_NAME', 'LAST_NAME', 'FATHER_NAME', 'MOTHER_NAME', 'MOBILE_NO', 'EMAIL', 'CITY', 'STATE', 'PINCODE',
            'ADDRESS', 'GENDER', 'DOB', 'COLLAGE_NAME', 'SEMESTER', 'YEAR', 'DOCUMENT', 'DOCUMENT_NO', 'GRADIAN_NAME',
            'GRADIAN_ADDRESS', 'GRADIAN_MOBILE', 'GRADIAN_MAIL', 'GRADIAN_DOCUMENT', 'PARENT_MOBILE', 'PARENT_MAIL',
            'PARENT_DOCUMENT','TIME','DATE','APPLICATION_NO'), xscrollcommand=x.set, yscrollcommand=y.set)
        x.pack(side=BOTTOM, fill=X)
        y.pack(side=RIGHT, fill=Y)
        x.config(command=self.student_tabel.xview)
        y.config(command=self.student_tabel.yview)
        self.student_tabel.heading('FIRST_NAME', text='FIRST_NAME')
        self.student_tabel.heading('LAST_NAME', text='LAST_NAME')
        self.student_tabel.heading('FATHER_NAME', text='FATHER_NAME')
        self.student_tabel.heading('MOTHER_NAME', text='MOTHER_NAME')
        self.student_tabel.heading('MOBILE_NO', text='MOBILE_NO')
        self.student_tabel.heading('EMAIL', text='EMAIL')
        self.student_tabel.heading('CITY', text='CITY')
        self.student_tabel.heading('STATE', text='STATE')
        self.student_tabel.heading('PINCODE', text='PINCODE')
        self.student_tabel.heading('ADDRESS', text='ADDRESS')
        self.student_tabel.heading('GENDER', text='GENDER')
        self.student_tabel.heading('DOB', text='DOB')
        self.student_tabel.heading('COLLAGE_NAME', text='COLLAGE_NAME')
        self.student_tabel.heading('SEMESTER', text='SEMESTER')
        self.student_tabel.heading('YEAR', text='YEAR')
        self.student_tabel.heading('DOCUMENT', text='DOCUMENT')
        self.student_tabel.heading('DOCUMENT_NO', text='DOCUMENT_NO')
        self.student_tabel.heading('GRADIAN_NAME', text='GRADIAN_NAME')
        self.student_tabel.heading('GRADIAN_ADDRESS', text='GRADIAN_ADDRESS')
        self.student_tabel.heading('GRADIAN_MOBILE', text='GRADIAN_MOBILE')
        self.student_tabel.heading('GRADIAN_MAIL', text='GRADIAN_MAIL')
        self.student_tabel.heading('GRADIAN_DOCUMENT', text='GRADIAN_DOCUMENT')
        self.student_tabel.heading('PARENT_MOBILE', text='PARENT_MOBILE')
        self.student_tabel.heading('PARENT_MAIL', text='PARENT_MAIL')
        self.student_tabel.heading('PARENT_DOCUMENT', text='PARENT_DOCUMENT')
        self.student_tabel.heading('APPLICATION_NO', text='APPLICATION_NO')
        self.student_tabel.heading('TIME', text='TIME')
        self.student_tabel.heading('DATE', text='DATE')


        self.student_tabel.column('FIRST_NAME', width=100)
        self.student_tabel.column('LAST_NAME', width=100)
        self.student_tabel.column('FATHER_NAME', width=100)
        self.student_tabel.column('MOTHER_NAME', width=100)
        self.student_tabel.column('MOBILE_NO', width=100)
        self.student_tabel.column('EMAIL', width=100)
        self.student_tabel.column('CITY', width=100)
        self.student_tabel.column('STATE', width=100)
        self.student_tabel.column('PINCODE', width=100)
        self.student_tabel.column('ADDRESS', width=100)
        self.student_tabel.column('GENDER', width=100)
        self.student_tabel.column('DOB', width=100)
        self.student_tabel.column('COLLAGE_NAME', width=100)
        self.student_tabel.column('SEMESTER', width=100)
        self.student_tabel.column('YEAR', width=100)
        self.student_tabel.column('DOCUMENT', width=100)
        self.student_tabel.column('DOCUMENT_NO', width=100)
        self.student_tabel.column('GRADIAN_NAME', width=100)
        self.student_tabel.column('GRADIAN_ADDRESS', width=100)
        self.student_tabel.column('GRADIAN_MOBILE', width=100)
        self.student_tabel.column('GRADIAN_MAIL', width=100)
        self.student_tabel.column('GRADIAN_DOCUMENT', width=100)
        self.student_tabel.column('PARENT_MOBILE', width=100)
        self.student_tabel.column('PARENT_MAIL', width=100)
        self.student_tabel.column('PARENT_DOCUMENT', width=100)
        self.student_tabel.column('APPLICATION_NO', width=100)

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
                "ERROR !!!!", "ALL FIELDS ARE REQUIRED \n             OR           \nInitial Amount >=500 ", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username='root', password='Test@123', database='hostel')
                my_cusror = conn.cursor()
                query="insert into students (FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,MOBILE_NO,EMAIL,CITY,STATE,PINCODE,ADDRESS,GENDER,DOB,COLLAGE_NAME,SEMESTER,YEAR,DOCUMENT,DOCUMENT_NO,GRADIAN_NAME,GRADIAN_ADDRESS,GRADIAN_MOBILE,GRADIAN_MAIL,GRADIAN_DOCUMENT,PARENT_MOBILE,PARENT_MAIL,PARENT_DOCUMENT,TIME,DATE,APPLICATION_NO) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                arg=(self.var_name.get(),self.var_last.get(),self.var_father.get(),self.var_mother.get(),self.var_mobile_no.get(),self.var_email.get(),self.var_city.get(),self.var_state.get(),self.var_pincode.get(),self.var_address.get(),self.var_gender.get(),self.var_dob.get(),self.var_college.get(),self.var_sem.get(),self.var_year.get(),self.var_document.get(),self.var_document_no.get(),self.var_gname.get(),self.var_gaddress.get(),self.var_gmobile.get(),self.var_gmail.get(),self.var_gdoc.get(),self.var_pmobile.get(),self.var_pmail.get(),self.var_pdoc.get(),self.var_time.get(),self.var_date.get(),self.var_apno.get())
                my_cusror.execute(query, arg)
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo('Student Details', f'ADDED SUCCUSEFULLY \n______________________________________________________________\n', parent=self.root2)
            except Exception as es:
                 messagebox.showerror("ERROR", f"DUE TO:{str(es)}")

    def fetchdata(self):
           conn = mysql.connector.connect(
               host="localhost", username='root', password='Test@123', database='hostel')
           my_cusror = conn.cursor()
           my_cusror.execute("select * from students")
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
        self.var_last.set(row[1]),
        self.var_father.set(row[2]),
        self.var_mother.set(row[3]),
        self.var_mobile_no.set(row[4]),
        self.var_email.set(row[5]),
        self.var_city.set(row[6]),
        self.var_state.set(row[7]),
        self.var_pincode.set(row[8]),
        self.var_address.set(row[9]),
        self.var_gender.set(row[10]),
        self.var_dob.set(row[11]),
        self.var_college.set(row[12]),
        self.var_sem.set(row[13]),
        self.var_year.set(row[14]),
        self.var_document.set(row[15]),
        self.var_document_no.set(row[16]),
        self.var_gname.set(row[17]),
        self.var_gaddress.set(row[18]),
        self.var_gmobile.set(row[19]),
        self.var_gmail.set(row[20]),
        self.var_gdoc.set(row[21]),
        self.var_pmobile.set(row[22]),
        self.var_pmail.set(row[23]),
        self.var_pdoc.set(row[24]),
        self.var_time.set(row[25]),
        self.var_date.set(row[26]),
        self.var_apno.set(row[27])


    def Update(self):
        if self.var_name.get() == "":

            messagebox.showerror(
                "ERROR !!!!", "ALL FIELDS ARE REQUIRED \n             OR           \nInitial Amount >=500 ",
                parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username='root', password='Test@123', database='hostel')
                my_cusror = conn.cursor()


                my_cusror.execute("update students set FIRST_NAME=%s,LAST_NAME=%s,FATHER_NAME=%s,MOTHER_NAME=%s,MOBILE_NO=%s,EMAIL=%s,CITY=%s,STATE=%s,PINCODE=%s,ADDRESS=%s,GENDER=%s,DOB=%s,COLLAGE_NAME=%s,SEMESTER=%s,YEAR=%s,DOCUMENT=%s,DOCUMENT_NO=%s,GRADIAN_NAME=%s,GRADIAN_ADDRESS=%s,GRADIAN_MOBILE=%s,GRADIAN_MAIL=%s,GRADIAN_DOCUMENT=%s,PARENT_MOBILE=%s,PARENT_MAIL=%s,PARENT_DOCUMENT=%s,TIME=%s,DATE=%s where APPLICATION_NO=%s",(self.var_name.get(), self.var_last.get(), self.var_father.get(), self.var_mother.get(),
                       self.var_mobile_no.get(), self.var_email.get(), self.var_city.get(), self.var_state.get(),
                       self.var_pincode.get(), self.var_address.get(), self.var_gender.get(), self.var_dob.get(),
                       self.var_college.get(), self.var_sem.get(), self.var_year.get(), self.var_document.get(),
                       self.var_document_no.get(), self.var_gname.get(), self.var_gaddress.get(),
                       self.var_gmobile.get(), self.var_gmail.get(), self.var_gdoc.get(), self.var_pmobile.get(),
                       self.var_pmail.get(), self.var_pdoc.get(), self.var_time.get(), self.var_date.get(),self.var_apno.get()))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo('Student Details',
                                    f'UPDATE SUCCUSEFULLY \n______________________________________________________________\n',
                                    parent=self.root2)
            except Exception as es:
                messagebox.showerror("ERROR", f"DUE TO:{str(es)}")

    def delete(self):
        mdelete=messagebox.askyesno("Hostel management software","DO YOU WANT TO DELETE THIS STUDENT",parent=self.root2)
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        if  mdelete >0:
            my_cusror = conn.cursor()
            my_cusror.execute("delete from students where APPLICATION_NO=%s",(self.var_apno.get(),))
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetchdata()
        conn.close()

    def reset(self):
        self.var_name.set(""),
        self.var_last.set(""),
        self.var_father.set(""),
        self.var_mother.set(""),
        self.var_mobile_no.set(""),
        self.var_email.set(""),
        self.var_city.set(""),
        self.var_state.set(""),
        self.var_pincode.set(""),
        self.var_address.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_college.set(""),
        self.var_sem.set(""),
        self.var_year.set(""),
        self.var_document.set(""),
        self.var_document_no.set(""),
        self.var_gname.set(""),
        self.var_gaddress.set(""),
        self.var_gmobile.set(""),
        self.var_gmail.set(""),
        self.var_gdoc.set(""),
        self.var_pmobile.set(""),
        self.var_pmail.set(""),
        self.var_pdoc.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        x = random.randint(100000, 999999)
        self.var_apno.set(str(x))

    def search(self):
        conn = mysql.connector.connect( host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select * from students where "+str(self.var_search.get())+"='"+str(self.var_ent_search.get())+"'")
        row = my_cusror.fetchall()
        if len(row) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in row:
                self.student_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    def back(self):
        self.root2.destroy()







if __name__ == "__main__":
    root2 = Tk()
    obj = Student(root2)

    root2.mainloop()
