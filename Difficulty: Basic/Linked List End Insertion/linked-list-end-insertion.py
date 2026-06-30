class Solution:
    def insertAtEnd(self, head, x):
        newnode = Node(x)

        # If list is empty
        if head is None:
            return newnode

        curr = head

        while curr.next is not None:
            curr = curr.next

        curr.next = newnode

        return head