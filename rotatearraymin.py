def fun(l,n):
    l=l[n::1]+l[:n:1]
    return l
def minfun(l,first,last):
    mid=(first+last)//2
    # if(first==last):
    #     return l[first]
    # if(mid==0 or mid==len(l)-1):
    #     return l[mid]
    # if(l[mid]<l[mid+1] and l[mid]<l[mid-1]):
    #     return l[mid]
    # else:
    #     return min(minfun(l,first,mid-1) ,minfun(l,mid+1,last))
    while(first<=last):
        mid=(first+last)//2
        # if(mid==0 or mid==n-1):
        #     return l[mid]
        if(l[mid]<l[mid+1] and l[mid]<l[mid-1]):
            return l[mid]
        if(l[mid+1]<l[mid]):
            first=mid+1
        elif(l[mid-1]<l[mid]):
            last=mid-1


    


for _ in range(int(input())):
    l=list(map(int,input().split()))
    n=int(input())
    l=fun(l,n)
    a=minfun(l,0,len(l)-1)
    print(a)