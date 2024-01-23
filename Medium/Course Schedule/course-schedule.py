#User function Template for python3
from collections import defaultdict
class Solution:
    def findOrder(self, N, m, P):
        # Code here
        graph = defaultdict(list)
        for a, b in P: graph[a].append(b)
        res, visited = [], [0] * N

        def DFS(i):
            if visited[i]: return visited[i] == 1
            visited[i] = -1

            if any(not DFS(node) for node in graph[i]): return False
            visited[i] = 1
            res.append(i)
            return True

        return all(DFS(node) for node in range(N)) and res or []

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends