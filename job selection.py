class fun:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __lt__(self,temp):
            if(self.end==temp.end):
                return self.start<temp.start
            return self.end<temp.end
        

n=int(input())
start=list(map(int,input().split()))
end=list(map(int,input().split()))
a=[]
for i in range(n):
    temp=fun(start[i],end[i])
    a.append(temp)
a.sort()
cnt=1
temp=a[0].end
# for i in range(n):
#     print(a[i].start,a[i].end)
for i in range(1,n):
    if(temp<=a[i].start):
        cnt+=1
        temp=a[i].end
print(cnt)


