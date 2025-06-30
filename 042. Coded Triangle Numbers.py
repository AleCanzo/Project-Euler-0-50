import numpy as np


def is_triang(x):
    for n in range(25):
        if x == int((n*(n+1))/2):
            return True
    return False

l = np.loadtxt("0042_words.txt", dtype=str, delimiter=",")
l = np.char.strip(l, "\"")

count =  0
for w in l:
    value = 0
    for c in w:
        value = value + (ord(c)-64)
    if is_triang(value):
        count = count + 1
        
print(count)