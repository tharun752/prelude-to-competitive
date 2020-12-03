class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertend(head,tail,data):
    if(head==None):
        head=tail=Node(data)
        return head,tail
    tmp=Node(data)
    tail.next=tmp
    tmp.next=head
    return head,tmp
def insertbegin(head,tail,data):
    if(head==None):
        head=tail=Node(data)
        return head,tail
    tmp=Node(data)
    tmp.next=head
    tail.next=tmp
    return tmp,tail
def deletebegin(head,tail):
    if(head==None):
        print(-1)
        return head,tail
    if(head.next==None):
        return None,None
    head=head.next
    tail.next=head
    return head,tail
def deleteend(head,tail):
    if(head==None):
        print(-1)
        return head,tail
    if(head.next==None):
        return None,None
    cur=head
    while(cur.next.next!=head):
        cur=cur.next
    
    cur.next=head
    tail=cur
    return head,tail
    
def deletek(head,tail,k):
    curr=head
    if(k==1):
        
        return deletebegin(head,tail)
    for i in range(0,k-2,1):
        
        head=head.next
    head.next=head.next.next
    if(head.next==curr):
        tail=head

    return curr,tail



def printll(head):
    tmp=head
    print(head.data,end=" ")
    head=head.next
    while(head!=tmp):
        print(head.data,end=" ")
        head=head.next
    print()

head=None
tail=None
head,tail=insertend(head,tail,4)
head,tail=insertend(head,tail,5)
head,tail=insertend(head,tail,6)
head,tail=insertend(head,tail,7)
head,tail=insertbegin(head,tail,1)
head,tail=insertbegin(head,tail,2)
head,tail=insertbegin(head,tail,3)
printll(head)
head,tail=deletebegin(head,tail)
printll(head)
head,tail=deletek(head,tail,5)


printll(head)

     