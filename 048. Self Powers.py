sum = 0
for i in range(1,1001):
    #print(i)
    sum = sum + pow(i, i)
    #print(sum)

print(str(sum)[-10:(len(str(sum)))])