def insertionsort(l:list):
    #best case =O(n)
    #worst case=O(n^2) 
    for i in range(1,len(l)):
        j=i-1
        key=l[i]
        while(j>=0 and l[j]>key): 
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
    print(l)
def merge(arr,l,mid,r):
    n1=mid-l+1
    n2=r-mid
    left=[0]*n1
    right=[0]*n2
    
    for i in range(n1):
        left[i]=arr[l+i]
    for j in range(n2):
        right[j]=arr[mid+1+j]
    i=0
    j=0
    k=l  
    while(i<n1 and j<n2):
        if(left[i]<=right[j]):
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1
  
    while(i<n1):
        arr[k]=left[i]
        i+=1
        k+=1

    while(j<n2):
        arr[k]=right[j]
        j+=1
        k+=1

def mergesort(arr,l,r):
    # print(arr)
    #divide and conquer
    #O(nlogn) complexity
    #O(n) auxilary space
    #python uses timsort(mergesort +quicksort)
    if l<r: 
        mid=(l+r)//2
        mergesort(arr,l,mid)
        mergesort(arr,mid+1,r)
        merge(arr,l,mid,r)
def intersectionofsortedarray(arr1,arr2):
    re=[]
    i=0
    j=0
    while(i<len(arr1) and j<len(arr2)):
        if(i>0 and arr1[i]==arr1[i-1]):
            i+=1
            continue
        if(arr1[i]<arr2[j]):
            
            i+=1
        elif(arr1[i]>arr2[j]):
            
            j+=1
        else:
            re.append(arr1[i])
            i+=1
            j+=1
    # while(i<len(arr1)):
    #     re.append(arr1[i])
    #     i+=1
    # while(j<len(arr2)):
    #     re.append(arr2[j])
    #     j+=1
    print(re)
def unionofsortedarray(arr1,arr2):
    re=[]
    i=0
    j=0
    while(i<len(arr1) and j<len(arr2)):
        if(i>0 and arr1[i]==arr1[i-1]):
            i+=1
            continue
        if(j>0 and arr2[j]==arr2[j-1]):
            j+=1
            continue
        if(arr1[i]<arr2[j]):
            re.append(arr1[i])
            i+=1
        elif(arr1[i]>arr2[j]):
            re.append(arr2[j])
            j+=1
        else:
            re.append(arr1[i])
            i+=1
            j+=1
    while(i<len(arr1)):
        re.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        re.append(arr2[j])
        j+=1
    print(re)
def inversionmerge(arr,l,mid,r):
    n1=mid-l+1
    n2=r-mid
    left=[0]*n1
    right=[0]*n2
    
    for i in range(n1):
        left[i]=arr[l+i]
    for j in range(n2):
        right[j]=arr[mid+1+j]
    i=0
    j=0
    k=l  
    res=0
    while(i<n1 and j<n2):
        if(left[i]<=right[j]):
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1
            res+=(n1-i)
  
    while(i<n1):
        arr[k]=left[i]
        i+=1
        k+=1

    while(j<n2):
        arr[k]=right[j]
        j+=1
        k+=1
    return res

def inversions(arr,l,r):

    res=0
    if l<r: 
        mid=(l+r)//2
        res+=inversions(arr,l,mid)
        res+=inversions(arr,mid+1,r)
        res+=inversionmerge(arr,l,mid,r)
    return(res)
def countinversion(arr):
    print(inversions(arr,0,len(arr)-1))
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
    while(i<j):
        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i>j):
        
            return j
            
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
        print(arr)
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




def cyclesort(arr):
    pos=0
    item=arr[0]
    for i in range(0,len(arr)):
        item=arr[i]
        pos=i
        for j in range(i,len(arr)):
            if(arr[j]<item):
                pos+=1
        arr[pos],item=item,arr[pos]
        while(pos!=i):
            pos=i
            for j in range(i,len(arr)):
                if(arr[j]<item):
                    pos+=1
            arr[pos],item=item,arr[pos]
    print(arr)
# from collections import Counter
def countingsort(arr,k):
    counter=[0]*(k)
    re=[0]*len(arr)
    for i in arr:
        counter[i]+=1
    for i in range(1,k):
        counter[i]=counter[i-1]+counter[i]
    # print(arr,counter)
    for j in range(len(arr)-1,-1,-1):
        re[counter[arr[j]]-1]=arr[j]
        counter[arr[j]]-=1
    print(re)
    



#insertionsort(list(map(int,input().split())))
# arr=[1,2,3,4,5,6,5,4,3,2,1]
# mergesort(arr,0,len(arr)-1)
# print(arr)
# intersectionofsortedarray([3,5,10,10,10,15,15,20],[5,10,10,15,30])
# unionofsortedarray([3,8,10],[2,8,9,10,15])
# cyclesort([5,3,2,4,1])
arr=list(map(int,input().split()))
countingsort(arr,int(input()))