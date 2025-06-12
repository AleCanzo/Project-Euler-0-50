from math import factorial

sum=0
for n in range(10,5000000):
    n_list=list(str(n))
    for x in n_list:
        sum=sum+factorial(int(x))
    if sum==n:
        print(n)
    sum=0    
