from tkinter import *
from QMul import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()
window.title('Quantum Calculator for Basic Operations')
window.geometry('500x500+175+80')
TextStyle = ('Arial', 16)

parse_expr = sympy.parsing.sympy_parser.parse_expr

def calculate():
    try:
        result['text'] = f"\n\nResult: {eval(sympy.srepr(parse_expr(inputEntry.get(), evaluate=False)).replace('Add(', 'QAdd1(').replace('Integer(', 'int(').replace('Mul(', 'qMul_w_QAdd('))}\n\n"
        
    except:
        ErrWindow = Tk()
        ErrWindow.title('Quantum Calculator for Basic Operations')
        ErrWindow.geometry('500x500+200+125')
        ErrLabelBig = Label(ErrWindow, text=f'\n\nError!\nInvalid Expression.\n\n', font=('Arial', 25))
        ErrLabel = Label(ErrWindow, text=format_exc(), font=TextStyle)
        ErrLabelBig.pack()        
        ErrLabel.pack()        
        ErrWindow.mainloop()

instruction = Label(window, text='\n\nPlease input the expression below:')
inputEntry = Entry(window)

calculateBtn = Button(window, text='Calculate', command=calculate)
result = Label(window, text='\n\nResult goes here...\n\n')

widgets = [instruction, inputEntry, calculateBtn, result]

for widget in widgets:
    widget['font'] = TextStyle
    widget.pack()

window.bind('<Return>', lambda event: calculate())

window.mainloop()