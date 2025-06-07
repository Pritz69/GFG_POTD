class Solution:
    def longestCommonSum(self, a1, a2):
        #Code here.
        s1=0
        s2=0
        d={}
        ans=0
        for i in range(len(a1)) :
            s1 += a1[i]
            s2 += a2[i]
            if s1==s2 :
                ans=max(ans,i+1)
            else :
                diff = s1-s2
                if diff in d :
                    ans=max(ans,i-d[diff])
                else :
                    d[diff]=i
            
        return ans