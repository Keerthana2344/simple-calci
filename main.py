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


