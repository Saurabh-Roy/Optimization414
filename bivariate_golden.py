import numpy as np
from tabulate import tabulate

# Output should appear in a text file called results.txt

# WARNING THE LAST ||Ak - Dk||1 column is currenlty wrong

# Inputs *********************************************************************
def f(x: np.ndarray):
    # x is justa a numpy array. the first element is x1 and the second is x2
    return 837.96  - x[0]*np.sin(np.sqrt(x[0])) - x[1]*np.sin(np.sqrt(x[1]))

# +1 for maximising and -1 for minimising
maximising = 1

# Accuracy tolerance
e_tol = 5

# Bounds in the x1 domain
a1_0 = 220
b1_0 = 400

# Bounds in the x2 domain
a2_0 = 220
b2_0 = 360

# phi
phi = 0.618034

# How many decimals you want round off to
decimal_accuracy = 3

# ****************************************************************************

# Ignore this function. Just helps me print results prettier.
def vert_arr(arr):
    return '\n'.join(str(np.round(x, decimal_accuracy)) for x in arr)

# Calc max number of iterations log_phi (e_tol /(b_0 - a_0))
Omega = np.max((
        int(np.ceil(np.log(e_tol/(b1_0-a1_0))/np.log(phi))),
        int(np.ceil(np.log(e_tol/(b2_0-a2_0))/np.log(phi)))
    ))

answer_table1 = []
answer_table2 = []


b1_k = b1_0; a1_k = a1_0
b2_k = b2_0; a2_k = a2_0

for k in range(Omega + 1):
    Ak = np.array([a1_k, a2_k])
    Bk = np.array([b1_k, a2_k])
    Ck = np.array([a1_k, b2_k])
    Dk = np.array([b1_k, b2_k])
    
    alpha1_k = b1_k - phi*(b1_k - a1_k)
    alpha2_k = b2_k - phi*(b2_k - a2_k)
    beta1_k = a1_k + phi*(b1_k - a1_k)
    beta2_k = a2_k + phi*(b2_k - a2_k)
    
    Ek = np.array([alpha1_k, alpha2_k])
    Fk = np.array([beta1_k, alpha2_k])
    Gk = np.array([alpha1_k, beta2_k])
    Hk = np.array([beta1_k, beta2_k])
    
    fA = f(Ak); fB = f(Bk); fC = f(Ck); fD = f(Dk)
    fE = f(Ek); fF = f(Fk); fG = f(Gk); fH = f(Hk)
    
    row1 = [k,vert_arr(Ak),vert_arr(Bk),vert_arr(Ck),vert_arr(Dk),vert_arr(Ek),vert_arr(Fk),vert_arr(Gk),vert_arr(Hk) ]
    row2 = [k, fA, fB, fC, fD, fE, fF, fG, fH, np.max(np.abs(Ak - Dk))]
    answer_table1.append(row1)
    answer_table2.append(row2)
    
    if maximising*fE == np.max(maximising*np.array((fE, fF, fG, fH))):
        b1_k = beta1_k
        b2_k = beta2_k
    elif maximising*fF == np.max(maximising*np.array((fE, fF, fG, fH))):
        a1_k = alpha1_k
        b2_k = beta2_k
    elif maximising*fG == np.max(maximising*np.array((fE, fF, fG, fH))):
        b1_k = beta1_k
        a2_k = alpha2_k
    else:
        a1_k = alpha1_k
        a2_k = alpha2_k
        
        
        
formated_table1 =tabulate(answer_table1, headers=['k','A','B','C','D','E','F','G','H'], tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
formated_table2 =tabulate(answer_table2, headers = ['k','fA','fB','fC','fD','fE','fF','fG','fH','||Ak-Dk||1'],tablefmt='fancy_grid',floatfmt=f'.{decimal_accuracy}f')
print(formated_table1)
print(formated_table2)

with open('results.txt', 'w') as output_file:
    output_file.write(formated_table1)
    output_file.write("\n")
    output_file.write(formated_table2)
    
    
