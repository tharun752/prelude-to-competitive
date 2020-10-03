import math
def gpf(n):
    while(n%2==0):
        print("2",end=" ")
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            print(i,end=" ")
            n//=i
    if(2<n):
        print(n)
for _ in range(int(input())):
    gpf(int(input()))