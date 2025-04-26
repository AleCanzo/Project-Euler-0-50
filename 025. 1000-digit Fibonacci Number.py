FLAG=False
x = 1
y = 1
index = 2
while FLAG==False:
    z = x + y
    x = y
    y = z
    index = index + 1
    if len(str(z))==1000:
        print(index)
        FLAG=True
        

    