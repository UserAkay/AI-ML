import sympy as sp

#Define variables and the multivariable function
x, y = sp.symbols('x y')
f = x**3 * y + x * sp.sin(y)

#Compute the Hessian matrix
hessian_matrix = sp.hessian(f, (x, y))

#Print the results
print("Function f(x, y): \n",(f))
print("Hessian Matrix: \n", hessian_matrix)
