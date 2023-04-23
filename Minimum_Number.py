class Solution:
    def minimumNumber(self, n, arr):
        #code here
        m=float('inf')
        for x in arr :
            if x%2 !=0 :
                return 1
            m = min(m,x)
        return m
