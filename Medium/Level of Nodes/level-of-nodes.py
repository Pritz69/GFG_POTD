#User function Template for python3
from collections import deque

class Solution:
    
    # Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        q = deque()
        q.append(0)
        level = 0
        vis=[0]*V
        vis[0]=1
        while q:
            level_size = len(q)  # Get the number of nodes at the current level
            
            for i in range(level_size):
                v = q.popleft()
                if v == X:
                    return level
                
                for neighbor in adj[v]:
                    if vis[neighbor]==0 :
                        vis[neighbor]=1
                        q.append(neighbor)
            
            level += 1
        
        return -1  # If X is not found, return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends