#!/usr/bin/env python
# coding: utf-8

'''
Calculations for: NASA Space Math 10Page113.pdf - Problem 2
PDF Document: https://spacemath.gsfc.nasa.gov/Calculus/10Page113.pdf
'''

from qmul import *
from qintegral import *

m = sympy.Symbol('m')
RawEqParts = [0.025*m**-0.9]

Eqn_Integrated = qintegrals(m, RawEqParts)

print(Eqn_Integrated)