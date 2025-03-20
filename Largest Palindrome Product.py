def is_pal(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

max = 0
for i in range(100,1000):
    for j in range(100,1000):
        if is_pal(i*j) == True and i*j > max:
            max = i*j
print(max)
        
