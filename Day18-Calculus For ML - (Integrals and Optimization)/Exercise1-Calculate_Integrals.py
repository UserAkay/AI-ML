import sympy as sp

#Define a function
X = sp.Symbol('X')
f = sp.exp(-X)

#Compute indefinite integral
indefinite_integral = sp.integrate(f, X)
print("Indefinite integret: ", indefinite_integral)

#Compute definite integral
definite_integral = sp.Integral(f, (X, 0, sp.oo))
print("Definite Integral: ", definite_integral)
