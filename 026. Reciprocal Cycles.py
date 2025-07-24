def len_cycle(n):
        couples_q_r = []
        list_r = []
        list_q = []
        Flag = False
        r = 1
        dividendo = 1
        list_r.append(1)
        while Flag == False:
                if dividendo < n:
                        dividendo = dividendo * 10
                if dividendo >= n:
                        list_q.append(dividendo//n)
                        r = dividendo % n
                        dividendo = r
                        if r == 0:
                                Flag = True
                        else:
                                list_r.append(r)
                                if (list_q[-1], r) not in couples_q_r:
                                        couples_q_r.append((list_q[-1], r))
                                else:
                                        lenght_cycle = len(couples_q_r[couples_q_r.index((list_q[-1], r)):len(couples_q_r)])
                                        return (list_q, list_r, lenght_cycle)
        return (list_q, list_r, 0)

max = 0
for n in range(2, 1000):
        l = len_cycle(n)[2] 
        if l > max:
                max = l
                n_max = n
        
print(n_max)
    
