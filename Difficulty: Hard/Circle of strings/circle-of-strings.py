#User function Template for python3
class Solution:
    def isCircle(self, arr):
        from collections import defaultdict, Counter
        
        # Step 1: Graph Construction
        # g will store the graph as an adjacency list
        # indegree and outdegree will count the in-degrees and out-degrees of characters
        g = defaultdict(list)
        indegree = Counter()
        outdegree = Counter()

        # Build the graph and compute in-degrees and out-degrees
        for s in arr:
            start = s[0]  # First character (source)
            end = s[-1]   # Last character (destination)
            g[start].append(end)
            outdegree[start] += 1
            indegree[end] += 1

        # Step 2: Check if in-degree and out-degree of every character are equal
        if indegree != outdegree:
            return 0

        # Step 3: Check if the graph is strongly connected using DFS
        visited = set()
        
        # DFS function to visit nodes
        def dfs(node, g):
            if node in visited:
                return
            visited.add(node)
            for neighbor in g[node]:
                dfs(neighbor, g)

        # Start DFS from the first character of the first string
        dfs(arr[0][0], g)

        # Step 4: Verify that all characters with non-zero degrees are visited
        # If not all are visited, the graph isn't connected
        if len(visited) != len(g):
            return 0
        
        # If all conditions are satisfied, return 1 (can form a circle)
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))

# } Driver Code Ends