class Solution:
    def missingNumber(self, arr):
        # code here
        d={}
        m=0
        for x in arr :
            d[x]=d.get(x,0)+1
            m=max(m,x)
        for i in range(1,m+1) :
            if i not in d :
                return i
        return m+1