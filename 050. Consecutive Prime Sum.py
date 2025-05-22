from sympy import *

List_primes=[]
for n in range(10000):
    if isprime(n):
        List_primes.append(n)

print(List_primes)

for j in range(21, len(List_primes)-1):
    for i in range(len(List_primes)-j):
        if ((isprime(sum(List_primes[i:i+j]))) and (sum(List_primes[i:i+j])<1000000)):
            print(sum(List_primes[i:i+j]), len(List_primes[i:i+j]))

        

