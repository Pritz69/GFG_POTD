class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices.sort()
        holes.sort()
        l,r=0,0
        n,m=len(mices),len(holes)
        ans=0
        while l < n and r < m :
            ans=max(ans,abs(mices[l]-holes[r]))
            l +=1
            r +=1
        return ans
            
        