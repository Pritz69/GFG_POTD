#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution():
#Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self,head):
    #Your code here
        def getmid(head) :
            slow,fast=head,head.next
            while fast and fast.next  :
                slow=slow.next
                fast=fast.next.next
            mid=slow.next
            slow.next=None
            mid.prev=None
            return mid
            
        def merge(l1,l2) :
            if l1 is None :
                return l2
            if l2 is None :
                return l1
            dummy=Node(-1)
            tail=dummy
            while l1 and l2 :
                if l1.data < l2.data :
                    tail.next=l1
                    l1.prev=tail
                    l1=l1.next
                else :
                    l2.prev=tail
                    tail.next=l2
                    l2=l2.next
                tail=tail.next
            if l1 :
                l1.prev=tail
                tail.next=l1
            if l2 :
                l2.prev=tail
                tail.next=l2
            head=dummy.next
            head.prev=None
            return head
        if head is None or head.next is None :
            return head
        mid=getmid(head)
        l1=self.sortDoubly(head)
        l2=self.sortDoubly(mid)
        return merge(l1,l2)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends