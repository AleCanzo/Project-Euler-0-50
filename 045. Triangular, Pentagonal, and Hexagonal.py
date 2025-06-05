T=[]
P=[]
H=[]

for n in range(100000):
    T.append(int(n*(n+1)/2))
    P.append(int(n*(3*n-1)/2))
    H.append(int(n*(2*n-1)))
    
for x in T:
    if x in P:
        if x in H:
            print(x)
