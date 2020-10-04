import math
def gpf(n):
    

    while(n%2==0):
        return 2
    for i in range(3,int(math.sqrt(n))+1,2):
    
        while(n%i==0):
            return i
    if(2<n ):
        return n
    
for _ in range(int(input())):
    num=int(input())
    k=int(input())
    if(gpf(num)>=(k)):
        print("Yes k-jagged")
    else:
        print("NO")