from sympy import * 

def max_prime_fact(n):
    max = 0
    if isprime(n) == True:
        return n
    else:
        for i in range(1,int((n+1)/2)):
            if n%i == 0 and i > max and isprime(i) == True:
                max = max_prime_fact(int(n/i))
                return max
        

print(max_prime_fact(600851475143))

