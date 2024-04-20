import numpy as np
from tabulate import tabulate

# Output should appear in a text file called results.txt

# Inputs *********************************************************************
def f(x: np.ndarray):
    # x is justa a numpy array. the first element is x1 and the second is x2
    return -1*(x[0]**3) + 3*x[0] - (x[1]**2)


# +1 for maximising and -1 for minimising
maximising = 1

# Initial Step lenght
e = 0.3

# a
a = 0.5

# Accuracy tolerance
e_tol = 0.1

# Initial point
x_0 = np.array([0.7, -0.5])

# Maximum number of iterations (used if you don't want to wait till convergence)
max_iterations = 30

# How many decimals you want round off to
decimal_accuracy = 3

# ****************************************************************************


answer_table = []

x_k = x_0
k = 0
for i in range(max_iterations):
    neighbourhood = np.array([
        x_k + [e, 0],
        x_k - [e, 0],
        x_k + [0, e],
        x_k - [0, e]
    ])
    
    results = [f(x_k)]
    for point in neighbourhood:
        results.append(f(point))
        
    results = np.array(results)
    
    best_performer = np.argmax(maximising*results)
    
    row = [k, e, np.round(x_k,decimal_accuracy), np.round(neighbourhood,decimal_accuracy), np.round(results[0],decimal_accuracy), np.round(results[1:], decimal_accuracy)]
    answer_table.append(row)
    
    if e < e_tol:
        break
    
    if best_performer == 0:
        e = a*e
    else:
        x_k = neighbourhood[best_performer-1]
        
    k += 1
    
    
    
formated_table =tabulate(answer_table, headers=['k','e','x_k','Neighbourhood', 'f(x_k)','Neighbourhood results'], tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
print(formated_table)

with open('results.txt', 'w') as output_file:
    output_file.write(formated_table)
