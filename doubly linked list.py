class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insertbegin(head,tail,data):
    tmp=Node(data)
    if(head==None):
        head=tmp
        tail=tmp
        return head,tail
    tmp.next=head
    head.prev=tmp
    
    return tmp,tail
def insertend(head,tail,data):
    tmp=Node(data)
    if(head==None):
        head=tmp
        tail=tmp
        return head,tail
    tail.next=tmp
    tmp.prev=tail
    
    return head,tmp
def deletebegin(head,tail):
    if(head==None):
        print(-1)
        return head,tail
    if(head.next==None):
        head=tail=None
        return head,tail

    head.next.prev=None
    head=head.next
    return head,tail

def deletelast(head,tail):
    if(head==None):
        print(-1)
        return head,tail
    if(head.next==None):
        head=tail=None
        return head,tail
    tail.prev.next=None
    tail=tail.prev
    
    return head,tail


def prinll(head):
    
    while(head): 
        print(head.data,end=" ")
        head=head.next
head=None
tail=None
head,tail=insertbegin(head,tail,4)
head,tail=insertbegin(head,tail,5)
head,tail=insertbegin(head,tail,6)

head,tail=insertend(head,tail,8)
prinll(head)
print()
head,tail=deletebegin(head,tail)
prinll(head)
print()
# print(head.data,head.next.data,tail.data,tail.prev.data)
head,tail=deletelast(head,tail)
prinll(head)

