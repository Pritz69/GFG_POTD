'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def mergeKLists(self, arr):
        # cod
        pq=[]
        for h in arr:
            heapq.heappush(pq,(h.data,h))
        head=Node(-1)
        tail=head
        while pq:
            _,node=heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq,(node.next.data,node.next))
            tail.next=node
            tail=tail.next
        return head.next
        