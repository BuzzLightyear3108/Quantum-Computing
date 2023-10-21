#!/usr/bin/env python
# coding: utf-8

'''Subtractions of Numbers using Quantum Circuits'''

from qiskit import QuantumCircuit, Aer, execute, transpile, execute, IBMQ
from qiskit_aer import AerSimulator

from qiskit.tools.monitor import job_monitor
from qiskit.circuit.library import WeightedAdder

from qiskit.circuit import Instruction, CircuitInstruction, Qubit, QuantumRegister, Clbit, ClassicalRegister
from qiskit.circuit.library.standard_gates import IGate, XGate, CXGate, CCXGate, C3XGate, C4XGate, MCXGate, \
                                                  RXGate, RYGate, RZGate, HGate
from qiskit.exceptions import QiskitError

import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

import os
import sys
import math as m
import numpy as np
import pandas as pd
import sympy

from _functools import *
from traceback import format_exc

backend = AerSimulator(method='matrix_product_state')

def afmtsd(the_list_original, chara, ndigits):
    '''
    afmtsd stands for "Add for making the same digits"
    This function can add some letters or numbers to the front for various purposes, including sorting purposes. For example, if one desires to sort an array ['00011', '100'], making '100' (3 digits) to become '00100' (5 digits) can make use of this function by calling afmtsd('100', '0', 5).
    '''
    
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

def setInputs(A, B, C, printResult=False):
    '''
    setInputs() function
    Convert to Excited State
    This function use X Gates to convert the ground state |0> to the excited state |1>
    (Excited state means any quantum state having energy larger than the ground state |0>.)
    '''
    
    if A > 1 or B > 1 or C > 1:
        raise OverflowError('Binary or Quantum States can only be either the ground state |0> or the excited state |1>.')
    
    sCirc.data[0].operation.name = gateNames[A]
    sCirc.data[1].operation.name = gateNames[B]
    sCirc.data[2].operation.name = gateNames[C]
    

# Create the circuit
nInputs = 3
nOutputs = 2

nQubits = 11

q = QuantumRegister(nQubits, 'q')
c = ClassicalRegister(nOutputs, 'c')

sCirc = QuantumCircuit(q, c)

def execCirc(circuit=sCirc, backend=AerSimulator(method='matrix_product_state'), shots=2000):
    '''Circuit execution function'''
    job = execute(sCirc, backend, shots=shots)
    result = job.result()
    counts = result.get_counts()
    
    return counts

initGates(circuit=sCirc, qreq=q, nInputs=nInputs, gateName='id')

# # D Part
sCirc.cx(0, 5)
sCirc.cx(1, 5)

sCirc.cx(5, 6)
sCirc.cx(2, 6)

# # Bout Part
sCirc.ccx(1, 2, 7)
sCirc.x(7)

sCirc.x(1)
sCirc.x(2)

sCirc.ccx(1, 2, 8)
sCirc.x(8)

sCirc.x(0)
sCirc.ccx(0, 8, 9)
sCirc.x(9)

sCirc.ccx(7, 9, 10)
sCirc.x(10)

sCirc.x(6)
sCirc.ccx(2, 6, 8)

sCirc.x(0)
sCirc.ccx(0, 1, 9)

sCirc.x(8)
sCirc.x(9)

sCirc.ccx(8, 9, 7)
sCirc.x(7)

sCirc.measure(6, 0)
sCirc.measure(10, 1)

# gateNames List is created due to its ability of indexing without having to use if/else condition.
# gateNames[Binary_Input_Digits] yields gateNames

# gateNames[0] yields 'id'
# gateNames[1] yields 'x'

gateNames = ['id', 'x']

if __name__ == '__main__':
    for i1 in range(2):
        sCirc.data[0].operation.name = gateNames[i1]
        
        for i2 in range(2):
            sCirc.data[1].operation.name = gateNames[i2]
            
            for i3 in range(2):
                sCirc.data[2].operation.name = gateNames[i3]
                counts = execCirc(circuit=sCirc)
                
                #print(i1, i2, i3, counts)

                for count in list(counts):
                    print(i1, i2, i3, count[::-1])
                #print(sCirc.draw())






