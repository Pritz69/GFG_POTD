#User function Template for python3

class Solution:

    def countPS(self, s):
        # code here
        cnt = 0
        n = len(s)
        
        for i in range(n):
            
            l,r=i,i
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>=2:
                    cnt+=1
                l-=1
                r+=1
            
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>=2:
                    cnt+=1
                l-=1
                r+=1
        return cnt

