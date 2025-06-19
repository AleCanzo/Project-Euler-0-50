

def is_palindrome(n):
    n_list=list(str(n))
    while len(n_list)!=0:
        if n_list[0]==n_list[-1]:
            if len(n_list)==1:
                return True
            del n_list[0]
            del n_list[-1]
        else:
            return False
    return True


N=1000000
sum=0

for n in range(N):
    if is_palindrome(n) and is_palindrome(int(str(bin(n))[2:len(str(bin(n)))])):
        sum=sum+n
        
print(sum)