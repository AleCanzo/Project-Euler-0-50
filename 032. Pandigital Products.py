from itertools import permutations

l=[]
for t in permutations([1,2,3,4,5,6,7,8,9]):
    for i in range(1,7):
        for j in range(i+2, 8):            
            x=int("".join(map(str,list(t[0:i]))))
            y=int("".join(map(str,list(t[i:j]))))
            n=int("".join(map(str,list(t[j:9]))))
            if x*y==n:
                print("{}*{}={}".format(x,y,n))
                l.append(n)


l=list(dict.fromkeys(l))
print(sum(l))
