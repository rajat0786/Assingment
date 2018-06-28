#ASSINMENT 17


#Q1
from tkinter import *

root =Tk()
frame=Frame(root,bg='red')
frame.pack()
rb=Button(frame,text='hello world',fg='red')
rb.pack(side=LEFT)
bb=Button(frame,text='exit',fg='brown',command=quit)
bb.pack(side=LEFT)
root.mainloop()


#Q2


root =Tk()
frame=Frame(root,bg='red')
frame.pack()
rb=Button(frame,text='hello world',fg='red')
rb.pack(side=LEFT)
def click():
    lb1.config(text="press after clicked")
bb=Button(frame,text='exit',fg='brown',command=quit )
bb.pack(side=LEFT)
db=Button(frame,text='press',fg='brown',command=click)
db.pack(side=LEFT)
lb1=Label(root,text='')
lb1.pack()
root.mainloop()



#Q3



root =Tk()
frame=Frame(root,bg='red')
frame.pack()
def click():
    lb1.config(text="press after clicked")
bb=Button(frame,text='exit',fg='brown',command=quit )
bb.pack(side=LEFT)
db=Button(frame,text='press',fg='brown',command=click)
db.pack(side=LEFT)
lb1=Label(root,text='preee before clicked')
lb1.pack()
root.mainloop()



#Q4

from tkinter import *
root = Tk()
frame=Frame(root,bg='white')
frame.pack()
Label(frame, text="First Name").grid(row=0)
Label(frame, text="Last Name").grid(row=1)

e1 = Entry(frame)
e2 = Entry(frame)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def cal():
  a = e1.get()
  b = e2.get()
  lb1 = Label(frame, text=a+b)
  lb1.grid(row=2, column=1)
  lb1.config(text=a+b)
lb1 = Label(frame, text="")
lb1.grid(row=2, column=1)

bb = Button(frame, text='exit', fg='brown', command=quit)
bb.grid(row=3,column=1)
db = Button(frame, text='press', fg='brown', command=cal)
db.grid(row=4,column=1)


mainloop( )

