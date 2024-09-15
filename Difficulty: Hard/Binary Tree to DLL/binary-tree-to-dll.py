#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def __init__(self):
        self.prev = None  # Previous node in DLL
        self.head = None  # Head of the DLL
    
    def bToDLL(self, root):
        # Helper function to convert binary tree to DLL using in-order traversal
        def convert_to_dll(node):
            if not node:
                return
            
            # Traverse the left subtree
            convert_to_dll(node.left)
            
            # Process the current node
            if self.prev is None:
                # Current node is the leftmost node, which will be the head of DLL
                self.head = node
            else:
                # Link the current node with the previous node
                node.left = self.prev
                self.prev.right = node
            
            # Update prev to the current node
            self.prev = node
            
            # Traverse the right subtree
            convert_to_dll(node.right)
        
        # Initialize conversion
        convert_to_dll(root)
        
        # Return the head of the DLL
        return self.head

#{ 
 # Driver Code Starts
#Initial template for Python

from collections import deque
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


import sys            
def printDLL(head): #Print util function to print Linked List
    prev = None
    sys.stdout.flush()
    while(head != None):
        print(head.data, end=" ")
        prev=head
        head=head.right
    print('')
    while(prev != None):
        print(prev.data, end=" ")
        prev=prev.left
    print('')
    
if __name__=='__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        head = ob.bToDLL(root)
        printDLL(head)
# } Driver Code Ends