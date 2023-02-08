import time
from datetime import datetime
from tkinter import *
from PIL import ImageTk,Image
from time import strftime
from tkinter import ttk, messagebox
import  os
from Students import Student
from room import Roomallocation
from addroom import Addroom
from mess import Mess
from Emp import Emp
from report import report









class Warden:

 def __init__(self, root1):
  self.var_accno2=StringVar()
  self.var_pin2=StringVar()
  self.root1 =root1
  self.root1.geometry("1530x790+0+0")
  self.root1.iconbitmap('E:\python\Hostel Management Software\images\icon.ico')
  self.root1.title("HOSTEL MANAGEMENT SOFTWARE")
  l = Label(self.root1, bd=20, relief=RIDGE, text="HOSTEL MANAGEMENT SOFTWARE", fg='red', bg='black',
            font=("times new roman", 50, 'bold', 'underline'))
  l.pack(side=TOP, fill=X)


  f1 = Frame(self.root1, bd=15, relief=RIDGE, bg='black')
  f1.place(x=0, y=100, width=1528, height=690)
  l12 = Label(root1, text='Copyright @DIPTISH-WORLD 2022', font='15', fg='White', bg='black').place(x=650, y=745)
  mainframe = Frame(f1, bd=2)
  mainframe.place(x=10, y=10, width=1480, height=600)
  Label(mainframe,text='MENU',font=('times new roman',20,'bold'),bg='gold',fg='black',bd=4,relief=RIDGE).place(x=0,y=0,width=230)
  btfram=Frame(mainframe,bd=4,relief=RIDGE)
  btfram.place(x=0,y=35,width=228,height=260)
  Button(btfram,text="Manage Students",font=('times new roman',14,'bold'),width=22,bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand1',command=lambda :self.student()).grid(row=0,column=0,pady=1)
  Button(btfram,text="Room Allocation",font=('times new roman',14,'bold'),width=22,bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand1',command=lambda :self.room()).grid(row=1,column=0,pady=1)
  Button(btfram,text="Attendance",font=('times new roman',14,'bold'),width=22,bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand1',command=lambda :self.addroom()).grid(row=2,column=0,pady=1)
  Button(btfram,text="Report",font=('times new roman',14,'bold'),width=22,bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand1',command=lambda :self.report()).grid(row=3,column=0,pady=1)
  Button(btfram,text="Mess Schedule",font=('times new roman',14,'bold'),width=22,bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand1',command=lambda :self.Mess()).grid(row=5,column=0,pady=1)
  Button(btfram,text="Log out",font=('times new roman',14,'bold'),width=22,bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand1',command=lambda :self.logout()).grid(row=6,column=0,pady=1)

  img = Image.open(r"E:\python\Hostel Management Software\images\img1.jpg")
  img = img.resize((1310, 590), Image.ANTIALIAS)
  self.photo = ImageTk.PhotoImage(img)
  p = Label(mainframe, image=self.photo,bd=4,relief=RIDGE)
  p.place(x=225, y=0, width=1310, height=590)

  img1 = Image.open(r"E:\python\Hostel Management Software\images\img2.jpeg")
  img1 = img1.resize((230, 160), Image.ANTIALIAS)
  self.photo1 = ImageTk.PhotoImage(img1)
  p1 = Label(mainframe, image=self.photo1,bd=4,relief=RIDGE)
  p1.place(x=0, y=295, width=230, height=160)

  img2 = Image.open(r"E:\python\Hostel Management Software\images\img3.jpeg")
  img2 = img2.resize((230, 190), Image.ANTIALIAS)
  self.photo2 = ImageTk.PhotoImage(img2)
  p2 = Label(mainframe, image=self.photo2,bd=4,relief=RIDGE)
  p2.place(x=0, y=440, width=230, height=190)
  l = Label(p, bd=4, relief=RIDGE, text="Warden", fg='red',
            font=("times new roman", 20, 'bold', 'underline'))
  l.pack(side=TOP, fill=X)




  def time():
      string = strftime("%H:%M:%S %p \n %d/%m/%Y")
      lbl.config(text=string)
      lbl.after(1000, time)

  lbl =Label(p,font="times 17 bold")
  lbl.place(x=1110,y=40)
  time()



 def student(self):
  self.new_window=Toplevel(self.root1)
  self.app =Student(self.new_window)

 def room(self):
  self.new_window=Toplevel(self.root1)
  self.app =Roomallocation(self.new_window)


 def addroom(self):
  self.new_window=Toplevel(self.root1)
  self.app =Addroom(self.new_window)

 def emp(self):
  self.new_window=Toplevel(self.root1)
  self.app =Emp(self.new_window)

 def dest(self):
     self.root1.destroy()

 def Mess(self):
       self.new_window = Toplevel(self.root1)
       self.app = Mess(self.new_window)
 def report(self):
       self.new_window = Toplevel(self.root1)
       self.app = report(self.new_window)
 def logout(self):
  self.root1.destroy()


if __name__ == "__main__":
  root1 = Tk()
  obj = Warden(root1)



  root1.mainloop()