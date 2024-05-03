import numpy as np
from tabulate import tabulate

import random

# Output should appear in a text file called results.txt


# Inputs *********************************************************************
def f(x: np.ndarray):
    # x is justa a numpy array. the first element is x1 and the second is x2
    # return (x[:,0]-3.14)**2 + (x[:,1]-2.72)**2 + np.sin(3*x[:,0] + 1.41) + np.sin(4*x[:,1]-1.73)
    # return 20 + x[:,0]**2 + x[:,1]**2 - 10*(np.cos(2*np.pi*x[:,0]) + np.cos(2*np.pi*x[:,1]))
    return -x[:,0]**3 + 3*(x[:,0]) - x[:,1]**2

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

# radom numbers
r = [0.43, 0.32, 0.77, 0.52, 0.45, 0.31, 0.98, 0.04, 0.89, 0.91, 0.46, 0.65, 0.12, 0.68,
0.81, 0.91, 0.13, 0.91, 0.63, 0.10, 0.28, 0.55, 0.96, 0.96, 0.16, 0.97, 0.96, 0.49, 0.80,
0.14, 0.42, 0.92, 0.79, 0.96, 0.66, 0.04, 0.85, 0.93, 0.68, 0.76, 0.74, 0.39, 0.66, 0.17]

# Number of iterations to run
num_iterations = 1


# How many decimals you want round off to
decimal_accuracy = 3

# ****************************************************************************

def velocity_update(velocity: np.array,partical: np.array, x:np.array ,x_best: np.array, c1: float, c2: float, p1: float, p2: float, w: float, p3, p4) -> np.array:
    # print(x)
    updated_velocity_1 = w*velocity[0] + p1*c1*(partical[0]-x[0]) + p2*c2*(x_best[0,0]-x[0])
    updated_velocity_2 = w*velocity[1] + p3*c1*(partical[1]-x[1]) + p4*c2*(x_best[0,1]-x[1])
    updated_velocity = [updated_velocity_1, updated_velocity_2]
    # print(updated_velocity)
    return np.squeeze(updated_velocity)



answer_table = []

random_number_index = 0

for k in range(num_iterations+1):
    x_best = np.array([x_population[np.argmax(maximising*f(x_population))]])
    
    row = [k, str(np.round(x_population,decimal_accuracy)),str(np.round(velocities, decimal_accuracy)),str(np.round(f(x_population),decimal_accuracy)), x_best]
    answer_table.append(row)
    
    new_velocities = []
    for i,partical in enumerate(particals):
        partical_copy = np.array([partical.copy()])
        
        new_velocities.append(velocity_update(velocities[i],partical,x_population[i],x_best,c1,c2,r[random_number_index],r[random_number_index+1],w,r[random_number_index+2],r[random_number_index+3]))
        print(r[random_number_index])
        print(r[random_number_index+1])
        print(r[random_number_index+2])
        print(r[random_number_index+3])
        # new_velocities[i] =  w*velocities[i] + p1*c1*(partical-x_population[i]) + p2*c2*(x_best-x_population[i])
        
        x_population[i] += velocity_update(velocities[i],partical,x_population[i],x_best,c1,c2,r[random_number_index],r[random_number_index+1],w,r[random_number_index+3],r[random_number_index+3])
        random_number_index += 4
        
        
        # current_itertations_x_best = np.array([x_population[np.argmax(maximising*f(x_population))]])
        # test_partical = np.array([particals[i].copy()])
        if maximising*f(np.array([x_population[i]])) > maximising*f(partical_copy):
            # partical = np.array([x_population[np.argmax(maximising*f(x_population))]])
            # print(x_population[i])
            particals[i] = x_population[i]
            
                
    #     if maximising*f(np.array([x_population[i]])) > maximising*f(x_best):
    #         x_best = np.array([x_population[np.argmax(maximising*f(x_population))]])
            
    velocities = np.array(new_velocities)
    
    
    
# for i,partical in enumerate(particals):
#     partical_copy = np.array([partical.copy()])
    
#     new_velocities.append(velocity_update(velocities[i],partical,x_population[i],x_best,c1,c2,r[random_number_index],r[random_number_index+1],w,r[random_number_index+2],r[random_number_index+3]))
#     print(r[random_number_index])
#     print(r[random_number_index+1])
#     print(r[random_number_index+2])
#     print(r[random_number_index+3])
#     # new_velocities[i] =  w*velocities[i] + p1*c1*(partical-x_population[i]) + p2*c2*(x_best-x_population[i])
    
#     x_population[i] += velocity_update(velocities[i],partical,x_population[i],x_best,c1,c2,r[random_number_index],r[random_number_index+1],w,r[random_number_index+3],r[random_number_index+3])
#     random_number_index += 4
        
# velocities = np.array(new_velocities)

# print(x_population)
# print(velocities)
    
formated_table = tabulate(answer_table,headers=['k','population', 'velocities','f(population)', 'x_best'], tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
print(formated_table)

print('last velos')
print(velocities)
print('last pop')
print(x_population)

print('last f(pop)')
print(f(x_population))


with open('results.txt', 'w') as output_file:
    output_file.write(formated_table)
    
            
        
        


