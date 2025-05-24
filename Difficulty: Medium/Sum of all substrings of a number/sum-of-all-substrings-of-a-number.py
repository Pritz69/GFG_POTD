class Solution:
    def sumSubstrings(self,s):
        # code here
        ans=0
        n=len(s)
        for i in range(n) :
            for j in range(i+1,n+1) :
                w=s[i:j]
                #print(w)
                ans +=int(w)
        return ans