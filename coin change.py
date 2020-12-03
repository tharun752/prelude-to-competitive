required=int(input())
nocoins=int(input())
coins=list(map(int,input().split()))
a=[[0]*(required+1) for _ in range(nocoins+1)]
for i in range(required+1):
    
    a[0][i]=999
for j in range(nocoins+1):
    a[j][0]=0
#print(a)
for i in range(1,nocoins+1):
    for j in range(1,required+1):
        if(coins[i-1]>j):
            a[i][j]=a[i-1][j]
        else:
            #print("ghhgh",a[i-1][j],1+a[i][j-coins[i-1]])
            a[i][j]=min(a[i-1][j],1+a[i][j-coins[i-1]])
        #print((i,j),a[i][j])
print(a)
print(a[-1][-1])
