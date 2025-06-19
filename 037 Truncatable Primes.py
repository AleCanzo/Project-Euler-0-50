from sympy import isprime



def is_truncatable_r(n):
    n_list=list(str(n))
    while len(n_list)!=1:
        del n_list[-1]
        x=int("".join(map(str,list(n_list))))
        if isprime(x)==False:
            return False
    if isprime(int(n_list[0])):
        return True
    else:
        return False
         
            
def is_truncatable_l(n):
    n_list=list(str(n))
    while len(n_list)!=1:
        del n_list[0]
        x=int("".join(map(str,list(n_list))))
        if isprime(x)==False:
            return False
    if isprime(int(n_list[0])):
        return True
    else:
        return False        
    
count=0
n=10
sum=0
        
while count!=11:
    if isprime(n):
        #print(n)
        if is_truncatable_r(n) and is_truncatable_l(n):
            sum=sum+n
            count=count+1
    n=n+1

print(sum)