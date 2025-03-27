def sum_div_num_list(d, n):
    d.append(0)
    for i in range(1, n):
        s = 0
        for j in range(1,i):
            if i%j == 0:
                s = s + j
        d.append(s)
    return d

n = 10001
#a list where i append the sum of the divisor of every num
d = []
d = sum_div_num_list(d, n)
#a list where i append all the amicable number
amic_num = []
for i in range(1, n-1):
    if d[i] < len(d):
        if d[d[i]] == i and d[i] != i:
            amic_num.append(i)


print(sum(amic_num))


        
