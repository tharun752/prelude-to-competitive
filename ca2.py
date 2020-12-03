# # import math 
 
# # def maxPrimeFactors (n): 

# #     maxPrime = -1

# #     while n % 2 == 0: 
# #         maxPrime = 2
# #         n >>= 1    

# #     for i in range(3, int(math.sqrt(n)) + 1, 2): 
# #         while n % i == 0: 
# #             maxPrime = i 
# #             n = n / i 

# #     if n > 2: 
# #         maxPrime = n 
      
# #     return int(maxPrime) 
# # def  setcheck(n): 
# #     count = 0
# #     while (n): 
# #         count += n & 1
# #         n >>= 1
# #     return count>=2 

# # n=int(input())
# # l=list(map(int,input().split()))
# # l.sort(reverse=True)
# # mx=0

# # for i in l:
# #     if(maxPrimeFactors(i*i+1)>=(2*i) and setcheck(i)):
# #         mx=i
# #         break
# # print(mx)

# class Node: 
   
    
#     def __init__(self, data): 
#         self.data = data   
#         self.next = None    
                          
   

# class LinkedList: 
 
#     def __init__(self):  
#         self.head = None
#     def pushstart(self,data):
#         if(self.head==None):
#             temp=Node(data)
#             self.head=temp
#         else:
#             temp=self.head
#             newnode=Node(data)
#             newnode.next=temp
#             self.head=newnode
#     def pushend(self,data):
#         if(self.head==None):
#             temp=Node(data)
#             self.head=temp
#         else:
#             temp=self.head
#             while(temp.next!=None):
#                 temp=temp.next
                
#             temp.next=Node(data)
#     def printfron(self):
#         if(self.head==None):
#             print(-1)
#         else:
#             print(self.head.data)
#     def printback(self):
#         if(self.head==None):
#             print(-1)
#         else:
#             temp=self.head
#             while(temp.next!=None):
#                 temp=temp.next
#             print(temp.data)
#     def removefront(self):
#         if(self.head==None):
#             print(-1)
#         else:
#             self.head=self.head.next
#     def removeback(self):
#         if(self.head==None):
#             print(-1)
#         else:
#             temp=self.head
#             if(not temp.next):
#                 temp = None
#                 return
#             while(temp.next and temp.next.next!=None):
#                 temp=temp.next
#             temp.next=None
#     def removemid(self):
#         if(self.head==None):
#             print(-1)
#         if(self.head.next==None):
#             self.head = None
#         slow=self.head
#         fast=self.head
#         prev=None
#         while(fast is not None and fast.next is not None):
#             fast=fast.next.next
#             prev=slow
#             slow=slow.next
        
#         prev.next=slow.next
#     def insertAtMid(self, x): 
  
#         if(self.head == None):  
#             self.head = Node(x) 
#         else: 
    
#             newNode = Node(x) 
    
#             ptr = self.head 
#             length = 0
#             count=0
#             while(ptr != None): 
#                 ptr = ptr.next
#                 length += 1

#             if(length % 2 == 0): 
#                 count = length / 2 
#             else: 
#                 (length + 1) / 2
    
#             ptr = self.head 

#             while(count > 1): 
#                 count -= 1
#                 ptr = ptr.next

#             newNode.next = ptr.next
#             ptr.next = newNode 
#     def printmiddle(self):
#         slow=self.head
#         fast=self.head
#         if(self.head is not None):
#             while(fast is not None and fast.next is not None):
#                 fast=fast.next.next
#                 slow=slow.next
#             print(slow.data)

#     def printll(self):
#         tmp=self.head
#         if(tmp):
#             while(tmp.next!=None):
#                 print(tmp.data,end=" ")
#                 tmp=tmp.next
#         print()
            
        

    

    
    
# a=LinkedList()
# head=0
# n=int(input())
# arr=list(map(int,input().split()))
# for i in arr:
#     a.insertAtMid(i)
    
# for i in range(int(input())):
#     l=list(map(int,input().split()))
#     if(l[0]==1):
#         a.insertAtMid(l[1])
#     if(l[0]==2):
#         a.removefront()
#     if(l[0]==3):
#         a.removeback()
#     if(l[0]==4):
#         a.removemid()
#     if(l[0]==5):
#         a.printfron()
#     if(l[0]==6):
#         a.printback()
#     if(l[0]==7):
#         a.printmiddle()
    
# n,q=map(int,input().split())
# l=list(map(int,input().split()))

# for i in range(1,n):

#     l[i]=l[i]+l[i-1]
# print(l)
# for i in range(q):

# #     x,y=map(int,input().split())
# #     if(x==1):


# #         print(l[y-1]//((y-x+1)))
# #     else:
# #         # print(l[y-1],l[x-2])
# #         print((l[y-1]-l[x-2])//(y-x+1))

# def largestRectangle(h):
#     stack=[]
#     maxarea=-1
#     i=0
#     while(i<len(h)):
#         if(not(stack) or h[stack[-1]]<=h[i]):
#             stack.append(i)
#             i+=1
            
#         else:
        
#             temp=stack.pop()
#             area=h[temp]*((i-stack[-1]-1) if stack else i)
#             maxarea=max(maxarea,area)
        
#     while(stack):
#         temp=stack.pop()
#         area=(h[temp]*((i-stack[-1]-1) if stack else i))
#         maxarea=max(maxarea,area)
#     return(maxarea)
        

# def make(M, rows, columns):
#     temp=[]
#     t=0
#     for i in range(columns):
#         t=0
#         for j in range(rows+1):
            
#             if(M[j][i]==0):
#                 t=0
#                 continue
#             t+=M[j][i]
#         temp.append(t)

#     return temp
        

# def maxRectangle(M, rows, columns):
    
#     re=[]
#     mx=-1
#     if(rows==1):
#         print(largestRectangle(M))
#     for row in range(rows):
#         re.append(make(M,row,columns))
#     print(re)
#     for i in re:
#         mx=max(mx,largestRectangle(i))
    


    
#     print(mx)

# k=[[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
# maxRectangle(k,4,4)
# import math

# for i in range(int(input())):
#     n=int(input())
#     if(n%2==0):
        
#         if(n==int(math.pow(2,int(math.sqrt(n))-2))):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         n=3*n+1
#         #print(n,int(math.pow(2,int(math.sqrt(n))-2)))
#         if(n==int(math.pow(2,int(math.sqrt(n))-2))):
#             print("YES")
#         else:
#             print("NO")
            

# def fun(n):
#     re=0
#     while(n!=0):
#         re=re+(n%10)
#         n=n//10
    
#     return re

# n=int(input())


# if(n%fun(n)==0):
#     print("YES")
# else:
#     print("NO")

# n=int(input())
# monster=list(map(int,input().split()))
# heroes=list(map(int,input().split()))
# re=0
# for i in range(n):
#     t=i
#     while(heroes[t]):
#         if(monster[t]-1>0):
# def make(n):
    
#     temp=[i for i in range(1,n+1)]
#     for i in range(1,n):
#         temp[i]=temp[i-1]+temp[i]
#     # print(temp)
#     return(temp)
# def fun(a,n,key):
#     s =0
#     e=n-1
    
#     while(s<=e):
#         mid = (s+e)//2
#         if(a[mid]==key):
            
#             return a[mid]
#         elif(a[mid]>key):
#             e = mid - 1 
#         else:
#             s = mid + 1
#     return a[e]
# n=int(input())
# k=list(map(int,input().split()))
# temp=make(n)
# mx=0
# # print(fun(temp,n,11))
# for i in range(1,n):
#     k[i]=k[i-1]+k[i]

# for i in range(n):

#     tar=n-i
#     r=fun(temp,n,tar)
#     if(i==0):
#         mx=max(mx,k[r-1])
#     else:
        
    
    
#     #print(i,i+r)
#     #print(sum(k[i:i+r]))
#         mx=max(mx,k[i+r-1]-k[i-1])

  

# print(mx)
# def make(s):
 
#     n = len(s)
#     answer = 0
#     prev = '-'
#     for i in range(0, n):
#         if (prev != s[i]):
#             prev = s[i]
#             answer += 1
         
#     return(answer)

# for i in range(int(input())):
#     n,q=map(int,input().split())
#     l=list(map(int,input().split()))
#     ans=make(l)
#     for j in range(q):
#         x,y=map(int,input().split())
#         temp=l[x-1]
#         l[x-1]=y
        # if(x==1):
        #     if(l[x-1]==l[x] and temp!=l[x]):
        #        ans=make(l)
        # elif(x==n):
        #     if(l[x-1]==l[x-2] and temp!=[x-2]):
        #         ans=make(l)
        
        # else:
        #     if((l[x-1]==l[x] or l[x-1]==l[x-2]) or (temp!=l[x-2] and temp!=[x-2])):
        #         ans=make(l)
            

        #print(make(l))
    
# def subsequence(strs,re,ex,index):
#     if(index==len(strs)):
#         re.append(ex)
#         return 
#     subsequence(strs,re,ex,index+1)
#     subsequence(strs,re,ex+[strs[index]],index+1)

# for _ in range(int(input())):
#     n=int(input())
#     strs=list(map(int,input().split()))    
#     re=[]
#     subsequence(strs,re,[],0)
#     mx=0
    
#     for i in re:
#         temp=sum(i)
#         #print(temp,i)
#         mx=mx|temp
#         #print(mx,"mx")
#     print(mx)

# def search(text, pat):

#         index=0
#         cnt=0
#         for i in text:

#                 if(cnt==len(pat)):
#                         break
                        
#                 if(i==pat[index]):
#                         index+=1
#                         cnt+=1
#                 else:
#                         index=0
                
#         if(cnt==len(pat)):
#                 return 1
#         else:
#                 return 0
# print(search(input(),input()))
for _ in range(int(input())):
    n=input()
    temp=""
    r=""
    for i in range(len(n)-1,-1,-1):
            if(n[i]=='.'):
                    temp+=r
                    temp+="."
                    r=""else:
                r=n[i]+r

                print(n[i],r,temp)
                print("------------")       
