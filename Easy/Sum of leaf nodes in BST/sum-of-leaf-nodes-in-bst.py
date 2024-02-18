#User function Template for python3

##Structure of node
'''
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
'''

class Solution:
    def sumOfLeafNodes(self, root):
        #Your code here
        s=0
        def rec(root) :
            nonlocal s
            if not root :
                return
            if not root.left and not root.right :
                s += root.data
            rec(root.left)
            rec(root.right)
            
        rec(root)
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data=0):
        self.data=data
        self.left=None
        self.right=None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root

for _ in range(int(input())):
    root=None
    sizeOfArray=int(input())
    arr=[int(x) for x in input().strip().split()]
    for i in arr:
        root=newNode(root,i)
    ob = Solution()
    print(ob.sumOfLeafNodes(root))
# } Driver Code Ends