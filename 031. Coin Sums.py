def Coins_Sums(v, values):
    c = 0
    while len(values)!= 0:
        u = values[0]
        if u < v:
            c = c + Coins_Sums(v - u, values[:])
            values.remove(u)
        elif u == v:
            c = c + 1
            values.remove(u)
        elif u > v:
            values.remove(u) 
    return c


values = [200, 100, 50, 20, 10, 5, 2, 1]

print(Coins_Sums(values[0], values))


            
