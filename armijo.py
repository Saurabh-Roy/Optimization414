import numpy as np
import sympy as sp
from tabulate import tabulate


x1, x2 = sp.symbols('x1 x2')

# f = (1/3)*x1**3 + x2**2 + 2*x1*x2 - 6*x1 - 3*x2 + 4
f= -(x1**2)-4*(x2**2) + 2*(x1)+8*(x2)-5
gradient_f = [sp.diff(f, var) for var in (x1, x2)]

f = sp.lambdify((x1, x2), f.evalf(), 'numpy')
gradient_f = sp.lambdify((x1, x2), [grad.evalf() for grad in gradient_f], 'numpy')

def armijo_goldstein(f,grad_f,a,b,p,x):
    armijo_table = []
    # REMINDER TO CHANGE THIS INEQUALITY BASED ON MINIMISING OR MAXIMISING
    alpha = 1
    print("GOLDSTEIN-------------------------------------------")
    # while not(f(x_1+alpha*p_1,x_2+alpha*p_2) > f(x_1,x_2) + a*alpha*grad_f(x_1,x_2).dot(np.array([p_1,p_2]))):
    while not(int(f(*(x + alpha * p))) > int(f(*x) + a * alpha * np.dot(grad_f(*x),p))):
        armijo_table.append([alpha,f(*(x + alpha * p)),f(*x) + a * alpha *np.dot(grad_f(*x),p)]) 
        alpha = b*alpha
        # print(alpha)
    # armijo_table.append([alpha,f(*(x + alpha * p)),f(*x) + a * alpha *np.dot(grad_f(*x),p)]) 
    
    print(tabulate(armijo_table, headers=['alpha','f(x + ap)','f(x)+a*alpha*H*p'], tablefmt='fancy_grid'))
    
    
    return alpha

x = sp.Matrix([0,0])     
p = sp.Matrix([2,8])

armijo_goldstein(f, gradient_f, 0.4, 0.9, p, x)