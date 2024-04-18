import numpy as np
from tabulate import tabulate

# Output should appear in a text file called results.txt

# Inputs *********************************************************************
def f(x):
    return x - np.sin(5*np.sqrt(2*x)) + 7*np.cos(4*x)
    # return 1 + 2*(x**2) - np.exp(x)


# +1 for maximising and -1 for minimising
maximising = 1

# accuracy tolerance
e_tol = 0.05

# Bounds
a_0 = 2
b_0 = 3

#  :)
phi = 0.618034

# How many decimals you want round off to
decimal_accuracy = 6
# ****************************************************************************

# Calc max number of iterations log_phi (e_tol /(b_0 - a_0))
Omega = int(np.ceil(np.log(e_tol/(b_0-a_0))/np.log(phi)))


answer_table = []

b_k = b_0; a_k = a_0
for i in range(Omega+1):
    alpha_k = b_k - phi*(b_k - a_k)
    beta_k = a_k + phi*(b_k-a_k)
    
    f_alpha = f(alpha_k)
    f_beta = f(beta_k)
    
    row = [i, a_k, b_k, alpha_k, beta_k, f(a_k),f(b_k),f_alpha, f_beta, b_k-a_k]
    answer_table.append(row)
    
    if (maximising*f_alpha > maximising*f_beta):
        b_k = beta_k
    else:
        a_k = alpha_k
    
            
formated_table =tabulate(answer_table, headers=['k','ak','bk','alpha_k','beta_k','f(a)','f(b)','f(alpha)','f(beta)','ak-bk'], tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
print(formated_table)

with open('results.txt', 'w') as output_file:
    output_file.write(formated_table)
