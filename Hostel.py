
import time
from datetime import datetime
from tkinter import *
from PIL import ImageTk,Image
from time import strftime
import pytz
from tkinter import ttk, messagebox
import  os
from adminlog import Admin




class Hostel:

 def __init__(self, root5):
  self.var_accno2=StringVar()
  self.var_pin2=StringVar()
  self.root5 =root5
  self.root5.geometry("1530x790+0+0")
  self.root5.iconbitmap('E:\python\Hostel Management Software\images\icon.ico')
  self.root5.title("HOSTEL MANAGEMENT SOFTWARE")
  l = Label(self.root5, bd=20, relief=RIDGE, text="HOSTEL MANAGEMENT SOFTWARE", fg='GREEN', bg='black',
            font=("times new roman", 50, 'bold', 'underline'))
  l.pack(side=TOP, fill=X)
  l = Label(self.root5, bd=10, relief=RIDGE, text=" ADMIN LOGIN ", fg='red', bg='black',
            font=("times new roman", 20, 'bold'))
  l.pack(side=TOP, fill=X)
  f1 = Frame(self.root5, bd=15, relief=RIDGE, bg='black')
  f1.place(x=0, y=170, width=1528, height=618)
  l12 = Label(root5, text='Copyright @DIPTISH-WORLD 2022', font='15', fg='White', bg='black').place(x=650, y=745)
  mainframe = Frame(f1, bd=2)
  mainframe.place(x=10, y=10, width=1480, height=550)
  hii=r"E:\python\Hostel Management Software\images\admin.jpeg"
  img = Image.open(hii)
  img = img.resize((1530, 530), Image.ANTIALIAS)
  self.photo = ImageTk.PhotoImage(img)
  p = Label(mainframe, image=self.photo)
  p.place(x=15, y=5, width=1450, height=530)
  f2 = Frame(mainframe, bd=5, relief=RIDGE, bg='BLACK')
  f2.place(x=200, y=55, width=315, height=450)
  l = Label(f2, bd=3, relief=RIDGE, text=" ADMIN ", fg='black', bg='WHITE',font=('times ', 20, 'bold'))
  l.pack(side=TOP, fill=X)
  b = Button(f2, text='Login', font="Times 20  bold", bg='GREEN', fg='black', width=6, height=1,command=lambda :self.verify()  ).place(x=98, y=275)
  b1 = Button(f2, text='back', font="Times 15  bold", bg='silver', fg='black', width=3,command=self.dest).place(x=250, y=380)
  Label(f2,text='USERNAME',font="Times 15  bold underline",bg='BLACK',fg='white').place(x=75,y=70)
  ttk.Entry(f2,width=22,font=("times new roman", 12, 'bold'),textvariable=self.var_accno2).place(x=60,y=110)
  Label(f2,text='PASSWORD',font="Times 15  bold underline",bg='BLACK',fg='white').place(x=75,y=150)
  ttk.Entry(f2,width=22,font=("times new roman", 12, 'bold'),textvariable=self.var_pin2,show='*').place(x=60,y=180)
  def time():
      string = strftime("%H:%M:%S %p \n %d/%m/%Y")
      lbl.config(text=string)
      lbl.after(1000, time)

  lbl =Label(p,font="times 17 bold")
  lbl.place(x=0,y=0)
  time()






 def dest(self):
     self.root5.destroy()


 def verify(self):
     accountno=self.var_accno2.get()
     pin=self.var_pin2.get()


     if accountno == "Diptish":

      if pin == "2213535":
       messagebox.showinfo('SUCCESS',"ACCESS GRANTED SUCCESS",parent=self.root5)
       #self.root5.destroy()
       self.var_accno2=""
       self.var_pin2=""
       self.Admin1()

      else:
       messagebox.showinfo('ERROR!!! NOT FOUND ',"PASSWORD IS WRONG",parent=self.root5)
     else:
       messagebox.showinfo('ERROR!!! USER NOT FOUND '," USERNAME NOT FOUND",parent=self.root5)

 def Admin1(self):
   self.new_window = Toplevel(self.root5)
   self.app = Admin(self.new_window)



if __name__ == "__main__":
  root5 = Tk()
  obj = Hostel(root5)



  root5.mainloop()