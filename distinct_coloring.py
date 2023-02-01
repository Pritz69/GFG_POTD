#User function Template for python3

class Solution:
    def distinctColoring (self, N, r, g, b):
        # code here 
        for i in range(1, len(r)):
            r[i] += min(g[i - 1], b[i - 1])
            g[i] += min(r[i - 1], b[i - 1])
            b[i] += min(r[i - 1], g[i - 1])
        return min(r[-1], g[-1], b[-1])
    
