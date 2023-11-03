class Solution:
    def minDist(self, arr, n, x, y):
        m=float('inf')
        ix=-1
        iy=-1
        for i,v in enumerate(arr) :
            if v==x :
                ix=i
            if v==y :
                iy=i
            if ix!=-1 and iy!=-1 :
                m=min(m,abs(ix-iy))
        if ix==-1 or iy==-1 :
            return -1
        else :
            return m
