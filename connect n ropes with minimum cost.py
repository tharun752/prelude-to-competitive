for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    re=0
    tar=0
    while(len(l)!=1):
        l.sort()
        tmp1=l.pop(0)
        tmp2=l.pop(0)
        
        re=tmp1+tmp2
        tar+=re
        l.append(re)
        #print(l)
    print(tar)

