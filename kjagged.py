import math
def gpf(n):
    mx=0
    bl=1
    while(n%2==0):
        mx=2
        bl=0
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        if(bl):
            while(n%i==0):
                mx=i
                break
                n//=i
    if(2<n and mx<n):
        mx=n
    return mx
for _ in range(int(input())):
    num=int(input())
    k=int(input())
    if(gpf(num)>=(k)):
        print("Yes k-jagged")
    else:
        print("NO")