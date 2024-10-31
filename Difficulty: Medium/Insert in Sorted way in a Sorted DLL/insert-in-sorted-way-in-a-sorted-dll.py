#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        
    #code here
        if x <=head.data :
            node=Node(x)
            node.next=head
            head.prev=node
            head=node
            return head
        curr=head
        while curr.next and not( curr.data <= x and x<=curr.next.data) :
            curr=curr.next
        if curr.next is None :
            node=Node(x)
            curr.next=node
            node.prev=curr
        else :
            nxt=curr.next
            node=Node(x)
            curr.next=node
            node.next=nxt
            node.next.prev=node
            node.prev=curr
        return head

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends