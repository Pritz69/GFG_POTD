class Solution:
    def minDifference(self, arr):
        ans = []
        for x in arr:
            h, m, s = map(int, x.split(":"))
            v = h * 3600 + m * 60 + s
            ans.append(v)
        
        ans.sort()
        
        min_diff = float('inf')
        for i in range(1, len(ans)):
            min_diff = min(min_diff, ans[i] - ans[i-1])
        
        # Consider circular time (add the difference between last and first times)
        min_diff = min(min_diff, 24 * 3600 - (ans[-1] - ans[0]))
        
        return min_diff

