from sympy import divisors

def is_abundant(n):
    divisors_n=divisors(n)
    divisors_n.pop()
    if sum(divisors_n)>n:
        return True
    else:
        return False

LIST_ABUNDANT=[]
for n in range(1, 28124):
    if is_abundant(n)==True:
        LIST_ABUNDANT.append(n)
        
NUM_SUM_ABUNDANT=[]
for i in LIST_ABUNDANT:
    for j in LIST_ABUNDANT[LIST_ABUNDANT.index(i):len(LIST_ABUNDANT)]:
        if ((i+j)<=28123):
            NUM_SUM_ABUNDANT.append(i+j)


ALL_NUM = []
for n in range(1,28124):
    ALL_NUM.append(n)

l = list(set(ALL_NUM) - set(NUM_SUM_ABUNDANT))
print(sum(l))