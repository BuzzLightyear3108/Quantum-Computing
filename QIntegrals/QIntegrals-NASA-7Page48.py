#!/usr/bin/env python
# coding: utf-8

'''
Calculations for: NASA Space Math 7Page48.pdf - Problem 1B
PDF Document: https://spacemath.gsfc.nasa.gov/Calculus/7Page48.pdf
'''

from qmul import *
from qintegral import *

T = sympy.Symbol('T')
RawEqParts = [float(coef)*T**exp for coef, exp in zip('1.49 12.30 41.94 76.00 77.55 42.28 9.46 0.18 0.0009'.split(), range(8, -1, -1))]

Eqn_Integrated = qintegrals(T, RawEqParts)

print(Eqn_Integrated)