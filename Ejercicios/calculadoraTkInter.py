from tkinter import *

operator= ''
n1=0
def operation(op):
    global n1
    global operator
    n1= float(textbox.get())
    operator= op
    textbox.delete (0, END)

def add():
    operation('+')

def minus():
    operation('-')

def times():
    operation('*')

def divide():
    operation('/')

def clear ():
    textbox.delete(0,END)

def evaluate ():
    n2= float(textbox.get())

    textbox.delete(0,END)

    if operator== '+':
        textbox.insert(END,n1 + n2)
    elif operator== '*':
        textbox.insert(END,n1 * n2)
    elif operator== '/':
        textbox.insert(END,n1 / n2)
    elif operator== '-':
        textbox.insert(END,n1 - n2)
    else:
        textbox.insert(END, 'Error')
    
#Crea la ventana principal 
ventana = Tk()
ventana.title('CALCULADORA')

textbox = Entry(ventana, width=20)
textbox.grid(row=0, column=0, columnspan=3)

button_add= Button(ventana, text='+', width=3, command=add)
button_add.grid(row=2, column=0)
button_minus= Button(ventana, text='-', width=3, command=minus)
button_minus.grid(row=2, column=1)
button_multiply= Button(ventana, text='*', width=3, command=times)
button_multiply.grid(row=3, column=0)
button_divide= Button(ventana, text='/', width=3, command=divide)
button_divide.grid(row=3, column=1)
button_equals= Button(ventana, text='=', width=6, command=evaluate)
button_equals.grid(row=4, column=0, columnspan=2)
button_clear= Button(ventana, text='CLEAR', width=6, command=clear)
button_clear.grid(row=4, column=2, sticky=E)

ventana.mainloop()