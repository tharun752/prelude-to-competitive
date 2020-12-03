def gcd(a,b):
    if(b==0):
        return a
    #print(a,b)
    return gcd(a,a%b)
arr=list(map(int,input().split()))
temp1=arr[0]
for i in range(1,len(arr)):
    
    re=gcd(temp1,arr[i])
    temp1=re
print(temp1)

