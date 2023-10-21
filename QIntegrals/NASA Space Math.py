#!/usr/bin/env python
# coding: utf-8

# <div style="font-size:225%; font-weight:bold; text-align: center; margin-bottom: 20px">NASA Space Math</div>
# <div style="font-size:175%; font-weight:bold; text-align: center">Using Quantum Algorithms Simulator to solve Integrals</div>

# In[1]:


from qiskit import QuantumCircuit, Aer, execute, transpile, execute, IBMQ
from qiskit_aer import AerSimulator

from qiskit.tools.monitor import job_monitor
from qiskit.circuit.library import WeightedAdder

from qiskit.circuit import Instruction, CircuitInstruction, Qubit, QuantumRegister, Clbit, ClassicalRegister
from qiskit.circuit.library.standard_gates import IGate, XGate, CXGate, CCXGate, C3XGate, C4XGate, MCXGate, \
                                                  RXGate, RYGate, RZGate, HGate
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


# In[2]:


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


# In[3]:


def qAdd(weights, backend=AerSimulator(method='matrix_product_state')):
    aCirc1 = WeightedAdder(num_state_qubits=len(weights), weights=weights)

    nQubits = aCirc1.num_qubits
    qubits = aCirc1.qubits

    sumQubitIndices = [qubitIndex for qubitIndex in range(len(qubits)) if "'sum'" in str(qubits[qubitIndex])]
    nInputs = str(qubits).count("'state'")
    nOutputs = len(sumQubitIndices)

    q = QuantumRegister(nQubits, 'q')
    c = ClassicalRegister(nOutputs, 'c')

    aCirc = QuantumCircuit(q, c)

    initGates(aCirc, q, nInputs, gateName='x')

    aCirc.append(aCirc1, range(nQubits))
    aCirc.measure(sumQubitIndices, range(nOutputs))

    job = execute(aCirc, backend, shots=2000)
    result = job.result()
    counts = result.get_counts()
    count = list(counts)[0]

    return int(count, 2)


# In[4]:


def qintegrals(var, RawEqParts, debugPrint=False):
    Eqn_Integrated = []
    if debugPrint: factorsSet = []
    
    for RawEqPart in RawEqParts:
        coeffExp = RawEqPart.as_coeff_exponent(var)
        
        if debugPrint: print(coeffExp)
        
        coeffExpFrac = [Fraction(str(eqNum)).limit_denominator().as_integer_ratio() for eqNum in coeffExp]

        # # Add 1 due to integration
        # Add by a value equal to the denominator of the 2nd/Divisor Fraction (e.g. if denominator=2, then 2/2=1, so add by two)

        factors = np.transpose(coeffExpFrac)
        denominator = factors[1, 1]

        # factors[:, 1][0] is the Numerator of the 2nd Fraction
        factors[:, 1][0] += denominator

        # # Fraction division is a multiplication by its reciprocal of the 2nd/Divisor Fraction
        factors[:, 1] = factors[:, 1][::-1]
        result = []

        if debugPrint: factorsSet.append(factors)

        for A, B in factors:
            # Using Repeated Addition through WeightedAdder
            resultMul = qAdd([A]*B)
            result.append(resultMul)

        # New Coefficient for the integrated expression
        integCoef = Fraction(result[0], result[1])

        # New Exponent for the integrated expression
        # Add by a value equal to the denominator of the 2nd/Divisor Fraction (e.g. if denominator=2, then 2/2=1, so add by two)
        integExp = coeffExpFrac[1][0]+denominator
        integExp /= denominator

        Eqn_Integrated.append(integCoef*var**integExp)
        
        if debugPrint: print(factorsSet)
        
    return Eqn_Integrated


# Calculations for: NASA Space Math 10Page120.pdf - Problem 2
#     
# PDF Document: https://spacemath.gsfc.nasa.gov/Calculus/10Page120.pdf

# In[5]:


T = sympy.Symbol('T')
RawEqParts = [sympy.Mul(49), 42*T, 9*T**2]

Eqn_Integrated = qintegrals(T, RawEqParts)

print(Eqn_Integrated)


# Calculations for: NASA Space Math 7Page48.pdf - Problem 1B
# 
# PDF Document: https://spacemath.gsfc.nasa.gov/Calculus/7Page48.pdf

# In[6]:


T = sympy.Symbol('T')
RawEqParts = [float(coef)*T**exp for coef, exp in zip('1.49 12.30 41.94 76.00 77.55 42.28 9.46 0.18 0.0009'.split(), range(8, -1, -1))]

Eqn_Integrated = qintegrals(T, RawEqParts)

print(Eqn_Integrated)


# Calculations for: NASA Space Math 10Page113.pdf - Problem 2
# 
# PDF Document: https://spacemath.gsfc.nasa.gov/Calculus/10Page113.pdf

# In[7]:


m = sympy.Symbol('m')
RawEqParts = [0.025*m**-0.9]

Eqn_Integrated = qintegrals(m, RawEqParts)

print(Eqn_Integrated)

