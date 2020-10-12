class jobsequence:
    def __init__(self,id,deadline,profit):
        self.id=id
        self.deadline=deadline
        self.profit=profit
    def __gt__(self, other):
        return self.profit < other.profit

for _ in range(int(input())):
    n=int(input())
    jobs=list(map(int,input().split()))
    ids=[]
    mx=0
    for i in range(0,n*3,3):
        a,b,c=jobs[i:i+3]
        temp=jobsequence(a,b,c)
        ids.append(temp)
        if(b>mx):
            mx=b
    ids.sort()
    # for i in ids:
    #     print(i.id,i.deadline,i.profit)

    a=[0]*(mx+1)
    pro=0
    cnt=0
    for i in ids:
        for j in range(i.deadline,0,-1):
            if(a[j]==0):
            
                a[j]=1
                pro+=i.profit
                cnt+=1
                break
    print(cnt,pro)
