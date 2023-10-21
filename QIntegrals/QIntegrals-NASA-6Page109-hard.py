#!/usr/bin/env python
# coding: utf-8

'''
Calculations for: NASA Space Math 6Page109.pdf - Problem 4
PDF Document: https://spacemath.gsfc.nasa.gov/Calculus/6Page109.pdf
'''

from qmul import *

m = sympy.Symbol('m')

RawEqParts = []
Eqn_Integrated = []

factorsSet = []

for RawEqPart in RawEqParts:
	coeffExp = RawEqPart.as_coeff_exponent(m)
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

	factorsSet.append(factors)

	for A, B in factors:
		# Set the Inputs by using setInputs()
		setInputs(A, B)
		
		# Execute the Circuit by using execCirc()
		resultMul = execCirc()
		result.append(resultMul)
		#print(f'Expression: {A}*{B} = {resultMul}')

	# New Coefficient for the integrated expression
	integCoef = Fraction(result[0], result[1])

	# New Exponent for the integrated expression
	# Add by a value equal to the denominator of the 2nd/Divisor Fraction (e.g. if denominator=2, then 2/2=1, so add by two)
	integExp = coeffExpFrac[1][0]+denominator
	integExp /= denominator

	Eqn_Integrated.append(integCoef*m**integExp)

print(Eqn_Integrated)
