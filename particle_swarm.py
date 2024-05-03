import numpy as np
from tabulate import tabulate

import random

# Output should appear in a text file called results.txt


# Inputs *********************************************************************
def f(x: np.ndarray):
    # x is justa a numpy array. the first element is x1 and the second is x2
    # return (x[:,0]-3.14)**2 + (x[:,1]-2.72)**2 + np.sin(3*x[:,0] + 1.41) + np.sin(4*x[:,1]-1.73)
    return 20 + x[:,0]**2 + x[:,1]**2 - 10*(np.cos(2*np.pi*x[:,0]) + np.cos(2*np.pi*x[:,1]))

# +1 for maximising and -1 for minimising
maximising = 1

# Initial population
x_population = np.array([[0.3,-0.2],[-0.9,0.5],[-0.4,0.5],[0.9,0.7],[-0.4,-0.5]])
swarm_size = len(x_population)
particals = x_population.copy()


# Initial velocity vectors (must be same length as x_population)
velocities = np.array([[0,0],[0,0],[0,0],[0,0],[0,0]])
# Inertia
w = 0.8

# Cognitive Factor 1
c1 = 0.2

# Cognitive Factor 2
c2 = 0.2

# 
p1 = 0.5

# 
p2 = 0.5

# Number of iterations to run
num_iterations = 5


# How many decimals you want round off to
decimal_accuracy = 3

# ****************************************************************************

def velocity_update(velocity: np.array,partical: np.array, x:np.array ,x_best: np.array, c1: float, c2: float, p1: float, p2: float, w: float) -> np.array:
    
    updated_velocity = w*velocity + p1*c1*(partical-x) + p2*c2*(x_best-x)
        
    return np.squeeze(updated_velocity)



answer_table = []

for k in range(num_iterations+1):
    x_best = np.array([x_population[np.argmax(maximising*f(x_population))]])
    
    row = [k, str(np.round(x_population,decimal_accuracy)),str(np.round(velocities, decimal_accuracy)),str(np.round(f(x_population),decimal_accuracy)), x_best]
    answer_table.append(row)
    
    new_velocities = []
    for i,partical in enumerate(particals):
        partical_copy = np.array([partical.copy()])
        new_velocities.append(velocity_update(velocities[i],partical,x_population[i],x_best,c1,c2,p1,p2,w))
        # new_velocities[i] =  w*velocities[i] + p1*c1*(partical-x_population[i]) + p2*c2*(x_best-x_population[i])
        
        x_population[i] += velocity_update(velocities[i],partical_copy,x_population[i],x_best,c1,c2,p1,p2,w)
        
        
        # current_itertations_x_best = np.array([x_population[np.argmax(maximising*f(x_population))]])
        # test_partical = np.array([particals[i].copy()])
        if maximising*f(np.array([x_population[i]])) > maximising*f(partical_copy):
            # partical = np.array([x_population[np.argmax(maximising*f(x_population))]])
            # print(x_population[i])
            particals[i] = x_population[i]
            
            
    # if maximising*f(np.array([x_population[i]])) > maximising*f(x_best):
    #     x_best = np.array([x_population[np.argmax(maximising*f(x_population))]])
            
    velocities = np.array(new_velocities)
        
formated_table = tabulate(answer_table,headers=['k','population', 'velocities','f(population)', 'x_best'], tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
print(formated_table)
with open('results.txt', 'w') as output_file:
    output_file.write(formated_table)
    
            
        
        


