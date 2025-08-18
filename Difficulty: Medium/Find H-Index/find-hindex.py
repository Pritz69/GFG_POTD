class Solution:
    def hIndex(self, citations):
        #code here
        n = len(citations)
        citations.sort()
        ans = 0
        
        for i in range(n):
            h = n - i   # number of papers with citations >= citations[i]
            if citations[i] >= h:
                ans = max(ans, h)
        
        return ans