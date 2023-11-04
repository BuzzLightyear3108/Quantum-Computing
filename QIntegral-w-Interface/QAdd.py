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


def QAdd(addends):
    '''
    The quantum circuit is in the addition parts.
    It uses a type of qiskit circuit called WeightedAdder.
    
    Here is a documentation:
    https://qiskit.org/documentation/stubs/qiskit.circuit.library.WeightedAdder.html
    
    Suppose there are two factors, a = 168 and b = 185
    During multiplication, a and b are going to be broken up into additions to be process using long multiplication algorithm, like this:
    a = 100+60+8
    b = 100+80+5
    
    a*b = 168*185
        = (100+60+8)*(100+80+5)
        = 10000+8000+500+6000+4800+300+800+640+40 = 31080
    '''
    
    weights = addends
    
    aCirc1 = WeightedAdder(num_state_qubits=len(weights), weights=weights)
    aCirc1.num_qubits
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
    
    backend = AerSimulator(method='matrix_product_state')
    job = execute(aCirc, backend, shots=2000)
    result = job.result()
    counts = result.get_counts()
    
    return int(list(counts)[0], 2)
    
    