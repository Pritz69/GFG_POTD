from functools import lru_cache
class Solution:
	def getCount(self, n):
	    
	    @lru_cache(None)
	    def helper(i,j,cnt):
	        if i<0 or j<0 or i>=4 or j>=3 or board[i][j] is None:
	            return 0
	        if cnt==1:
	            return 1
	        res=0
	        res+=helper(i,j,cnt-1)
	        res+=helper(i-1,j,cnt-1)
	        res+=helper(i+1,j,cnt-1)
	        res+=helper(i,j-1,cnt-1)
	        res+=helper(i,j+1,cnt-1)
	        return res
	    
		board=[[1,2,3],[4,5,6],[7,8,9],[None,0,None]]
		res=0
		for i in range(4):
		    for j in range(3):
		        res+=helper(i,j,n)
		return res