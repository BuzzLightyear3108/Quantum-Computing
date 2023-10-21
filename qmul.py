#!/usr/bin/env python
# coding: utf-8

from qiskit import QuantumCircuit, Aer, execute, transpile, execute, IBMQ
from qiskit_aer import AerSimulator

from qiskit.tools.monitor import job_monitor
from qiskit.circuit.library import RGQFTMultiplier

from qiskit.circuit import Instruction, CircuitInstruction, Qubit, QuantumRegister, Clbit, ClassicalRegister
from qiskit.circuit.library.standard_gates import IGate, XGate, CXGate, CCXGate, C3XGate, C4XGate, MCXGate
from qiskit.exceptions import QiskitError

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit.visualization import plot_histogram

import os
import sys
import math as m
import numpy as np
import pandas as pd
import sympy

from fractions import Fraction

from _functools import *
from traceback import format_exc

def afmtsd(the_list_original, chara, ndigits):
    '''afmtsd stands for "Add for making the same digits"
    This function can add some letters or numbers to the front for various purposes, including sorting purposes. For example, if one desires to sort an array ['00011', '100'], making '100' (3 digits) to become '00100' (5 digits) can make use of this function by calling afmtsd('100', '0', 5).'''
    
    the_list = list(the_list_original)
    a = [chara]*(ndigits-len(the_list)) + the_list
    
    if type(the_list_original) == type(''): return ''.join(a)
    else: return a


def initGates(circuit, qreq, nInputs, gateName='id'):
    '''Determine Input Value (Either 0 or 1)
    Initialization Gates
    First, zero it out at the beginning.
    All qubits start from ground state |0>. Create manipulable initialization gates as many as the input qubits.
    The identity gate means that it remains the same state as previous, which, in this case, the ground state |0>.
    Later, the Identity gate can be converted to an X Gate or NOT gate.'''

    circuit.data = [CircuitInstruction(operation=Instruction(name=gateName, num_qubits=1, num_clbits=0, params=[]),
                                     qubits=(Qubit(qreq, inputIndex),),
                                     clbits=()) for inputIndex in range(nInputs)]

def setInputs(A, B, printResult=False):
    '''setInputs() function
    Convert to Excited State
    This function use X Gates to convert the ground state |0> to the excited state |1>
    (Excited state means any quantum state having energy larger than the ground state |0>.)'''
    
    if A < 0:
        mCirc.data[0].operation.name = 'x'

    if B < 0:
        mCirc.data[inputDigits+1].operation.name = 'x'

    ABin, BBin = bin(abs(A))[2:], bin(abs(B))[2:]
    ABin, BBin = afmtsd(ABin, '0', inputDigits), afmtsd(BBin, '0', inputDigits)

    # Operand A
    if printResult:
        print('A in Binary Digits :', ABin, end='\n\n')

    for ADigit, AIndex in zip(ABin, range(len(ABin))[::-1]):
        ABinInput = int(ADigit)

        if ABinInput == 1: gateName = 'x'
        else: gateName = 'id'

        mCirc.data[AIndex+1].operation.name = gateName

        if printResult:
            print(AIndex+1, ADigit, gateName)

    if printResult:
        print(f'\n{"-"*100}\n')

    # Operand B
    if printResult:
        print('B in Binary Digits :', BBin, end='\n\n')

    for BDigit, BIndex in zip(BBin, range(len(BBin))[::-1]):
        BBinInput = int(BDigit)

        if BBinInput == 1: gateName = 'x'
        else: gateName = 'id'

        mCirc.data[BIndex+2+inputDigits].operation.name = gateName

        if printResult:
            print(BIndex+2+inputDigits, BDigit, gateName)


def execCirc(backend=AerSimulator(method='matrix_product_state'), shots=2000, printResult=False):
    '''execCirc() function
    Implement the Program with Combinations of Input States

    This function can execute the Circuit by using default values, which are matrix_product_state Simulator since it can implement with higher memory usage and 2000 shots. (See how it is implemented.)

    Note: Default arguments in Python can be modified.'''
    
    job = execute(mCirc, backend, shots=shots)
    result = job.result()
    counts = result.get_counts()

    # Raw Result String
    resultRaw = list(counts)[0]

    # Separating the Number from the Sign Indicator
    resultBinNum = resultRaw[-nOutput:]
    resultDecNum = int(resultBinNum, 2)

    if resultRaw[0] == '1':
        resultDecNum *= -1
        
    if printResult:
        print(f'Expression: {A}*{B}')
        print('-'*100)
        print(f'counts: {counts}')
        print(f'resultBinNum: {resultBinNum}')
        print(f'resultDecNum: {resultDecNum}')

        # Draw the Circuit
        mCirc.draw(output='mpl')
        
    return resultDecNum

inputDigits = 10

nInputs = inputDigits + inputDigits + 2
nOutput = 2*inputDigits

nQubits = nInputs+nOutput

q = QuantumRegister(nQubits,'q')
c = ClassicalRegister(nOutput+1,'c')

mCirc = QuantumCircuit(q, c)

# Determine Input Value (Either 0 or 1)
# Use initGates() function
initGates(mCirc, q, nInputs)

# RGQFTMultiplier is a QFT multiplication circuit, which is one of the most important parts of the entire Fraction Multiplication system.
# As per Qiskit documentation, the circuit itself is already containing another circuit, which is QFT circuit.
# For more information, refer to
# 1. https://qiskit.org/documentation/stubs/qiskit.circuit.library.RGQFTMultiplier.html
# 2. https://arxiv.org/pdf/1411.5949.pdf

mCirc1 = RGQFTMultiplier(num_state_qubits=inputDigits,
                         num_result_qubits=inputDigits*2)

input1Qubits = (np.arange(1, inputDigits+1)).tolist()
input2Qubits = (np.arange(1, inputDigits+1) + inputDigits+1).tolist()

inputQubits = input1Qubits + input2Qubits

outputQubits = (np.arange(0, nOutput) + (inputDigits+1)*2).tolist()

mCirc.append(mCirc1, inputQubits + outputQubits)

# Use CNOT or CX gate (Quantum XOR gate) properties to determine signs.
# There are 2 qubits that are dedicated for sign indicators only.
# "+" or positive numbers is represented by the ground state |0>.
# "-" or negative numbers is represented by the excited state |1>.

mCirc.append(CXGate(), [0, inputDigits+1])
mCirc.measure(inputDigits+1, nOutput)

# Measure Results other than Sign Indicator Parts by putting the results on a classical bit.
rangeLimit = 2**inputDigits

# Qubit Range
QRange = outputQubits

# Classical Bit Range
CRange = range(len(outputQubits))

mCirc.measure(QRange, CRange)

if __name__ == '__main__':
    # Circuit 1 (Numerator Circuit)

    # Set the Inputs by using setInputs()
    A, B = -7, -6
    setInputs(A, B)

    # Execute the Circuit by using execCirc()
    execCirc()

    # Draw the Circuit
    mCirc.draw(output='mpl')


    # Circuit 2 (Denominator Circuit)

    # Set the Inputs by using setInputs()
    A, B = -4, -5
    setInputs(A, B)

    # Execute the Circuit by using execCirc()
    execCirc()

    # Draw the Circuit
    mCirc.draw(output='mpl')
