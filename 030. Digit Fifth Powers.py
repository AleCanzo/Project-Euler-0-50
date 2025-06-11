l=[]

for n in range(2,1000000):
    n=str(n)
    sum=0
    for x in n:
        x=int(x)
        sum=sum+pow(x,5)
    n=int(n)
    if(sum==n):
        l.append(n)
        print(n)

sum=0
for n in l:
    sum=sum+n

print(sum)