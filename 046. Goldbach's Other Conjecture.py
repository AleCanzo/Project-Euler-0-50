from sympy import isprime
import math

def Goldbach_num(n):
    for x in range(n): 
        for p in range(3,n):
                if isprime(p) and n >= p + 2 * pow(x,2):
                    d = p + 2 * pow(x,2)
                    if d==n:
                        return False
    return True

Flag=False
n=2
while Flag==False:
    if(n % 2 !=0):
        if isprime(n)==False:
            Flag=Goldbach_num(n)
    n = n+1

print(n-1)
