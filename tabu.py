import numpy as np
from tabulate import tabulate
from automatic_queue import Automatic_Queue
# Output should appear in a text file called results.txt

# WARNING this will not work if the question works with aspiration criteria

# Inputs *********************************************************************
def f(x: np.ndarray):
    # x is justa a numpy array. the first element is x1 and the second is x2
    return (x[0]-3.14)**2 + (x[1]-2.72)**2 + np.sin(3*x[0]+1.41) + np.sin(4*x[1]- 1.73)

# +1 for maximising and -1 for minimising
maximising = -1

# Initial Step lenght
e = 0.3

# Accuracy tolerance
e_tol = 0.01

# Initial point
x_0 = np.array([1, 1])

# Time not improving till you want to stop
time_to_stop = 5

# Tabue List: max_size = how many items can be tabu at one time
tabu_list = Automatic_Queue(max_size=2)

# How many decimals you want round off to
decimal_accuracy = 3
# ****************************************************************************

answer_table = []

# This will hold the indeces of which neighbour is tabu in the neighbourhood list

x_k = x_0
incumbent_solution = f(x_0)
k = 0
while(True):
    neighbourhood = np.array([
        x_k + [e, 0],
        x_k + [0, e],
        x_k - [e, 0],
        x_k - [0, e]
    ])
    
    f_xk = f(x_k)
    results = []
    for point in neighbourhood:
        results.append(f(point))
        
    # results that will show up in table (will show if a solution is Tabu or not)
    display_results = np.round(results, decimal_accuracy)
    
    for tabu_index in tabu_list.queue:
        if tabu_index is not None:
            display_results[tabu_index] = None
    
    
    results = np.array(results)
    
    row = [k, e, np.round(x_k,decimal_accuracy), np.round(neighbourhood,decimal_accuracy), np.round(f(x_k),decimal_accuracy), np.round(display_results, decimal_accuracy)]
    answer_table.append(row)
    
    # Sorts the indexes of the results array from worst performing to best performing
    ordered_results_indeces = np.argsort(maximising*results)
    
    for index in reversed(ordered_results_indeces):
        if index not in tabu_list.queue:
            if maximising*results[index] > maximising*incumbent_solution:
                incumbent_solution = results[index]
                time_without_improvement = 0
            else:
                time_without_improvement += 1
                
            x_k = neighbourhood[index]
           
            if index <= 1:
                tabu_list.enqueue(index+2)
            else:
                tabu_list.enqueue(index-2)
            
            break  
    k += 1
    if time_without_improvement >= time_to_stop+1:
        break
     
formated_table =tabulate(answer_table, headers=['k','e','x_k','Neighbourhood', 'f(x_k)','Neighbourhood results'], tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
print(formated_table)

with open('results.txt', 'w') as output_file:
    output_file.write(formated_table)

    
    