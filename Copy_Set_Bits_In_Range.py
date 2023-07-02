
class Solution:
    def setSetBit(self, x, y, l, r):
        # code here
        for i in range(l,r+1) :
            t = 1 << (i-1)
            if t & y :
                x = x | t
        return x
