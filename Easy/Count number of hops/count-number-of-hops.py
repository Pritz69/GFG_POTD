#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        dp=[-1]*(n+1)
        mod=10**9 + 7
        def rec(i) :
            if i==n :
                return 1
            if dp[i] != -1 :
                return dp[i]
            o=0
            if i+1 <=n :
                o=rec(i+1)%mod
            t=0
            if i+2<=n :
                t=rec(i+2)%mod
            th=0
            if i+3<=n :
                th=rec(i+3)%mod
            dp[i] = (o+t+th)%mod
            return dp[i]
        return rec(0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends