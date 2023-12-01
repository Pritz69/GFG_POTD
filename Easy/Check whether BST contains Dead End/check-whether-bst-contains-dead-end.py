# Your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isDeadEnd(self, root):
        # Code here
        l=[('N',0)]
        def rec(node) :
            if not node :
                return
            rec(node.left)
            if not node.left and not node.right :
                l.append(('l',node.data))
            else :
                l.append(('N',node.data))
            rec(node.right)
        rec(root)
        for i,x in enumerate(l) :
            if x[0]=='l' :
                if i+1<len(l) and x[1]==l[i-1][1]+1 and x[1]==l[i+1][1]-1 :
                    return True
        return False
                

#{ 
 # Driver Code Starts

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
                
        ob = Solution()
        if ob.isDeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends