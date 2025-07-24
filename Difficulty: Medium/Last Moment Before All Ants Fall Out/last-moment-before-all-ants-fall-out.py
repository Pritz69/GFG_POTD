class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        r=0
        l=0
        for i in left :
            l=max(l,i)
        for i in right :
            r=max(r,n-i)
        return max(l,r)