from tkinter import *

window= Tk()
window.geometry("300x300")
window.title("Simple Calculator")

lab1=Label(window,text="Enter 1st integer:")
lab1.place(x=50,y=50)

lab2=Label(window,text="Enter 2nd integer: ")
lab2.place(x=50,y=100)

lab3=Label(window,text="Result: ")
lab3.place(x=50,y=150)

t1=Entry()
t1.place(x=170,y=50)

t2=Entry()
t2.place(x=170,y=100)

t3=Entry()
t3.place(x=170,y=150)



def add():
  num1=int(t1.get())
  num2=int(t2.get())
  sum=num1 + num2
  t1.insert(END,str(sum))

b1=Button(window, text="Add",command=add)
b1.place(x=50,y=200)

def sub():
  num1=int(t1.get())
  num2=int(t2.get())
  sub=num1 - num2
  t2.insert(END,str(sub))

b2=Button(window, text="Subract",command=sub)
b2.place(x=100,y=200)

def mul():
  num1=int(t1.get())
  num2=int(t2.get())
  pro=num1 * num2
  t3.insert(END,str(pro))

b3=Button(window, text="Multi",command=mul)
b3.place(x=150,y=200)

def div():
  num1=int(t1.get())
  num2=int(t2.get())
  quo=num1 / num2
  t3.insert(END,str(quo))

b4=Button(window, text="Divide",command=div)
b4.place(x=200,y=200)

def clear():
  t1.delete(0,END)
  t2.delete(0,END)
  t3.delete(0,END)
b5=Button(window, text="Clear",command=clear)
b5.place(x=130,y=250)










