
'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def reverse(self,head):
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

# 3 2 6 5 11 10 15 12

    def compute(self,head):
        head=self.reverse(head)
        curr=head
        while curr.next:
            if curr.data>curr.next.data:
                curr.next=curr.next.next
            else:
                curr=curr.next
        head=self.reverse(head)
        return head
                
