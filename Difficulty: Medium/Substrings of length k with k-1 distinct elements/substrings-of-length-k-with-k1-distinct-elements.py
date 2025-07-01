class Solution:
    def substrCount(self, s, k):
        # code here
        ans=0
        l=0
        r=0
        n=len(s)
        d={}
        while r < n :
            c=s[r]
            d[s[r]]=d.get(s[r],0)+1
            while (r-l+1) > k :
                d[s[l]]-=1
                if d[s[l]]==0 :
                    d.pop(s[l])
                l +=1
            if (r-l+1)==k and len(d)==k-1 :
                ans +=1
            r +=1
        return ans
            
        