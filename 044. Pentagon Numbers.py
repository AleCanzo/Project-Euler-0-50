
N=10000

list_pentagon = []
for i in range(1,N):
    list_pentagon.append(int(i*(3*i -1)/2))
   

for x in list_pentagon:
    for y in list_pentagon:
        if y>x:
            if ((x+y) in list_pentagon):
                if ((y-x) in list_pentagon):
                    print(x, y, x+y, abs(x-y))
            

    
    