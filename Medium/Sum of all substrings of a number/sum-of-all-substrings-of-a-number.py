#User function Template for python3

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        
        # code here
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=int(s[0])
        mod=10**9 + 7 
        ans=dp[0]
        for i in range(1,n) :
            dp[i]=((dp[i-1]*10)%mod + (int(s[i])*(i+1))%mod )%mod
            ans=(ans+dp[i])%mod
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends