
from collections import deque

class Solution:
    def isDeadEnd(self, root):
        dq=deque([root])
        seen={0} 
        leaves=set()
        while(dq):
            curr=dq.popleft()
            seen.add(curr.data)
            if not curr.left and not curr.right:
                leaves.add(curr.data)
            else:
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        for leaf in leaves:
            if leaf-1 in seen and leaf+1 in seen:
                return True
        return False