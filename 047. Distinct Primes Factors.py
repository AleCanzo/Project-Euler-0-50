from sympy import *
#Nella lista l metto tutti i primi che dividono n, L è il dizionario di tutte le liste l
L={}
M=[]

for n in range(1,1000000):
    l=[]    
    for p in divisors(n):    
        if isprime(p) & (n % p==0):
            l.append(p)            
    L[n]=l

#In M metto tutte i numeri che hanno un certo numero di divisori distinti

for n in L:
    #print(n, L[n])
    if len(L[n])==4:
        #print(n, L[n])
        M.append(n)

#print(M)
print("uscito")
Flag=false
i=0
while Flag==false:
    print(i)
    if M[i+3]==M[i+2]+1==M[i+1]+2==M[i]+3:
        Flag=true
        print(M[i], M[i+1], M[i+2], M[i+3])
    i=i+1
    
        
        
        
        