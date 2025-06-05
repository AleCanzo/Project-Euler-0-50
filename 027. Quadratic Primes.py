from sympy import isprime

def count_of_primes(a,b):
    Flag=False
    count=0
    n=0
    while Flag==False:
        if isprime(n*n + a*n + b):
            count=count+1
            n=n+1
        else:
            Flag=True
    return(count)    

max=0
for a in range(-1000,1000):
    for b in range(-1000,1001):
        x = count_of_primes(a,b)
        if x > max:
            print("a={}, b={}, numero di primi={}".format(a, b, x))
            max=x