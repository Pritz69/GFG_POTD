'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def findmid(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def merge(self,first,second):
        head=Node(-1)
        tail=head
        while first and second:
            if first.data<=second.data:
                tail.next=first
                first=first.next
            else:
                tail.next=second
                second=second.next
            tail=tail.next
        if first:
            tail.next=first
        if second:
            tail.next=second
        return head.next
    
    def mergeSort(self, head):
        if head.next:
            mid=self.findmid(head)
            first=head
            second=mid.next
            mid.next=None
            first=self.mergeSort(first)
            second=self.mergeSort(second)
            return self.merge(first,second)
        return head
        # code here
        