from tkinter import *
'''
root =Tk()
frame=Frame(root,bg='red')
frame.pack()
rb=Button(frame,text='hello world',fg='red')
rb.pack(side=LEFT)
bb=Button(frame,text='exit',fg='brown',command=quit)
bb.pack(side=LEFT)
root.mainloop()
'''
def click():
    input.insert(0)

root =Tk()
frame=Frame(root,bg='red')
frame.pack()
rb=Button(frame,text='hello world',fg='red')
rb.pack(side=LEFT)
bb=Button(frame,text='press',fg='brown',command=click ).place(x=10,y=40)
bb.pack(side=LEFT)
root.mainloop()
