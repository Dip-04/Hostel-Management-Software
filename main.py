import time
from datetime import datetime
from tkinter import *
from PIL import ImageTk,Image
from time import strftime
from tkinter import ttk, messagebox
import  os
from Hostel import Hostel
from STUDENTLOGIN import Stu










class Admin:

 def __init__(self, root10):
  self.var_accno2=StringVar()
  self.var_pin2=StringVar()
  self.root10 =root10
  self.root10.geometry("1530x790+0+0")
  self.root10.iconbitmap('E:\python\Hostel Management Software\images\icon.ico')
  self.root10.title("HOSTEL MANAGEMENT SOFTWARE")
  l = Label(self.root10, bd=20, relief=RIDGE, text="HOSTEL MANAGEMENT SOFTWARE", fg='red', bg='black',
            font=("times new roman", 50, 'bold', 'underline'))
  l.pack(side=TOP, fill=X)


  f1 = Frame(self.root10, bd=15, relief=RIDGE, bg='black')
  f1.place(x=0, y=100, width=1528, height=690)
  l12 = Label(root10, text='Copyright @DIPTISH-WORLD 2022', font='15', fg='White', bg='black').place(x=650, y=745)
  mainframe = Frame(f1, bd=2)
  mainframe.place(x=10, y=10, width=1480, height=600)
  img = Image.open(r"E:\python\Hostel Management Software\images\back.jpg")
  img = img.resize((1480, 590), Image.ANTIALIAS)
  self.photo = ImageTk.PhotoImage(img)
  p = Label(mainframe, image=self.photo, bd=4, relief=RIDGE)
  p.place(x=0, y=0, width=1480, height=590)

  img1 = Image.open(r"E:\python\Hostel Management Software\images\student.png")
  img1 = img1.resize((190, 250), Image.ANTIALIAS)
  self.photo1 = ImageTk.PhotoImage(img1)
  btfram = Frame(mainframe, bd=4, relief=RIDGE,bg='black')
  btfram.place(x=250, y=160, width=200, height=260)
  Button(btfram,image=self.photo1,font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand1',command=lambda :self.stu()).place(x=0,y=0)

  img2 = Image.open(r"E:\python\Hostel Management Software\images\warden.png")
  img2 = img2.resize((190, 250), Image.ANTIALIAS)
  self.photo2 = ImageTk.PhotoImage(img2)
  btfra2 = Frame(mainframe, bd=4, relief=RIDGE,bg='black')
  btfra2.place(x=650, y=160, width=200, height=260)
  Button(btfra2,image=self.photo2,font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand1').place(x=0,y=0)

  img3 = Image.open(r"E:\python\Hostel Management Software\images\administor.png")
  img3 = img3.resize((190, 250), Image.ANTIALIAS)
  self.photo3 = ImageTk.PhotoImage(img3)
  btfra3 = Frame(mainframe, bd=4, relief=RIDGE, bg='black')
  btfra3.place(x=1050, y=160, width=200, height=260)
  Button(btfra3, image=self.photo3, font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, relief=RIDGE,
         cursor='hand1',command=lambda :self.adminstor()).place(x=0, y=0)

  def time():
      string = strftime("%H:%M:%S %p \n %d/%m/%Y")
      lbl.config(text=string)
      lbl.after(1000, time)

  lbl =Label(p,font="times 17 bold")
  lbl.place(x=1328,y=00)
  time()

 def adminstor(self):
  self.new_window=Toplevel(self.root10)
  self.app =Hostel(self.new_window)

 def stu(self):
  self.new_window=Toplevel(self.root10)
  self.app =Stu(self.new_window)


if __name__ == "__main__":
  root10 = Tk()
  obj = Admin(root10)



  root10.mainloop()