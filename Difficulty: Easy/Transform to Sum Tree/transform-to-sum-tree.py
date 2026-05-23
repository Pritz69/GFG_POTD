''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        # code here
        def pre(node):
            if node is None:
                return 0

            return node.data + pre(node.left) + pre(node.right)

        def trav(node):
            if node is None:
                return

            original = node.data

            node.data = pre(node) - original

            trav(node.left)
            trav(node.right)

        trav(root)
        return root
            
        