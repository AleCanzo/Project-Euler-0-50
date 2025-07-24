from sympy import isprime
from itertools import permutations

v = []

list_primes=[]
for i in range(1000,10000):
    if isprime(i):
        list_primes.append(i)

for n in list_primes:
    n_list = list(str(n))
    for perm1 in permutations(n_list):
        permutation1 = int("".join(map(str,list(perm1))))
        if (permutation1 in list_primes) and (permutation1!=n):
            for perm2 in permutations(n_list):
                permutation2 = int("".join(map(str,list(perm2))))
                if (permutation2 in list_primes) and (permutation2!=permutation1) and (permutation2!=n):
                    l = [n, permutation1, permutation2]
                    l.sort()
                    if(l[2]-l[1]==l[1]-l[0]):
                        if ((l in v) == False):
                            v.append(l)

print(v)

