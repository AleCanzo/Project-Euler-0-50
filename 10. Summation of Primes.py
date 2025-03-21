from sympy import isprime

s = 0
for i in range(1,2000001):
    print(i)
    if isprime(i) == True:
        s += i

print(s)