import math 

den=1
num=1

for d in range(11,100):
    d_list=list(str(d))
    for n in range(10,d):
        x=n/d
        n_list=list(str(n))
        if "0" in n_list and "0" in d_list:
            break
        else:
            for number in d_list:
                if number in n_list:
                    n_list.remove(number)
                    removed=number
                    d_list.remove(removed)
            if int(d_list[0])!=0:
                gcd=math.gcd(int(n_list[0]),int(d_list[0]))
                y=int(n_list[0])/int(d_list[0])
                if x==y and len(d_list)==1:
                    num=num*int(n_list[0])/gcd
                    den=den*int(d_list[0])/gcd
                    print("{}/{}={}/{}={}".format(n,d,n_list[0],d_list[0], x))
            d_list=list(str(d))

print("{}/{}".format(int(int(num)/math.gcd(int(num),int(den))), int(int(den)/math.gcd(int(num),int(den)))))