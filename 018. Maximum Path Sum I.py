import numpy as np
N = 15
  
def maxPathSum(tri, i, j, row, col): 
    if(j == col ): 
        return 0
    
    if(i == row-1 ): 
        return tri[i][j]  
    
    return tri[i][j] + max(maxPathSum(tri, i+1, j, row, col), maxPathSum(tri, i+1, j+1, row, col))

tri=np.zeros((N,N), dtype=int)
for i in range(N):
    #tri2 is the file where i copied the triangle
    l=np.loadtxt("tri2.txt", dtype=int, usecols=i, skiprows=i)
    if l.size!=1:
        for j in range(l.size):
            print(j, l, l[j])
            tri[j+i][i]=l[j]            
    else:
        tri[i][i]=l
            
print(tri)
print(maxPathSum(tri, 0, 0, N, N)) 

