#User function Template for python3
import heapq
class Solution:
    def minCost(self, houses):
      # code here
        if len(houses) == 1:
            return 0
    
        n = len(houses)
        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, node)
        total_cost = 0
        count = 0
    
        def distance(i, j):
            return abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])
    
        while min_heap and count < n:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            count += 1
    
            for v in range(n):
                if not visited[v]:
                    heapq.heappush(min_heap, (distance(u, v), v))
    
        return total_cost

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends