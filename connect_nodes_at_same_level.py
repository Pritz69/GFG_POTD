class Solution:
    def connect(self, root):
        # code here
        
        q = [root]
        while q:
            temp=[]
            for _ in range(len(q)):
                node = q.pop(0)
               
                if len(q)>0:
                    node.nextRight = q[0]
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q+=temp
        return root
