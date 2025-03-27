sum_sq = 0
sum = 0
for i in range(1,101):
    sum_sq += pow(i,2)
    sum += i
print(pow(sum,2) - sum_sq)
