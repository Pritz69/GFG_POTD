'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        ans=-1
        def inord(node) :
            nonlocal ans
            if not node :
                return None
            inord(node.left)
            if node.data <= k :
                ans=node.data
            inord(node.right)
        
        inord(root)
        return ans