import math
def isPerfectSquare(n):
    x=math.sqrt(n)
    #print(index,x,math.floor(x),(x-math.floor(x))==0)
    return ((x-math.floor(x))==0)
def approach2(n):
    x=math.sqrt(n)
    return ((n+math.floor(0.5+x)))
for _ in range(int(input())):
    n=int(input())
    index=0
    count=1
    while(count<=n):
        index+=1
        if(not(isPerfectSquare(index))):
            count+=1
    print(approach2(n))
    print(index)
        
