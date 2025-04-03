class Solution:
	    from collections import deque
    	def orangesRotting(self, mat):
    		rows,cols=len(mat),len(mat[0])
    		fresh_org=0
    		queue=self.deque()
    		for i in range(rows):
    		    for j in range(cols):
    	            if mat[i][j]==2:
                        queue.append((i,j))
    		        if mat[i][j]==1:
    		            fresh_org+=1
    		            
    		minutes_passed=0
    		vectors=[[0, 1], [0, -1], [1, 0], [-1, 0]]
    		while queue and fresh_org>0:
    		    minutes_passed+=1
    		    for _ in range(len(queue)):
    		        i,j=queue.popleft()
    		        for r_ele,c_ele in vectors:
    		            x,y=i+r_ele,j+c_ele
    		            if 0<=x<rows and 0<=y<cols and mat[x][y]==1:
    		                fresh_org-=1
    		                mat[x][y]=2
    		                queue.append((x,y))
    		                
            return minutes_passed if fresh_org==0 else -1

#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends