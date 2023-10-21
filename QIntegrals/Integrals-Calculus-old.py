#!/usr/bin/env python
# coding: utf-8

from qmul import *

x = sympy.Symbol('x')

# Time in Hours
T = [0, 0.5, 1.2, 2.3, 3.7, 5.3, 6.7, 7.8, 8.5]

# Rate of radiation dose rates into an unshielded silicon material
G = [0.08, 0.23, 1.5, 2.4, 2.4, 2.4, 2.4, 1.6, 0.19]

# Slope of G(T) function
G_Slopes = [(G2-G1)/(T2-T1) for G2, G1, T2, T1 in zip(G[1:], G[:-1], T[1:], T[:-1])]

# T Intervals
T_Intervals = [(T1,T2) for T2, T1 in zip(T[1:], T[:-1])]

# y-intercept of G(T) function
G_y_intercept = [G1-G_Slope*T1 for G1, G_Slope, T1 in zip(G[:-1], T[:-1], G_Slopes)]

x = sympy.Symbol('x')

# G(T) piecewise functions
G_eq_BeforeInt = [Fraction(str(m)).limit_denominator()*x+b for m, b in zip(G_Slopes, G_y_intercept)]

# Integrate the equations separately between Slopes and Y Intercepts
# Rule: ∫(f(x) + g(x))dx = ∫f(x)dx + ∫g(x)dx

G_Slopes_BeforeInt = [Fraction(str(m)).limit_denominator()*x for m in G_Slopes]
G_b_BeforeInt = [b for b in G_y_intercept]

G_Slopes_AfterInt = []
G_b_AfterInt = [b*x for b in G_b_BeforeInt] # Rule: ∫ C * dx = Cx

factorsSet = []

for G_Slopes_RawEq in G_Slopes_BeforeInt:
	coeffExp = G_Slopes_RawEq.as_coeff_exponent(x)
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
	integExp = coeffExpFrac[1][0]+1

	G_Slopes_AfterInt.append(integCoef*x**integExp)

# Rule: ∫(f(x) + g(x))dx = ∫f(x)dx + ∫g(x)dx
G_Integrated_eqns = [G_Slopes_Part+G_y_intercept_Part for G_Slopes_Part, G_y_intercept_Part in zip(G_Slopes_AfterInt, G_b_AfterInt)]

# Lambdify the Integrated G(T) Functions
G_Int_Funcs = [sympy.lambdify(x, G_Integrated) for G_Integrated in G_Integrated_eqns]

# Areas between curves within T_Intervals calculated
G_Areas = [G_Int_Func(T_Interval[1])-G_Int_Func(T_Interval[0]) for T_Interval, G_Int_Func in zip(T_Intervals, G_Int_Funcs)]

# Areas summed
G_Sum_Area = sum(G_Areas)