class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertbegin(head,data):
    temp=Node(data)
    temp.next=head
    return temp
def insertend(head,data):
    if(head==None):
        head=Node(data)
    while(head.next):
        head=head.next
    head.next=Node(data)
def deletebegin(head):
    if(head==None):
        print(-1)
        return None
    if(head.next==None):
        return None
    head=head.next
    return head
def deletelast(head):
    prev=head
    if(head==None):
        print(-1)
        return
    if(head.next==None):
        head=None
        return head
    while(head.next.next):
        
        head=head.next
    head.next=None
    return prev
def search(head,ele):
    pos=1
    while(head):
        if(head.data==ele):
            print(pos)
            break
        else:
            pos+=1
            head=head.next
    print(-1)
def searchrecursive(head,ele):
    if(head==None):
        print(-1)
    if(head.data==ele):
        return 1
    re=searchrecursive(head.next,ele)
    if(re==-1):
        return -1
    else:
        return re+1
def middleele(head):
    cnt=0
    curr=head
    while(head):
        cnt+=1
        head=head.next
    for i in range(0,cnt//2):
        curr=curr.next
    print(curr.data)
def midlleeleefficient(head):
    slow=fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    print(slow.data)
def nthfromend(head,n):
    cnt=0
    curr=head

    while(head):
        cnt+=1
        head=head.next
    if(n>cnt):
        print(-1)
        return
    for i in range(0,cnt-n):
        curr=curr.next
    print(curr.data)
def nthfromendefficient(head,n):
    fast=slow=head
    for i in range(0,n):
        if(fast==None):
            print(-1)
            return
        fast=fast.next
    while(fast):
        slow=slow.next
        fast=fast.next
    print(slow.data)

def reversalll(head):
    prev=None
    curr=net=head
    
    while(curr):
        net=curr.next
        curr.next=prev
        prev=curr
        
        curr=net
    return prev
def recursive(head,prev):
    if(head==None):
        return prev
    tmp=head.next
    head.next=prev
    prev=head
    head=tmp
    return recursive(head,prev)
def reverserecursive(head):
    prev=None
    return recursive(head,prev)
def reversefirstkgroups(head,k):
    cnt=0
    prev=None
    curr=net=head
    
    while(curr and cnt!=k):
        net=curr.next
        curr.next=prev
        prev=curr
        cnt+=1
        curr=net
    print(prev.data)
    prev2=None
    while(curr ):
        net=curr.next
        curr.next=prev2
        prev2=curr
        curr=net
    head.next=prev2
    return prev
def recursivegroupreversal(head,k):

    cur=head
    prev=None
    cnt=0
    tmp=None
    resthead=None
    while(cur and cnt!=k):
        tmp=cur.next
        cur.next=prev
        prev=cur
        cur=tmp
        cnt+=1
    if(tmp!=None):
        resthead=recursivegroupreversal(tmp,k)
        head.next=resthead
    return prev



def kgroupsreversal(head,k):
    return recursivegroupreversal(head,k)
    


def prinll(head):
    
    while(head): 
        print(head.data,end=" ")
        head=head.next
    print()

head=None
head=insertbegin(head,4)
head=insertbegin(head,5)
insertend(head,3)

insertend(head,0)
head=insertbegin(head,1)
prinll(head)
# prinll(head)
# print()
# head=deletebegin(head)
# prinll(head)
# print()
# head=deletelast(head)
# prinll(head)
# head=reversalll(head)
# print(head.data,head.next.data,head.next.next.data,head.next.next.next.data,head.next.next.next.next.next.data)
# prinll(head)
# head=reverserecursive(head)
# prinll(head)
# # head=deletelast(head)
# print()
# head=reversefirstkgroups(head,6)
# prinll(head)
head=kgroupsreversal(head,2)
# print(head.next.next.data)
prinll(head)
# nthfromendefficient(head,3)


