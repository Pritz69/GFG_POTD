from collections import deque
class Solution:
    def maxLevelSum(self, root):
        # Code here
        q=deque()
        max_sum=-float('inf')
        q.append(root)
        while q:
            curr_sum=0
            n=len(q)
            for i in range(n):
                curr=q.popleft()
                curr_sum+=curr.data
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            max_sum=max(curr_sum, max_sum)
        return max_sum
