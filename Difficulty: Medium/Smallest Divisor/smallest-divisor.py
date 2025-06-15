import math
class Solution:
    def smallestDivisor(self, arr, k):
        # Code here
        def func(x) :
            c=0
            for e in arr :
                c = c + int(math.ceil(e/x))
            return c 
        l=1
        h=max(arr)
        while l <= h :
            m=(l+h)//2
            if func(m) <= k :
                ans=m
                h=m-1
            else :
                l=m+1
        return ans
            