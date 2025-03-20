import math
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def mod_list(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j]%l[i] == 0:
                l[j] = int(l[j]/l[i])
    return l
print(l)
print(math.prod(mod_list(l)))