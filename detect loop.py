
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def method1(head):
    tmp=SinglyLinkedListNode(0)
    while(head):
        if(head==tmp):
            return 1
        tmp2=head.next
        head.next=tmp
        head=tmp2
    return 0 
def method2(head):
    slow=fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return 1
    return 0
def detectandremove(head):
    slow=fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            break
    
    if(slow!=fast):
        print("no loop")
        return
    slow=head
    while(fast.next!=slow.next):
        fast=fast.next
        slow=slow.next
    fast.next=None

