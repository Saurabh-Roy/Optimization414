import numpy as np
from tabulate import tabulate
x_0 = -1.5
x_1 = -0.5

def f(x):
    return -(x**4) + (np.e ** x)

def secant_method(x0, x1,f,iterations):
    def delta_xk(xk,xk_minus,f):
        return -((xk_minus -xk)/(f(xk_minus)-f(xk))) * f(xk)
    
    
    x_k = x1
    x_k_minus = x0
    delta = delta_xk(x_k, x_k_minus, f)
    
    answer_table = []
    for i in range(iterations):
        # print(f"xk-: {x_k_minus}  xk:{x_k} f(xk-): {f(x_k_minus)} f(xk): {f(x_k)} delta: {delta}")
        row = [x_k_minus,x_k, f(x_k_minus),f(x_k),delta]
        answer_table.append(row)
        # print("")
        x_k_plus = x_k + delta
        x_k, x_k_minus = x_k_plus, x_k
        
        delta = delta_xk(x_k, x_k_minus, f)
        
        if abs(x_k - x_k_minus) < 0.000000001:
            break
        
    print(tabulate(answer_table, headers=['x_k-1','xk','f(x_k-1)','f(xk)','delta'], tablefmt='fancy_grid'))
        
secant_method(x_0,x_1,f,10)