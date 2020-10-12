for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    mx=-1
    temp=0
    for i in range(0,n):
        temp=temp+l[i]
        if(temp>mx):
            mx=temp
        if(temp<0):
            temp=0


    print(mx)