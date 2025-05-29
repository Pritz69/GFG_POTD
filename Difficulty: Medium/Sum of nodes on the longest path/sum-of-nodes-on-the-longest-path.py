'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''

from collections import deque

class Solution:
    def sumOfLongRootToLeafPath(self, root):
        max_sum, max_length, queue = 0, 0, deque()
        queue.append([root, 1, root.data])  # [node, length, current_sum]
        
        while queue:
            node, length, current_sum = queue.popleft()
            
            # Check if leaf node
            if not node.left and not node.right:
                # Update max_sum and max_length if needed
                if (max_length < length) or (max_length == length and max_sum < current_sum):
                    max_length, max_sum = length, current_sum
                continue
            
            # Add left child to the queue
            if node.left:
                queue.append([node.left, length + 1, current_sum + node.left.data])
            
            # Add right child to the queue
            if node.right:
                queue.append([node.right, length + 1, current_sum + node.right.data])
        
        return max_sum