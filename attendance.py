from tkinter import *
import random
import tk as tk
from PIL import ImageTk, Image
from time import strftime
from tkinter import filedialog
import pickle
import mysql.connector
from tkinter import ttk, messagebox


class attendance:

    def __init__(self, root2):

        self.root2 = root2
        self.root2.geometry("1260x638+255+150")
        self.root2.iconbitmap(
            'E:\python\Hostel Management Software\images\icon.ico')
        self.root2.title("HOSTEL MANAGEMENT SOFTWARE")

        # VARIABELS
        self.n = StringVar()
        self.roomno = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.attend = StringVar()

        self.var_date.set(strftime('%d/%m/%Y'))



        l = Label(self.root2, bd=10, relief=RIDGE, text="ATTENDANCE", fg='YELLOW', bg='black',
                  font=("times new roman", 18, 'bold', 'underline'))
        l.pack(side=TOP, fill=X)
        # students details
        labelframe = LabelFrame(self.root2, text='REPORT', font=("times new roman", 12, "bold"), bd=2, relief=RIDGE,
                                padx=2, bg='sky blue')
        labelframe.place(x=0, y=40, width=1258, height=715)

        Label(labelframe, text="First Name: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=0,
                                                                                                               column=0,
                                                                                                               sticky=W)
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select FIRST_NAME from students")
        row = my_cusror.fetchall()
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly", textvariable=self.n)
        ca['value'] = row
        ca.current(0)
        ca.grid(row=0, column=1)

        Label(labelframe, text="ROOM NO: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=2,
                                                                                                                column=0,
                                                                                                                sticky=W)
        conn = mysql.connector.connect(
            host="localhost", username='root', password='Test@123', database='hostel')
        my_cusror = conn.cursor()
        my_cusror.execute("select H_NO from adds")
        row1 = my_cusror.fetchall()
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly", textvariable=self.roomno)
        ca['value'] = row1
        ca.current(0)
        ca.grid(row=2, column=1)
        Label(labelframe, text="Date: ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                sticky=W)
        nen = ttk.Entry(labelframe, font=('arial', 10, 'bold'), width=25,textvariable=self.var_date,state='readonly')
        nen.grid(row=3, column=1)
        Label(labelframe, text="Attendance : ", font=('arial', 10, 'bold'), pady=6, padx=2, bg="sky blue").grid(row=4,
                                                                                                            column=0,
                                                                                                            sticky=W)
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly", textvariable=self.attend)
        ca['value'] = ("Present","Absent")
        ca.current(0)
        ca.grid(row=4, column=1)




        # TIME
        ca = ttk.Combobox(labelframe, font=("times new roman", 12, 'bold'),
                          width=8, state="readonly",textvariable=self.var_time)
        ca['value'] = (strftime('%H:%M'))
        ca.current(0)
        ca.place(x=3900, y=1000)


        btf = Frame(labelframe, bd=3, relief=RIDGE)
        btf.place(x=140, y=160)
        Button(btf, text='Apply', font=('arial', 10, 'bold'), bg='black', fg='gold', width=11,
               command=lambda: self.Add_data()).grid(row=0, column=0)
        Button(btf, text='Back', font=('arial', 10, 'bold'), bg='black', fg='gold', width=11,
               command=lambda: self.back()).grid(row=0, column=2)

        img5 = Image.open(r"E:\python\Hostel Management Software\images\pass.jpg")
        img5 = img5.resize((600, 550), Image.ANTIALIAS)
        self.photo5 = ImageTk.PhotoImage(img5)
        p5 = Label(self.root2, image=self.photo5, bd=4, relief=RIDGE)
        p5.place(x=600, y=60, width=600, height=550)


        def time():
            string = strftime("%H:%M:%S %p \n %d/%m/%Y")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(labelframe, font="times 12 bold")
        lbl.grid(row=0, column=3)
        time()

    def Add_data(self):
        if self.n.get() == "":

            messagebox.showerror(
                "ERROR !!!!", "ALL FIELDS ARE REQUIRED \n  ", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username='root', password='Test@123', database='hostel')
                my_cusror = conn.cursor()
                query = "insert into attendance (FIRST_NAME,ROOM_NO,DATE,TIME) values (%s,%s,%s,%s)"
                arg = (self.n.get(), self.roomno.get(),self.var_date.get(),self.var_time.get())
                my_cusror.execute(query, arg)
                conn.commit()
                conn.close()
                messagebox.showinfo('Attendance ', f' SUCCUSEFULLY \n______________________________________________________________\n', parent=self.root2)
            except Exception as es:
                 messagebox.showerror("ERROR", f"DUE TO:{str(es)}")


    def back(self):
        self.root2.destroy()







if __name__ == "__main__":
    root2 = Tk()
    obj = attendance(root2)

    root2.mainloop()
