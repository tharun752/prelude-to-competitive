for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    mxsub=[0]*len(l)
    mxsub[0]=l[0]
    mx=l[0]
    for i in range(1,len(l)):
        mxsub[i]=max((mxsub[i-1]+l[i]),l[i])
    for j in range(1,len(l)):
        mx=max(l[j]+mx,mx)

    print(max(mxsub),mx)