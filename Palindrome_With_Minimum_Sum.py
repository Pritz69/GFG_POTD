import math
class Solution:
    def minimumSum(self, s : str) -> int:
        # code here
        ans=0
        s=list(s)
        n=len(s)
        for i in range(n//2) :
            if s[i]=='?' and s[n-i-1] !='?' :
                s[i]=s[n-i-1]
            elif s[i]!=s[n-i-1] and s[i]!='?' and s[n-i-1]!='?' :
                return -1
        prev='.'
        for i in range(n//2) :
            if s[i]!='?' :
                if prev=='.' :
                    prev = s[i]
                elif s[i]!=prev :
                    ans += abs(ord(s[i])-ord(prev))
                prev=s[i]
        return ans*2
            

