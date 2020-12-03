class jobsequence:
    def __init__(self,id,deadline,profit):
        self.id=id
        self.deadline=deadline
        self.profit=profit
    def __gt__(self, other):
        if(self.profit==other.profit):
            return self.deadline<other.deadline
        return self.profit < other.profit



n=int(input())
ids=[]
mx=0
for i in range(0,n):
    a,b,c=map(int,input().split())
    temp=jobsequence(a,b,c)
    ids.append(temp)
    if(b>mx):
        mx=b
ids.sort()

a=[0]*(mx+1)
pro=0
cnt=0
re=[0]*(mx+1)
for i in ids:
    for j in range(i.deadline,0,-1):
        if(a[j]==0):
            re[j]=i.id
            a[j]=1
            pro+=i.profit
            cnt+=1
            break
for i in re:
    if(i!=0):
        print(i,end=" ")