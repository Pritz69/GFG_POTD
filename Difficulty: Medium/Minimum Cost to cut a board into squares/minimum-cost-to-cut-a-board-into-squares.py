class Solution:
    def minCost(self, n, m, x, y):
        # code here
        hx = 1
        vr = 1
        x.sort(reverse = True)
        y.sort(reverse = True)
        
        ans = 0
        i = 0
        j = 0
        
        r = len(x)
        c = len(y)
        
        while i < r and j < c:
            if x[i] >= y[j]:
                ans += x[i]*vr
                hx += 1
                i += 1
            else:
                ans += y[j]*hx
                vr += 1
                j += 1
        
        while i < r:
            ans += x[i]*vr
            hx += 1
            i += 1
        
        while j < c:
            ans += y[j]*hx
            vr += 1
            j += 1
        
        return ans
