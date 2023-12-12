from tkinter import *
import math
root=Tk()
root.geometry("380x400")
root.title("claculator")

def click(num):
    global expression
    expression=expression+str(num)   
    screen.set(expression)
    

def root_func():
    global expression
    try:
        res=eval(expression)
        ans=math.sqrt(res)
        screen.set(ans)
        print(ans)
    except:
        screen.set("Error")        
    
def clear():   
    global expression
    expression=""
    screen.set(expression)
    
def result():
    global expression
    try:
        res=eval(expression)
        screen.set(res)
        print(res)
    except:
        screen.set("Error")
        
              
expression=""

f1=Frame(root)
f1.grid()
    
screen=IntVar()
screen.set("")
screen_entry=Entry(f1,textvariable=screen,bd=6,bg="#6CD300",font="Helvetica 20 bold",background="skyblue",relief=SUNKEN)
screen_entry.grid(padx=20)
      
f2=Frame(root)
f2.grid()

b1=Button(f2,text="0",padx=20,pady=10,command=lambda:click("0"),font="Helvetica 15 bold").grid(row=6,column=0)
b2=Button(f2,text="1",padx=20,pady=10,command=lambda:click("1"),font="Helvetica 15 bold").grid(row=5,column=0)
b3=Button(f2,text="2",padx=20,pady=10,command=lambda:click("2"),font="Helvetica 15 bold").grid(row=5,column=1)
b4=Button(f2,text="3",padx=20,pady=10,command=lambda:click("3"),font="Helvetica 15 bold").grid(row=5,column=2)
b5=Button(f2,text="4",padx=20,pady=10,command=lambda:click("4"),font="Helvetica 15 bold").grid(row=4,column=0)
b6=Button(f2,text="5",padx=20,pady=10,command=lambda:click("5"),font="Helvetica 15 bold").grid(row=4,column=1)
b7=Button(f2,text="6",padx=20,pady=10,command=lambda:click("6"),font="Helvetica 15 bold").grid(row=4,column=2)
b8=Button(f2,text="7",padx=20,pady=10,command=lambda:click("7"),font="Helvetica 15 bold").grid(row=3,column=0)
b9=Button(f2,text="8",padx=20,pady=10,command=lambda:click("8"),font="Helvetica 15 bold").grid(row=3,column=1)
b10=Button(f2,text="9",padx=20,pady=10,command=lambda:click("9"),font="Helvetica 15 bold").grid(row=3,column=2)
b11=Button(f2,text="+",padx=20,pady=10,command=lambda:click("+"),font="Helvetica 15 bold").grid(row=2,column=3)
b12=Button(f2,text="-",padx=20,pady=10,command=lambda:click("-"),font="Helvetica 15 bold").grid(row=2,column=1)
b13=Button(f2,text="*",padx=20,pady=10,command=lambda:click("*"),font="Helvetica 15 bold").grid(row=2,column=2)
b14=Button(f2,text="/",padx=20,pady=10,command=lambda:click("/"),font="Helvetica 15 bold").grid(row=5,column=3)
b15=Button(f2,text=".",padx=20,pady=10,command=lambda:click("."),font="Helvetica 15 bold").grid(row=6,column=1)
b16=Button(f2,text="00",padx=15,pady=10,command=lambda:click("00"),font="Helvetica 15 bold").grid(row=6,column=2)
b17=Button(f2,text="=",padx=20,pady=10,command=result,font="Helvetica 15 bold").grid(row=6,column=3)
b18=Button(f2,text="c",padx=20,pady=10,command=clear,font="Helvetica 15 bold").grid(row=2,column=0)
b19=Button(f2,text="root",padx=8,pady=10,command=root_func,font="Helvetica 15 bold").grid(row=3,column=3)
photo=PhotoImage(file="py.png")
photosize=photo.subsample(4,4)
b20=Button(f2,image=photosize,padx=1,pady=5,font="Helvetica 15 bold").grid(row=4,column=3)

root.mainloop()