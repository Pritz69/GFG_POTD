
from typing import List


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        def dfs(node, parent, adj, subtree_size, removable_edges):
            count = 1
            for neighbor in adj[node]:
                if neighbor != parent:
                    count += dfs(neighbor, node, adj, subtree_size, removable_edges)
            subtree_size[node] = count
            if count % 2 == 0 and node != 1:
                removable_edges.append((parent, node))
            return count
        
        adj = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        subtree_size = [0] * (n + 1)
        removable_edges = []

        dfs(1, -1, adj, subtree_size, removable_edges)
    
        return len(removable_edges)



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)

        print(res)

# } Driver Code Ends