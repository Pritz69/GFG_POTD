class Solution:
    def toSumTree(self, root) :
        #code here
        if(root == None):
            return 0
        
        
        l = self.toSumTree(root.left)
        r = self.toSumTree(root.right)
        temp = root.data
        root.data = l+r
        return root.data+temp
