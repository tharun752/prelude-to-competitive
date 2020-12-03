def sortedMerge(head1, head2):
    if(head2==None):
        return head1    
    if(head1==None):
        return head2
    head=None
    curr=None
    if(head1.data<=head2.data):
        head=head1
        curr=head
        head1=head1.next
    else:
        head=head2
        curr=head
        head2=head2.next
    while(head1 and head2):
        if(head1.data<=head2.data):
            head.next=head1
            head=head1
            head1=head1.next
        else:
            head.next=head2
            head=head2
            head2=head2.next
    if(head1==None and head2!=None):
        head.next=head2
    if(head1!=None and head2==None):
        head.next=head1
    return curr