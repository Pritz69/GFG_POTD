from typing import List, Tuple
from collections import deque

class Solution:
    def chefAndWells(self, n : int, m : int, c : List[List[str]]) -> List[List[int]]:
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        dist = [[-1 for _ in range(m)] for _ in range(n)]
        vis = [[False for _ in range(m)] for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if c[i][j] == 'W':
                    q.append((i, j))
                    vis[i][j] = True
                if c[i][j] == 'W' or c[i][j] == '.' or c[i][j] == 'N':
                    dist[i][j] = 0
        dis = 2
        while q:
            qsize = len(q)
            for _ in range(qsize):
                i, j = q.popleft()
                for k in range(4):
                    curri, currj = i + dx[k], j + dy[k]
                    if 0 <= curri < n and 0 <= currj < m and not vis[curri][currj] and c[curri][currj] != 'N':
                        vis[curri][currj] = True
                        q.append((curri, currj))
                        if c[curri][currj] == 'H':
                            dist[curri][currj] = dis
            dis += 2
        return dist
