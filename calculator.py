from tkinter import *
root=Tk()
root.geometry("400x400")
root.resizable(FALSE,FALSE)
root.title("Calculator")
root.iconbitmap("475497.ico")
root.configure(bg="black")

equation=""
def clear():
    global equation
    equation=""
    input.config(text=equation)
def show(value):
    global equation
    equation+=value
    input.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    input.config(text=result)
def delete():
    global equation
    if equation!="":
        equation=equation[0:len(equation)-1]
        
    else:
        equation=""
    input.config(text=equation)



input=Label(root,width=250,height=3,text="")
input.pack(padx=60,pady=35)

Button(root,text="C",bg="orange",fg="white",padx=31,pady=10,command=lambda: clear()).place(x=60,y=90)
Button(root,text="/",bg="black",fg="white",padx=31,pady=10,command=lambda: show('/')).place(x=131,y=90)
Button(root,text="*",bg="black",fg="white",padx=31,pady=10,command=lambda: show('*')).place(x=198,y=90)
Button(root,text="x",bg="orange",fg="white",padx=31,pady=10,command=lambda: delete()).place(x=265,y=90)

Button(root,text="7",bg="black",fg="white",padx=31,pady=10,command=lambda: show('7')).place(x=60,y=135)
Button(root,text="8",bg="black",fg="white",padx=31,pady=10,command=lambda: show('8')).place(x=131,y=135)
Button(root,text="9",bg="black",fg="white",padx=31,pady=10,command=lambda: show('9')).place(x=198,y=135)
Button(root,text="-",bg="black",fg="white",padx=31,pady=10,command=lambda: show('-')).place(x=265,y=135)

Button(root,text="4",bg="black",fg="white",padx=31,pady=10,command=lambda: show('4')).place(x=60,y=180)
Button(root,text="5",bg="black",fg="white",padx=31,pady=10,command=lambda: show('5')).place(x=131,y=180)
Button(root,text="6",bg="black",fg="white",padx=31,pady=10,command=lambda: show('6')).place(x=198,y=180)
Button(root,text="+",bg="black",fg="white",padx=29,pady=10,command=lambda: show('+')).place(x=265,y=180)

Button(root,text="1",bg="black",fg="white",padx=31,pady=10,command=lambda: show('1')).place(x=60,y=225)
Button(root,text="2",bg="black",fg="white",padx=31,pady=10,command=lambda: show('2')).place(x=131,y=225)
Button(root,text="3",bg="black",fg="white",padx=31,pady=10,command=lambda: show('3')).place(x=198,y=225)
Button(root,text="=",bg="orange",fg="white",padx=29,pady=32,command=lambda: calculate()).place(x=265,y=225)

Button(root,text="%",bg="black",fg="white",padx=31,pady=10,command=lambda: show('%')).place(x=60,y=270)
Button(root,text="0",bg="black",fg="white",padx=31,pady=10,command=lambda: show('0')).place(x=131,y=270)
Button(root,text=".",bg="black",fg="white",padx=27,pady=10,command=lambda: show('.')).place(x=198,y=270)

root.mainloop()