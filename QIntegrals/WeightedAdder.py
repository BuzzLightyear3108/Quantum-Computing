from qiskit import QuantumCircuit, Aer, execute, transpile, execute, IBMQ
from qiskit_aer import AerSimulator

from qiskit.tools.monitor import job_monitor
from qiskit.circuit.library import WeightedAdder

from qiskit.circuit import Instruction, CircuitInstruction, Qubit, QuantumRegister, Clbit, ClassicalRegister
from qiskit.circuit.library.standard_gates import IGate, XGate, CXGate, CCXGate, C3XGate, C4XGate, MCXGate, \
                                                  RXGate, RYGate, RZGate, HGate
from qiskit.exceptions import QiskitError

import matplotlib.pyplot as plt
%matplotlib inline
from qiskit.visualization import plot_histogram

import os
import sys
import math as m
import numpy as np
import pandas as pd
import sympy

from _functools import *
from traceback import format_exc

from qmul import setInputs, initGates

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

    # for count in list(counts):
        # print(int(count, 2))

