import numpy as np
from tabulate import tabulate
x_0 = 1
x_1 = 2

def f(x):
    # return -(x**4) + (np.e ** x)
    return np.sin(np.e**x)
    

def derivative(f, x, h=9e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

def secant_method(x0, x1,f,derivative,iterations):
    def delta_xk(xk,xk_minus,f, derivative):
        return -((xk_minus -xk)/(derivative(f,xk_minus)-derivative(f,xk))) * derivative(f,xk)
    
    
    x_k = x1
    x_k_minus = x0
    delta = delta_xk(x_k, x_k_minus, f, derivative)
    
    answer_table = []
    for i in range(iterations):
        # print(f"xk-: {x_k_minus}  xk:{x_k} f(xk-): {derivative(f,x_k_minus)} f(xk): {derivative(f,x_k)} delta: {delta}")
        answer_table.append([x_k_minus, x_k, derivative(f,x_k_minus),derivative(f,x_k), delta])
        x_k_plus = x_k + delta
        x_k, x_k_minus = x_k_plus, x_k
        
        delta = delta_xk(x_k, x_k_minus, f, derivative)
        
        if abs(x_k - x_k_minus) < 0.0005:
            break
        
    print(tabulate(answer_table, headers=['x_k-1','xk','f`(x_k-1)','f`(xk)','delta'], tablefmt='fancy_grid', floatfmt='.7f'))
    
secant_method(x_0,x_1,f,derivative,12)