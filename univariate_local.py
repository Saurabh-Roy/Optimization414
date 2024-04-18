import numpy as np
from tabulate import tabulate

# Output should appear in a text file called results.txt

# Inputs *********************************************************************
def f(x):
    return 1 + 2*(x**2) - np.exp(x) 


# +1 for maximising and -1 for minimising
maximising = -1

# accuracy tolerance
e_tol = 0.00025

# Initial step length
e = 0.1

# a
a = 0.5

# initial point
x_0 = 0.7

#  :)
phi = 0.618034

# Maximum number of iterations (used if you don't want to wait till convergence)
max_iterations = 30

# How many decimals you want round off to
decimal_accuracy = 6
# ****************************************************************************


answer_table = []

x_k = x_0
k = 0
for i in range(max_iterations):
    
    if e < e_tol:
        break
    
    neighbourhood = [np.round(x_k - e, decimal_accuracy), np.round(x_k + e, decimal_accuracy)]
    
    results = np.array([f(x_k),f(neighbourhood[0]), f(neighbourhood[1])])
    
    best_performer = np.argmax(maximising*results)
    
    row = [k, e, x_k, neighbourhood, results[0], results[1:]]
    answer_table.append(row)
    
    if best_performer > 0:
        x_k = np.round(neighbourhood[best_performer-1], decimal_accuracy)
        
    
    else:
        e = e*a
        
    k += 1
    
  
# Output results  
formated_table =tabulate(answer_table, headers=['k','e','x_k','Neighbourhood', 'f(x_k)','Neighbourhood results'], tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
print(formated_table)

with open('results.txt', 'w') as output_file:
    output_file.write(formated_table)