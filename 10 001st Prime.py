from sympy import isprime

i = 0
n = 2
while i < 10001:
    if isprime(n) == True:
        i += 1
    n += 1
print(n-1)