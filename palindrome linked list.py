class Solution:
    def midll(self,head):
        slow=fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow,fast
    def reversalll(self,head):
        prev=None
        curr=net=head

        while(curr):
            net=curr.next
            curr.next=prev
            prev=curr

            curr=net
        return prev
    def isPalindrome(self, head: ListNode) -> bool:
        if(head==None):
            
            return 1
        slow,fast=self.midll(head)
        if(fast):
            slow=slow.next
        slow=self.reversalll(slow)
        fast=head
       
        bl=1
        
        while(slow):
            if(slow.val!=fast.val):
                bl=0
                break
            slow=slow.next
            fast=fast.next
        if(bl):
            return 1
        else:
            return 0