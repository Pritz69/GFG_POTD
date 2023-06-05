#User function Template for python3

# Tree Node
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.
    def minDiff(self,root, K):
        # code here
        global ans
        ans=float('inf')
        def inorder_traverse(root):
            global ans
            if root is None:
                return
            inorder_traverse(root.left)
            ans = min(ans, abs(K - root.data))
            inorder_traverse(root.right)
        
        inorder_traverse(root)
        return ans
