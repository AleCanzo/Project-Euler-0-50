
def is_pandigital(s):
    l = list(map(int,s))
    for n in range(1,9):
        if n in l:
            l.remove(n)
        else:
            return False
    return True
        
max = 0
for n in range(1,10000):
    s = ""
    Flag = True
    i = 1
    count = 0
    while Flag == True:
        if len(s + str(n*i))<=9:
            s = s + str(n*i)
            i = i + 1
        else:
            Flag = False
    if is_pandigital(s):
        if int(s) > max:
            max = int(s)

print(max)    