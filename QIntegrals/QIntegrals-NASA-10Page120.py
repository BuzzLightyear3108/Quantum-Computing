#!/usr/bin/env python
# coding: utf-8

'''
Calculations for: NASA Space Math 10Page120.pdf - Problem 2
PDF Document: https://spacemath.gsfc.nasa.gov/Calculus/10Page120.pdf
'''

from qmul import *
from qintegral import *

T = sympy.Symbol('T')
RawEqParts = [sympy.Mul(49), 42*T, 9*T**2]

Eqn_Integrated = qintegrals(T, RawEqParts)

print(Eqn_Integrated)