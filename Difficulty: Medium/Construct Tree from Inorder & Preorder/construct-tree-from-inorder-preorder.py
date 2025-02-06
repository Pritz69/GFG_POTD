#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        index_map = { inorder[i] : i for i in range(len(inorder)) }
        pre_inx = 0
        
        def construct(left , right):
            nonlocal pre_inx
            if left> right:
                return None
            
            val = preorder[pre_inx]
            pre_inx+=1
            inorder_inx = index_map[val]
            root = Node(val)
            root.left = construct(left , inorder_inx-1)
            root.right = construct(inorder_inx+1,right)
            
            return root            
            
        return construct(0,len(inorder)-1)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends