class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def maxDepth(self,root):
        q=deque()
        q.append((root,1))
        l=1
        ans=1
        while q :
            node,l = q.popleft()
            ans=l
            if node.left :
                q.append((node.left,l+1))
            if node.right :
                q.append((node.right,l+1))
        return ans
