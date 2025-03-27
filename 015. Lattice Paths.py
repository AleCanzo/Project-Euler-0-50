import numpy as np

def num_paths(M, a, b):
    if M[a,b] != 0:
        return M[a,b]
    if a == 20 and b != 20:
        M[a,b] = num_paths(M, a, b+1)        
    if b == 20 and a != 20:
        M[a,b] = num_paths(M, a+1, b)
    if a == b == 20:
        return 1
    if a != 20 and b != 20:
        M[a,b] = num_paths(M, a+1, b) + num_paths(M, a, b+1)
    return M[a,b]


M = np.zeros((21,21), int)
print(num_paths(M, 0, 0))
