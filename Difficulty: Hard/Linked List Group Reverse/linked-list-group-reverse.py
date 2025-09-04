"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        if not head or k == 1:
            return head

        dummy = Node(0)
        new_tail = dummy
        current = head

        while current:
            # Step 1: Collect up to k nodes into a temporary list
            count = 0
            temp_values = []
            temp_node = current
            while temp_node and count < k:
                temp_values.append(temp_node.data)
                temp_node = temp_node.next
                count += 1

            # Step 2: Reverse the values (even if less than k, still reverse)
            temp_values.reverse()

            # Step 3: Create a new linked list for this chunk
            for val in temp_values:
                new_tail.next = Node(val)
                new_tail = new_tail.next

            # Step 4: Move pointer for next group
            current = temp_node

        return dummy.next