import inflect
p=inflect.engine()
sum=0
for i in range(1,1001):
    l=list(p.number_to_words(i))
    while "-" in l:
        l.remove("-")
    while " " in l:
        l.remove(" ")
    sum=sum+len(l)
print(sum)
    
    
