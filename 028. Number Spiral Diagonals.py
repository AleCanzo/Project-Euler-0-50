import numpy as np
    
def move_right(M,x,y,n,N):
    Flag=False
    while Flag==False:
        if M[x][y+1]==0:
            n=n+1
            M[x][y+1]=n
            y=y+1
            return (n,x,y)    
        else:
            (n,x,y)=move_up(M,x,y,n,N)
    
def move_down(M,x,y,n,N):
    Flag=False
    while Flag==False:
        if M[x+1][y]==0:
            n=n+1
            M[x+1][y]=n
            x=x+1
            return (n,x,y)
        else:
            (n,x,y)=move_right(M,x,y,n,N)
            if n==pow(N,2):
                return (n,x,y)
    
def move_up(M,x,y,n,N):
    Flag=False
    while Flag==False:
        if M[x-1][y]==0:
            n=n+1
            M[x-1][y]=n
            x=x-1
            return (n,x,y)
        else:
            (n,x,y)=move_left(M,x,y,n,N)
            
def move_left(M,x,y,n,N):
    Flag=False
    while Flag==False:
        if M[x][y-1]==0:
            n=n+1
            M[x][y-1]=n
            y=y-1
            return (n,x,y)
        else:
            (n,x,y)=move_down(M,x,y,n,N)

def spiral_matrix(M,x,y,n,N):
    (n,x,y)=move_right(M,x,y,n,N)
    if x==0 and y==N-1:
        return (True, n, x, y)
        
    (n,x,y)=move_down(M,x,y,n,N)
    if x==0 and y==N-1:
        return (True, n, x, y)
            
    (n,x,y)=move_left(M,x,y,n,N)
    if x==0 and y==N-1:
        return (True, n, x, y)
           
    (n,x,y)=move_up(M,x,y,n,N)
    if x==0 and y==N-1:
        return (True, n, x, y)
    
    return (False, n, x, y)
    
    


N=1001
M=np.zeros((N,N), dtype=int)

#center
c=int((N-1)/2)
n=1
x=y=c
M[x][y]=n
Flag=False

while Flag==False:
    (Flag, n, x, y)=spiral_matrix(M,x,y,n,N)

sum=0
for i in range(N):
    sum=sum+M[i][i]
for i in range(N):
    sum=sum+M[(N-1)-i][i]

print(sum-1)