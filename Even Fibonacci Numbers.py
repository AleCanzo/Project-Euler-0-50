def list_even_fib_in_range(n):
    list = [2]
    a = 1
    b = 2
    while a+b < n:
        c = a+b
        if c%2 == 0:
            list.append(c)
        a = b
        b = c

    return list

print(sum(list_even_fib_in_range(4000000)))