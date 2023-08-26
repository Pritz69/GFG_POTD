#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        l=0
        r=0
        n=len(s)
        d={}
        ans=-1
        while(r<n) :
            x=s[r]
            d[x]=d.get(x,0) + 1
            if len(d)==k :
                ans=max(ans,r-l+1)
            elif len(d) > k :
                while len(d) > k :
                    d[s[l]] = d.get(s[l]) - 1
                    if d[s[l]]==0 :
                        d.pop(s[l])    # del d[s[l]]
                    l +=1
            r +=1
        return ans



