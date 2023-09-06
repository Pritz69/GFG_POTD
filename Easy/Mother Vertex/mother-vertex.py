
class Solution:
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		#Code here
		def dfs(i, vis):
            vis[i] = True
            for x in adj[i]:
                if not vis[x]:
                    dfs(x, vis)

        vis = [False] * V
        mother = -1

        # Find the last visited vertex during DFS traversal
        for i in range(V):
            if not vis[i]:
                dfs(i, vis)
                mother = i

        # Check if the mother vertex is indeed a mother vertex
        check = [False] * V
        dfs(mother, check)
        for i in check:
            if i is False:
                return -1

        return mother









#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends