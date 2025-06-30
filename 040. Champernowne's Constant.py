N=1000000

num = "0."+"".join(map(str,list(range(1,N))))

print(int(num[2]) * int(num[11]) * int(num[101]) * int(num[1001]) * int(num[10001]) * int(num[100001]) * int(num[1000001]))