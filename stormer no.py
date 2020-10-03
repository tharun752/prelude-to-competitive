import math
def gpf(n):
    mx=0
    while(n%2==0):
        mx=2
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            mx=i
            n//=i
    if(2<n and mx<n):
        mx=n
    return mx
for _ in range(int(input())):
    num=int(input())
    if(gpf(num*num+1)>=(2*num)):
        print("Stormer no")
    else:
        print("NO")