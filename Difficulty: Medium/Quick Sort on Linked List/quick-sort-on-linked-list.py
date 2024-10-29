#User function Template for python3
def quickSort(head):
    if not head or not head.next:
        return head  

    def partition(start, end):
        pivot, prev = start, None
        curr = start
        tail = pivot

        while curr != end:
            if curr.data < pivot.data:
                if prev:
                    prev.next = curr.next
                curr.next = start
                start = curr
                curr = prev.next if prev else tail.next
            else:
                prev = curr
                curr = curr.next
        return pivot, start, tail

    def quickSortRecur(start, end):
        if start == end or not start:
            return start
        pivot, left_head, pivot_tail = partition(start, end)
        left_head = quickSortRecur(left_head, pivot)
        pivot_tail.next = quickSortRecur(pivot.next, end)
        return left_head

    return quickSortRecur(head, None)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def nodeID(head, dic):
    while head:
        dic[head.data].append(id(head))
        head = head.next


def printList(head, dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        dic = defaultdict(list)  # dictonary to keep data and id of node
        nodeID(ll.head, dic)  # putting data and its id

        resHead = quickSort(ll.head)
        printList(resHead, dic)  #verifying and printing
        print()

        print("~")

# } Driver Code Ends