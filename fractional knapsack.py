class knapsack:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.ratio=value/weight
    def __lt__(self,other):
        return self.ratio<other.ratio
for _ in range(int(input())):
    n,capacity=map(int,input().split())
    l=list(map(int,input().split()))
    arr=[]
    for i in range(0,len(l),2):
        arr.append(knapsack(l[i+1],l[i]))
    profit=0
    arr.sort(reverse=True)
    # for i in arr:
    #     print(i.weight,i.value,i.ratio)
    #print(arr[0].value)
    for i in arr:
        value=i.value
        itemweight=i.weight
        if(capacity-itemweight>0):
            capacity=capacity-itemweight
            profit+=value
        else:
            ratio=capacity/itemweight
            profit+=value*(ratio)
            capacity=int(capacity-(i.weight*ratio))
            break
    print("%.2f"%profit)
