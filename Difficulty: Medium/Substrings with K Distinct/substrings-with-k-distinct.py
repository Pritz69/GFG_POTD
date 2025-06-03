class Solution:
    def countSubstr (self, s, k):
        # Code here
        def helper(s,k) :
            d={}
            l=0
            c=0
            for r in range(len(s)) :
                d[s[r]]=d.get(s[r],0)+1
                while len(d) > k :
                    d[s[l]]=d[s[l]]-1
                    if d[s[l]]==0 :
                        d.pop(s[l])
                    l +=1
                c += (r-l)+1
            return c
                
        return helper(s,k)-helper(s,k-1)
                
        