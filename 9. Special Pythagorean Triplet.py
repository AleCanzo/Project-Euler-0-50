from math import sqrt

Flag = False
h = 5
while Flag == False:
    for i in range(h):
        for j in range(i):
            #print(sqrt(pow(j,2)+pow(i,2))) 
            if sqrt(pow(j,2)+pow(i,2)) == h and h+j+i == 1000:
                print(j*i*int(sqrt(pow(j,2)+pow(i,2))))
                Flag = True
    h += 1