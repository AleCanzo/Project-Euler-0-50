from math import sqrt

def num_div(n):
    count = 2
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            count += 2
    return count

Flag = False
n = 1
s = 0
while Flag == False:
    s += n
    if num_div(s) >= 500:
        Flag = True
    n += 1    