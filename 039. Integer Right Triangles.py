
def integral_length(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    if(pow(l[0],2)+pow(l[1],2)==pow(l[2],2)):
        return True
    else:
        return False

max_count = 0                
for p in range(1,1001):
    count = 0
    for x in range(1,p):
        for y in range(x, p):
            if x + y < p:
                z = p - (x + y)
                if z!=0 and integral_length(x,y,z):
                    count = count + 1
    if count>max_count:
        max_num=p
        max_count=count                

print(max_num, max_count)                    
    
            

            
             