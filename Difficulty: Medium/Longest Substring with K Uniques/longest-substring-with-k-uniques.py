class Solution:
    def longestKSubstr(self, s, k):
        # code here
        l,r=0,0
        ans=-1
        d={}
        n=len(s)
        while r < n :
            d[s[r]]=d.get(s[r],0)+1
            while len(d) > k :
                d[s[l]]=d[s[l]]-1
                if d[s[l]]==0 :
                    d.pop(s[l])
                l +=1
            if len(d)==k :
                ans=max(ans,(r-l)+1)
            r +=1
        return ans