def collatz_seq(n, max):
    count = 0
    while n != 1:
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n +1 
        count += 1
    return count


max = 0
num = 0
for n in range(2,1000001):
    m = collatz_seq(n,max)
    if max < m:
        max = m
        num = n
print(num, max)   