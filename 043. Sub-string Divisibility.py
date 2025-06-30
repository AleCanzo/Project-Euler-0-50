from itertools import permutations

sum = 0

for perm in permutations([0,1,2,3,4,5,6,7,8,9]):
    l = list(perm)
    if (int(''.join(map(str, l[1:4]))) % 2 == 0) and (int(''.join(map(str, l[2:5]))) % 3 == 0) and (int(''.join(map(str, l[3:6]))) % 5 == 0) and (int(''.join(map(str, l[4:7]))) % 7 == 0) and (int(''.join(map(str, l[5:8]))) % 11 == 0) and (int(''.join(map(str, l[6:9]))) % 13 == 0) and (int(''.join(map(str, l[7:10]))) % 17 == 0):
        sum = sum +  int("".join(map(str,list(perm))))
    
print(sum)

