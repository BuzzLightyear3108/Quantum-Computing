import sympy

# Time in Hours
T = [0, 0.5, 1.2, 2.3, 3.7, 5.3, 6.7, 7.8, 8.5]

# Rate of radiation dose rates into an unshielded silicon material
G = [0.08, 0.23, 1.5, 2.4, 2.4, 2.4, 2.4, 1.6, 0.19]

# Slope of G(T) function
G_Slopes = [(G2-G1)/(T2-T1) for G2, G1, T2, T1 in zip(G[1:], G[:-1], T[1:], T[:-1])]

# y-intercept of G(T) function
G_y_intercept = [G1-G_Slope*T1 for G1, G_Slope, T1 in zip(G[:-1], T[:-1], G_Slopes)]

x = sympy.Symbol('x')

# G(T) piecewise functions
G_eqns = [m*x+b for m, b in zip(G_Slopes, G_y_intercept)]

# Integrate the equations separately between Slopes and Y Intercepts
# Rule: ∫(f(x) + g(x))dx = ∫f(x)dx + ∫g(x)dx

G_Slopes_Part = [m*x for m in G_Slopes]
G_b_Part = [b for b in G_y_intercept]

