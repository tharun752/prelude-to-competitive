# # class Node:
# #     def __init__(self,data):
# #         self.data=data
# #         self.next=None
# # def insertbegin(head,data):
# #     temp=Node(data)
# #     temp.next=head
# #     return temp
# # def insertend(head,data):
# #     if(head==None):
# #         head=Node(data)
# #     while(head.next):
# #         head=head.next
# #     head.next=Node(data)
# # def deletebegin(head):
# #     if(head==None):
# #         print(-1)
# #         return None
# #     if(head.next==None):
# #         return None
# #     head=head.next
# #     return head
# # def deletelast(head):
# #     prev=head
# #     if(head==None):
# #         print(-1)
# #         return
# #     if(head.next==None):
# #         head=None
# #         return head
# #     while(head.next.next):
        
# #         head=head.next
# #     head.next=None
# #     return prev
# # def search(head,ele):
# #     pos=1
# #     while(head):
# #         if(head.data==ele):
# #             print(pos)
# #             break
# #         else:
# #             pos+=1
# #             head=head.next
# #     print(-1)
# # def searchrecursive(head,ele):
# #     if(head==None):
# #         print(-1)
# #     if(head.data==ele):
# #         return 1
# #     re=searchrecursive(head.next,ele)
# #     if(re==-1):
# #         return -1
# #     else:
# #         return re+1
# # def middleele(head):
# #     cnt=0
# #     curr=head
# #     while(head):
# #         cnt+=1
# #         head=head.next
# #     for i in range(0,cnt//2):
# #         curr=curr.next
# #     print(curr.data)
# # def midlleeleefficient(head):
# #     slow=fast=head
# #     while(fast and fast.next):
# #         slow=slow.next
# #         fast=fast.next.next
# #     print(slow.data)
# # def nthfromend(head,n):
# #     cnt=0
# #     curr=head

# #     while(head):
# #         cnt+=1
# #         head=head.next
# #     if(n>cnt):
# #         print(-1)
# #         return
# #     for i in range(0,cnt-n):
# #         curr=curr.next
# #     print(curr.data)
# # def nthfromendefficient(head,n):
# #     fast=slow=head
# #     for i in range(0,n):
# #         if(fast==None):
# #             print(-1)
# #             return
# #         fast=fast.next
# #     while(fast):
# #         slow=slow.next
# #         fast=fast.next
# #     print(slow.data)

# # def reversalll(head):
# #     prev=None
# #     curr=net=head
    
# #     while(curr):
# #         net=curr.next
# #         curr.next=prev
# #         prev=curr
        
# #         curr=net
# #     return prev
# # def recursive(head,prev):
# #     if(head==None):
# #         return prev
# #     tmp=head.next
# #     head.next=prev
# #     prev=head
# #     head=tmp
# #     return recursive(head,prev)
# # def reverserecursive(head):
# #     prev=None
# #     return recursive(head,prev)


# # def prinll(head):
    
# #     while(head): 
# #         print(head.data,end=" ")
# #         head=head.next
# #     print()

# # head=None
# # head=insertbegin(head,4)
# # head=insertbegin(head,5)
# # insertend(head,3)

# # insertend(head,3)
# # head=insertbegin(head,1)

# # # prinll(head)
# # # print()
# # # head=deletebegin(head)
# # # prinll(head)
# # # print()
# # # head=deletelast(head)
# # prinll(head)
# # head=reversalll(head)
# # # print(head.data,head.next.data,head.next.next.data,head.next.next.next.data,head.next.next.next.next.next.data)
# # prinll(head)
# # head=reverserecursive(head)
# # prinll(head)
# # # # head=deletelast(head)
# # print()

# # # nthfromendefficient(head,3)


# # class Node:
# #     def __init__(self,data):
# #         self.data=data
# #         self.next=None
# # def insertbegin(head,data):
# #     if(head==None):
# #         head=Node(data)
# #         return head
# #     temp=Node(data)
# #     temp.next=head
# #     return temp
# # for _ in range(int(input())):
# #     head=None
# #     head1=None
# #     head2=None
# #     n=int(input())
# #     l=list(map(int,input().split()))
# #     for i in l:
# #         head=insertbegin(head,i)
# #     while(head):
# #         if(head.data%2):
# #             head1=insertbegin(head1,head.data)
# #             # print(head1.data,end=" ")
# #         else:
# #             head2=insertbegin(head2,head.data)
# #             # print(head2.data,end=" ")
# #         head=head.next
# #     curr=head2
# #     while(curr.next):
# #         curr=curr.next
# #     curr.next=head1
# #     while(head2):
# #         print(head2.data,end=" ")
# #         head2=head2.next

# # class Node:
# #     def __init__(self,key,data):
# #         self.key=key
# #         self.data=data
# #         self.next=None
# #         self.prev=None


# # class LRUCache:
# #     def __init__(self,cap):
# #         self.cap=cap
# #         self.head=None
# #         self.tail=None
# #         self.hashtable=dict()
     
    
# #     def addnode(self,key,data):
# #         head=self.head
# #         tail=self.tail
# #         tmp=Node(key,data)
# #         if(head==None):
# #             head=tmp
# #             tail=tmp
# #             return head,tail
# #         tmp.next=head
# #         head.prev=tmp
        
# #         self.head=tmp
# #         self.tail=tail
         
# #         self.hashtable[key]=self.head
# #     def deleteNode(self,node):
        
        

# #         node.prev.next=node.next
# #         node.next.prev=node.prev
# #     def get(self,key):
# #         if(key in self.hashtable):
# #             re=self.hashtable[key]
# #             return re.data
# #         else:
# #             return -1
# #     def set(self,key,value):
# #         if(key in self.hashtable):
# #             re=self.hashtable[key] 
# #             self.deleteNode(re)
# #             self.addnode(key,value)
# #         else:
# #             if(self.cap):
# #                 self.cap-=1
# #                 self.addnode(key,value)
# #             else:
# #                 if(self.tail.prev==None):
# #                     self.head=self.tail=None
# #                 else:

# #                     self.tail.prev.next=None
# #                     self.tail=self.tail.prev
# #                     self.addnode(key,value)


# # for _ in range(int(input())):
# #     x,y=map(int,input().split())
# #     if(x==y):
# #         print(2*x)
# #     elif((x%2==0 and y%2==1) or (x%2==1 and y%2==0)):
# #         if(max(x,y)%2):
# #             print(2*min(x,y)+1)
# #         else:
# #             print(2*max(x,y)-1)
# #     elif(x%2 and y%2):
# #         print(2*max(x,y)-1)
# #     else:
# #         print(2*max(x,y)-1)
# def merge(arr, l, m, r): 
#     n1 = m - l + 1
#     n2 = r- m 
  
#     # create temp arrays 
#     L = [0] * (n1) 
#     R = [0] * (n2) 
  
#     # Copy data to temp arrays L[] and R[] 
#     for i in range(0 , n1): 
#         L[i] = arr[l + i] 
  
#     for j in range(0 , n2): 
#         R[j] = arr[m + 1 + j] 
  
#     # Merge the temp arrays back into arr[l..r] 
#     i = 0     # Initial index of first subarray 
#     j = 0     # Initial index of second subarray 
#     k = l     # Initial index of merged subarray 
  
#     while i < n1 and j < n2 : 
#         if L[i] <= R[j]: 
#             arr[k] = L[i] 
#             i += 1
#         else: 
#             arr[k] = R[j] 
#             j += 1
#         k += 1
  
#     # Copy the remaining elements of L[], if there 
#     # are any 
#     while i < n1: 
#         arr[k] = L[i] 
#         i += 1
#         k += 1
  
#     # Copy the remaining elements of R[], if there 
#     # are any 
#     while j < n2: 
#         arr[k] = R[j] 
#         j += 1
#         k += 1
  
# # l is for left index and r is right index of the 
# # sub-array of arr to be sorted 
# def mergeSort(arr,l,r): 
#     if l < r: 
  
#         # Same as (l+r)//2, but avoids overflow for 
#         # large l and h 
#         m = (l+(r-1))//2
  
#         # Sort first and second halves 
#         mergeSort(arr, l, m) 
#         mergeSort(arr, m+1, r) 
#         merge(arr, l, m, r) 
  
  
# # Driver code to test above 
# arr = [12, 11, 13, 5, 6, 7] 
# n = len(arr) 
# print ("Given array is") 
# for i in range(n): 
#     print ("%d" %arr[i]), 
  
# mergeSort(arr,0,n-1) 
# print ("\n\nSorted array is") 
# for i in range(n): 
#     print ("%d" %arr[i])

# a,b=map(int,input().split())
# c,v=map(int,input().split())
# print(a*v-b*c)

# n,x=map(int,input().split())
# s=input()
# for i in s:
#     if(i=='o'):
#         x+=1
#     else:
#         if(x==0):
#             continue
#         else:
#             x-=1
# print(x)



            
            


# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# if(x1%2==y1%2):
# def lomutopartition(arr:list,low,high):
#     i=low-1
#     pivot=arr[high]
    
    
#     for j in range(low,high+1):
#         if(arr[j]<=pivot):
#             i+=1
        
#             arr[i],arr[j]=arr[j],arr[i]
#     # print(arr,low,high)
#     return i
# def kthSmallest(arr, l, r, k):
#     l=0
#     r=r
#     while(l<=r):
#         p=lomutopartition(arr,l,r)
#         print(p)
#         if(p==k-1):
#             return arr[p]
#         if(p>k-1):
#             r=p-1
#         elif(p<k-1):
#             l=p+1
#     return -1

# arr=list(map(int,input().split()))
# kthSmallest(arr,0,len(arr)-1,3)
    
# def maxEvents( events):
#         events.sort(key=lambda events:events[1])
#         curr=1
#         res=0
#         arr=[0]*(events[-1][-1]+1)
#         events.sort(key=lambda events:events[0])
#         for i in events:
        
#             for j in range(i[1],i[0]-1,-1):
#                 if(arr[j]==0):
#                     arr[j]=1
#                     res+=1
#                     break
#         print(res)
#         return res
# maxEvents([[1,2],[2,2],[3,3],[3,4],[3,4]])
def minSwaps(arr, N):
    visited=[False for i in range(N+1)]
    arrplace=[*enumerate(arr)]
    arrplace.sort(key=lambda x: x[1])
    re=0
    for j in range(N):
        if(visited[j] or arrplace[j][0]==j):
            continue
        cyclesize=0
        i=j
        while not visited[i]:
            visited[i]=True
            i=arrplace[i][0]
            
            cyclesize+=1
        re+=cyclesize-1
    print(re)
arr=list(map(int,input().split()))
minSwaps(arr,len(arr))
