from itertools import permutations
from sympy import isprime

max=0

for n in range(1,10):
    for perm in permutations(list(range(1, n+1))):
        if isprime(int("".join(map(str,list(perm))))):
            max = int("".join(map(str,list(perm))))

print(max)