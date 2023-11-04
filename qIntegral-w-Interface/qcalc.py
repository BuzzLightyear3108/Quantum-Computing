from tkinter import *
import os
import ctypes
import threading

from sympy.parsing.sympy_parser import parse_expr

from qintegral import *

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def evaluate(event):
    # After 1 ms call `evaluate`
    # That is to make sure that tkinter has handled the keyboard press
    window.after(1, evaluateRaw)

def evaluateRaw():
    try:
        EqnsList1 = EqnsText.get(1.0, 'end').split('\n')
        EqnsList2 = [sympy.parsing.sympy_parser.parse_expr(el1) for el1 in EqnsList1 if el1 != '']
        EqnsList3 = [sympy.Add.make_args(el2) for el2 in EqnsList2]
        EqnsList4 = [qintegrals(el3, window) for el3 in EqnsList3]
        EqnsList5 = [[el4Expr.as_coeff_exponent(extractVarFromExpr(el4Expr)[0])+(extractVarFromExpr(el4Expr)[0],) for el4Expr in el4] for el4 in EqnsList4]; ErrMsgText.insert('end', str(EqnsList5))
        EqnsList6 = [[sympy.Mul(sympy.UnevaluatedExpr(el5Expr[0]), sympy.UnevaluatedExpr(sympy.Pow(el5Expr[2], el5Expr[1]))) for el5Expr in el5] for el5 in EqnsList5]
        EqnsList7 = [str(sum(el6)+sympy.UnevaluatedExpr(sympy.Symbol('C'))) for el6 in EqnsList6]
        
        result = '\n\n'.join(EqnsList7)
        IntEqnsText.delete('1.0', 'end')
        IntEqnsText.insert('end', result)
        
        ErrMsgText.delete('1.0', 'end')
    
    except:
        if ErrMsgText.get('1.0', 'end') != '\n':
            ErrMsgText.insert('end', '\n\n')
        
        ErrMsgText.insert('end', format_exc())

window = Tk()

window.title('Quantum Integral Calculator')  # title of the GUI window
window.geometry('968x856+175+80')  # specify the max size the window can expand to
window.resizable(False, False)
window.config(bg='skyblue')  # specify background color

# Create left and right frames
left_frame = Frame(window, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(window, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

bottom_frame = Frame(window, width=650, height=400, bg='grey')
bottom_frame.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

# Create title for Original Equations
Label(left_frame, text="Equations:", font=('Arial', 20)).grid(row=0, column=0, padx=5, pady=5)

# Textbox for Original Equations in left_frame
EqnsText = Text(left_frame, width=30, height=10, font=('Arial', 16))
EqnsText.grid(row=2, column=0, padx=5, pady=5)

# Create title for Integrated Equations
Label(right_frame, text="Integrated Equations:", font=('Arial', 20)).grid(row=0, column=1, padx=5, pady=5)

# Textbox for Integrated Equations in right_frame
IntEqnsText = Text(right_frame, width=30, height=10, font=('Arial', 16))
IntEqnsText.grid(row=2, column=1, padx=5, pady=5)

# Create title for Error Message Display
Label(bottom_frame, text="Error Message Display (in case there are errors)", font=('Arial', 20)).grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# Textbox for Display Error Messages in right_frame
ErrMsgText = Text(bottom_frame, width=100, height=20, font=('Arial', 10))
ErrMsgText.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

# Create Key Event so when EqnsText is given input, IntEqnsText is already updated
EqnsText.bind('<Key>', evaluate)

# window.mainloop()