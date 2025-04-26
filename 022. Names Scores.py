import numpy as np

l=np.loadtxt("names.txt", dtype=str, delimiter=',')
l=np.sort(l)
for i in range(len(l)):
    l[i]=eval(l[i])
SCORES=np.zeros(len(l))
n=0
for i in range(len(l)):
    n = 0
    for x in l[i]:
        n = n + (ord(x)-64)
    SCORES[i]=n*(i+1)

print(int(np.sum(SCORES)))
        


