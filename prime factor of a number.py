import math
import math 
from sys import stdin, stdout 

 
def gpf (n): 
    cnt=0
    maxPrime = -1

    while n % 2 == 0: 
        cnt+=1
        maxPrime = 2
        n >>= 1    

    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i
            cnt+=1 
            n = n / i 

    if n > 2: 
        cnt+=1
        maxPrime = n 
      
    return maxPrime,cnt

n,p=map(int,input().split())
l=[int(x) for x in stdin.readline().rstrip().split()]
l.sort(reverse=True)

re=0
mxc=0
a={}
for i in l:
    mx,cnt=gpf(i)
    if(mx<=p):
        a[i]=cnt

for i in a:
    # print(i,a[i])
    if(a[i]>mxc):
        re=i
        mxc=a[i]
if(re==0):
    print(-1)
else:
    print(re)

