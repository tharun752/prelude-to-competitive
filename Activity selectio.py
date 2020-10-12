
for _ in range(int(input())):
    n=int(input())
    start=list(map(int,input().split()))
    finish=list(map(int,input().split()))
    finish,start=zip(*sorted(zip(finish,start)))
    # print(start,finish)
    i=0
    cnt=0
    for j in range(n):
        if(finish[i]<=start[j]):
            cnt+=1
            i=j
    print(cnt+1)


