l=[]

for a in range(2,101):
    for b in range(2,101):
        l.append(pow(a,b))

print(len(list(dict.fromkeys(l))))
