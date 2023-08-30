# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    # Code here
    if k==1 :
        head=head.next
        return head
    curr=head
    prev=curr
    p=1
    while (p<=k) :
        if p==k-1 :
            prev.next=curr.next.next
            break
        else :
            curr=curr.next
            prev=curr
        p +=1
    return head
        



