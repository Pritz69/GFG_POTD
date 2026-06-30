"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def insertAtFront(self, head, x):
        #code here
        newnode=Node(x)
        newnode.next=head
        head=newnode
        return head
