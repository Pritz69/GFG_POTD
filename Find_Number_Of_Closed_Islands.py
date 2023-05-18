class Solution:
	def closedIslands(self, matrix, N, M):
		#Code here
		visit=set()
		def dfs(r,c) :
		    if (r<0 or c<0 or r==N or c==M) :
		        return 0
		    if matrix[r][c]==0 or (r,c) in visit :
		        return 1
		    visit.add((r,c))
		    return min(dfs(r+1,c),dfs(r,c+1),dfs(r-1,c),dfs(r,c-1))
		    
		res =0
		for r in range(N) :
		    for c in range(M) :
		        if matrix[r][c]==1 and (r,c) not in visit :
		            res += dfs(r,c)
		return res
