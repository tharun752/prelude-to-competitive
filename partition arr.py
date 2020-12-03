def lomutopartition(arr:list,low,high):
    i=low-1
    pivot=arr[high]
    
    
    for j in range(low,high+1):
        if(arr[j]<=pivot):
            i+=1
        
            arr[i],arr[j]=arr[j],arr[i]
    # print(arr,low,high)
    return i
def hoarepartition(arr:list,l,h):
    i=0
    pivot=arr[l]
    j=h
    while(True):
        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i>=j):
        
            return j
            
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    
    
def quicksortusinglomuto(arr,l,h):
    if(l<h):
        p=lomutopartition(arr,l,h)
        print("left starts",p,l,p-1)
        quicksortusinglomuto(arr,l,p-1)
        print("right starts",p,p+1,h)
        quicksortusinglomuto(arr,p+1,h)
def quicksortusinghoare(arr,l,h):
    if(l<h):
        p=hoarepartition(arr,l,h)
        quicksortusinghoare(arr,l,p)
        quicksortusinghoare(arr,p+1,h)

    

arr=list(map(int,input().split()))

# lomutopartition(arr,0,6)
quicksortusinghoare(arr,0,len(arr)-1)
print(arr)