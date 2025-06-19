from sympy import isprime 
import numpy as np

def is_circular_prime(x):
    n_list=np.array(list(str(x)))
    for i in range(len(n_list)):
        y=int("".join(map(str,list(np.roll(n_list, i)))))
        if isprime(y)==False:
            return False
    return True

count=0

n=1000000

list_primes=[]
for i in range(1,n):
    if isprime(i):
        list_primes.append(i)

for x in list_primes:
    Flag=True
    Flag=is_circular_prime(x)
    if Flag==True:
        count=count+1

print(count) 
        
