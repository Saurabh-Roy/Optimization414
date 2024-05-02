import numpy as np
from tabulate import tabulate

# Output should appear in a text file called results.txt

# WARNING: only works with linear and geometric cooling schedules

# Inputs *********************************************************************
def f(x: np.ndarray):
    # x is justa a numpy array. the first element is x1 and the second is x2
    return 837.96  - x[0]*np.sin(np.sqrt(x[0])) - x[1]*np.sin(np.sqrt(x[1]))

# +1 for maximising and -1 for minimising
maximising = 1

# step length
e = 20

# Initial Temperature
T = 1

# Schedules fomrula: Linear or geometric process
heating_schedule = 'geometric'
# heating_schedule = 'linear'

cooling_schedule = 'geometric'
# cooling_schedule = 'linear'
cooling_schedule = 'geometric'

# Heating factor B'
heating_factor = 1.15

# Cooling Factor B
cooling_factor = 0.85

# Initial point
x_0 = np.array([100, 400])

# random number lists
r1 = [0.43,0.77,0.52,0.31,0.04,0.89,0.91,0.46,0.12,0.95,0.38,0.54,0.84,0.33,0.68,0.22,0.59,0.77,0.47,0.57]
r2 = [0.32,0.45,0.98,0.65,0.68,0.11,0.03,0.25,0.51,0.72,0.50,0.37,0.91,0.44,0.67,0.32,0.12,0.09,0.47,0.83]

# Acceptances per epoch
max_a = 3

# Rejections per epoch
max_r = 2

# Max number of reheatings
max_p = 10

# Max number of epochs
max_i = 4

# Max iterations
max_k = 20

# phi
phi = 0.618034

# How many decimals you want round off to
decimal_accuracy = 3

# ****************************************************************************

def pertubation(x, r):
    if r <= 0.25:
        x = x + np.array([e , 0]) 
    elif 0.25 < r <= 0.5:
        x = x + np.array([0 , e]) 
    elif 0.5 < r <= 0.75:
        x = x - np.array([e , 0]) 
    else:
        x = x - np.array([0, e]) 
        
    return x
        
def metropolis_criterion(f_x, f_new_x, T):
    if maximising*f_new_x > maximising*f_x:
        return 1
    else:
        metropolis =  np.exp((f_new_x-f_x)/T)
        return metropolis
    
def reheat(T):
    if heating_schedule == 'linear':
        T = T + heating_factor
    elif heating_schedule == 'geometric':
        T = T*heating_factor
        
    return T
        

def cool(T):
    if cooling_schedule == 'linear':
        T = T + cooling_factor*T
    elif cooling_schedule == 'geometric':
        T = T*cooling_factor
        
    return T
        
answer_table = [] 
     
r1_index = 0
r2_index = 0
p = 0
x_k = x_0  
k = 0
for i in range(max_i+1):
    a = 0; r = 0
    
    while True:
        f_x = f(x_k)
        new_x_k = pertubation(x_k, r1[r1_index])
        r1_index+= 1
        
        
        
        f_new_x = f(new_x_k)
        
        row = [i, T, k, x_k, f_x,r1[r1_index-1], new_x_k, f_new_x]
        
        
        # check metropolis here
        metropolis = metropolis_criterion(f_x, f_new_x, T)
        if metropolis == 1:
            a += 1
            x_k = new_x_k
            row.append('---')
        elif metropolis >= r2[r2_index]:
            row.append(r2[r2_index])
            r2_index += 1
            a += 1
            x_k = new_x_k
        else:
            row.append(r2[r2_index])
            
            r2_index += 1
            r += 1  
        
        row.append(a)
        row.append(r)
        answer_table.append(row)
        k += 1
           
        if r2_index >= len(r2):
            break
        
        if r1_index >= len(r1):
            break
        
        if k>= max_k:
            break
            
        if r >= max_r:
            # reheat
            T = reheat(T)
            p+=1
            break
        elif a >= max_a:
            # cool
            T = cool(T)
            break
    
        
    if r1_index >= len(r1) or r2_index >= len(r2) or k >= max_k:
        break
    if p == max_p:
        break
        
        
formated_table = tabulate(answer_table,headers = ['i','T','k','xk','f(xk)','r1','new_x','f(new_x)','r2','a','r'] ,tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
print(formated_table)

with open('results.txt', 'w') as output_file:
    output_file.write(formated_table)
