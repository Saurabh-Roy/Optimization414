import numpy as np
import sympy as sp
from tabulate import tabulate


x1, x2 = sp.symbols('x1 y2')

f = (1/3)*x1**3 + x2**2 + 2*x1*x2 - 6*x1 - 3*x2 + 4
gradient_f = [sp.diff(f, var) for var in (x1, x2)]

f = sp.lambdify((x1, x2), f.evalf(), 'numpy')
gradient_f = sp.lambdify((x1, x2), [grad.evalf() for grad in gradient_f], 'numpy')


def armijo_goldstein(f,grad_f,a,b,p,x):
    armijo_table = []
    # REMINDER TO CHANGE THIS INEQUALITY BASED ON MINIMISING OR MAXIMISING
    alpha = 1
    print("GOLDSTEIN-------------------------------------------")
    # while not(f(x_1+alpha*p_1,x_2+alpha*p_2) > f(x_1,x_2) + a*alpha*grad_f(x_1,x_2).dot(np.array([p_1,p_2]))):
    while not(f(*(x + alpha * p)) < f(*x) + a * alpha * np.dot(grad_f(*x),p)):
        armijo_table.append([alpha,f(*(x + alpha * p)),f(*x) + a * alpha *np.dot(grad_f(*x),p)]) 
        alpha = b*alpha
        # print(alpha)
    armijo_table.append([alpha,f(*(x + alpha * p)),f(*x) + a * alpha *np.dot(grad_f(*x),p)]) 
    
    print(tabulate(armijo_table, headers=['alpha','f(x + ap)','f(x)+a*alpha*H*p'], tablefmt='fancy_grid'))
    
    
    return alpha

# print(np.dot(gradient_f(1,1),np.array([2,8])))
# armijo_goldstein(f,gradient_f,0.45,0.95,sp.Matrix([-13,-3]),sp.Matrix([2.5,1.5]))

B = sp.Matrix([[7,3],[3,2]])
x_init = sp.Matrix([4,-2])
def SR1(B, x_init, a, b,f, grad_f):
    xk = x_init
    
    answer_table_1 = []
    answer_table_2 = []
    answer_table_3 = []
    
    for i in range(5):
        answer_row = []
        answer_row_2 = []
        answer_row_3 = []
        
        
        answer_row.append(list(xk))
        answer_row.append(list(sp.Matrix(grad_f(*xk))))
        answer_row.append(np.array(B))
        
        pk = -B.inv()*sp.Matrix(grad_f(*xk))
        answer_row_2.append(list(pk))
        
        alpha = armijo_goldstein(f, grad_f, a, b, pk, xk)
        answer_row_2.append(alpha)
        
        xk_minus = xk
        xk = xk + alpha*pk
        
        sk = xk - xk_minus
        answer_row_2.append(list(sk))
        
        yk = sp.Matrix(grad_f(*xk)) - sp.Matrix(grad_f(*xk_minus))
        answer_row_3.append(list(yk))
        
        answer_row_3.append(sp.Matrix(grad_f(*xk_minus)).norm(2))
        
        B += ((yk - B*sk) * (yk - B*sk).T) / (yk - B*sk).dot(sk)
        answer_table_1.append(answer_row)
        answer_table_2.append(answer_row_2)
        answer_table_3.append(answer_row_3)
        
    print(tabulate(answer_table_1,headers=['xk','f`(xk)','B'], tablefmt='fancy_grid'))
    print(tabulate(answer_table_2,headers=['pk','a','sk',], tablefmt='fancy_grid'))
    print(tabulate(answer_table_3,headers=['yk','||f`(xk)||'], tablefmt='fancy_grid'))
    
       
SR1(B, x_init,0.45,0.95,f,gradient_f)