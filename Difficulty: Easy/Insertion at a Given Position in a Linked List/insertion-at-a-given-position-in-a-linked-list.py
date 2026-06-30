'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
      # code here
        #pos=pos-1
        newn=Node(val)
        if pos==1 :
          newn.next=head
          return newn
        c=0
        curr=head
        while curr is not None and c < pos-2 :
            c +=1
           # print(c,curr.data)
            curr=curr.next
        
        if curr is None :
            return head
        
        newn.next=curr.next
        curr.next=newn
        return head
      