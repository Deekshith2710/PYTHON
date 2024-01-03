from tkinter import *


root=Tk()

#it sets the root window fixed by the use of  maxsize() and minsize() 
#root.minsize(width=900,height=400)

#root.maxsize(width=900,height=400)

#this fucntion called whenever we click numeric buttons
def click(number):
         a=e1.get()
         e1.delete(0,END)
         e1.insert(0,str(a)+str(number))

#this fucntion called whenever we click button'='
def clear():
         e1.delete(0,END)

         
# this fucntion  called whenever we click the button '+'
def add():
         f=e1.get()
         global f1
         global math
         math='addition'
         f1=int(f)
         e1.delete(0,END)

def equal():
         s=e1.get()
         e1.delete(0,END)

         if math=='addition':
                  
                  e1.insert(0, f1 + int(s))

         if math=='minus':
                  e1.insert(0, f1-int(s))

         if math=='multiplication':
                  e1.insert(0, f1*int(s))

         if math=='division':
                  e1.insert(0, f1/int(s))

def minus():
         
         f=e1.get()
         global f1
         global math
         math='minus'
         f1=int(f)
         e1.delete(0,END)

def mul():
         
         f=e1.get()
         global f1
         global math
         math='multiplication'
         f1=int(f)
         e1.delete(0,END)

def div():

         f=e1.get()
         global f1
         global math
         math='division'
         f1=int(f)
         e1.delete(0,END)


         

         

         
e1=Entry(root,width=120,borderwidth=5)
e1.grid(row=0,column=0,padx=10,columnspan=3)

#to give the title name for the widget

root.title('Simple Calculator')

b1=Button(root,text='1',command=lambda:click(1),width=40,height=2).grid(row=3 ,column=0)
b2=Button(root,text='2',command=lambda:click(2),width=40,height=2).grid(row=3 ,column=1)
b3=Button(root,text='3',command=lambda:click(3),width=40,height=2).grid(row=3 ,column=2)

b4=Button(root,text='4',command=lambda:click(4),width=40,height=2).grid(row=2 ,column=0)
b5=Button(root,text='5',command=lambda:click(5),width=40,height=2).grid(row=2 ,column=1)
b6=Button(root,text='6',command=lambda:click(6),width=40,height=2).grid(row=2 ,column=2)

b7=Button(root,text='7',command=lambda:click(7),width=40,height=2).grid(row=1 ,column=0)
b8=Button(root,text='8',command=lambda:click(8),width=40,height=2).grid(row=1 ,column=1)
b9=Button(root,text='9',command=lambda:click(9),width=40,height=2).grid(row=1 ,column=2)

b0=Button(root,text='0',command=lambda:click(0),width=40,height=2).grid(row=4 ,column=0)


b_add=Button(root,text='+',command=add,width=40,height=2).grid(row=5,column=0)

b_equal=Button(root,text='=',command=equal,width=82,height=2).grid(row=5,column=1,columnspan=2)

b_mul=Button(root,text='*',command=mul,width=40,height=2).grid(row=6,column=1)

b_minus=Button(root,text='-',command=minus,width=40,height=2).grid(row=6,column=0)


b_clear=Button(root,text='clear',command=clear,width=82,height=2).grid(row=4,column=1,columnspan=2)


b_div=Button(root,text='/',command=div,width=40,height=2).grid(row=6,column=2)















root.mainloop()
