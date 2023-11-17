#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''

class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        head=None
        prev=None
        def inorder(curr) :
            nonlocal head,prev
            if curr is None :
                return 
            inorder(curr.left)
            
            if head is None :
                head=prev=curr
            else :
                prev.right=curr
                curr.left=prev
            
            prev=curr
            inorder(curr.right)
        
        inorder(root)
        head.left=prev
        prev.right=head
        return head
