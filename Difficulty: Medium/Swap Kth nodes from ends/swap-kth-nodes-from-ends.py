'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # code here
        n=0
        curr=head
        while curr :
            n +=1
            curr=curr.next
        a,b=0,0
        c=0
        curr=head
        while curr :
            c +=1
            if c==k :
                a=curr.data
            if c==(n-k)+1 :
                b=curr.data
            curr=curr.next
        c=0
        curr=head
        while curr :
            c +=1
            if c==k :
                curr.data=b
            if c==(n-k)+1 :
                curr.data=a
            curr=curr.next
        return head
