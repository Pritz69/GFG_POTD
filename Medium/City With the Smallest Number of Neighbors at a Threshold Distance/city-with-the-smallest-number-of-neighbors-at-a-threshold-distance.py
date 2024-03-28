#User function Template for python3
from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        g = defaultdict(list)
        
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        def dijkstr(n):
            costs = {n: 0}
            q = [(0, n)]
            while q:
                cost0, n0 = heappop(q)
                for nbr, c in g[n0]:
                    cost = cost0+c
                    if cost > distanceThreshold:
                        continue
                    if nbr not in costs or costs[nbr] > cost:
                        costs[nbr] = cost
                        heappush(q, (cost, nbr))
            return len(costs)
            
        ans = 0
        cnt = n
        for k in range(n):
            c = dijkstr(k)
            if c <= cnt:
                cnt = c
                ans = k
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        
        n, m = map(int, input().strip().split())
        edges = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            edges.append([u, v, wt])
        distanceThreshold = int(input())
        obj = Solution()
        ans = obj.findCity(n, m, edges, distanceThreshold)
        print(ans)
            

# } Driver Code Ends