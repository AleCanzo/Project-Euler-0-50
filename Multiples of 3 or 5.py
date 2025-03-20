def list_mult_in_range(n,m):
    mult = n
    i = 1
    list=[]
    while mult < m:
        list.append(mult)
        i += 1
        mult = n*i
    return list

print(sum(list(dict.fromkeys(list_mult_in_range(3,1000)+list_mult_in_range(5,1000)))))
