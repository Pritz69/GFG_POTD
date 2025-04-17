class Solution:
    def findMinCycle(self, V, edges):
        # code here
        from collections import defaultdict
        import heapq

        # Create adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        min_cycle = INF

        # For each edge, remove it and run Dijkstra
        for u, v, w in edges:
            # Temporarily remove the edge u-v
            graph[u].remove((v, w))
            graph[v].remove((u, w))

            # Run Dijkstra from u to v
            dist = [INF] * V
            dist[u] = 0
            heap = [(0, u)]

            while heap:
                d, node = heapq.heappop(heap)

                if d > dist[node]:
                    continue

                for nei, wt in graph[node]:
                    if dist[nei] > dist[node] + wt:
                        dist[nei] = dist[node] + wt
                        heapq.heappush(heap, (dist[nei], nei))

            if dist[v] != INF:
                min_cycle = min(min_cycle, dist[v] + w)

            # Add the edge back
            graph[u].append((v, w))
            graph[v].append((u, w))

        return min_cycle if min_cycle != INF else -1

        



#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        obj = Solution()
        res = obj.findMinCycle(V, edges)

        print(res)


if __name__ == "__main__":
    main()

# } Driver Code Ends