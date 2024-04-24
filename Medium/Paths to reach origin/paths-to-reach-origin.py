#User function Template for python3

class Solution:
    def ways(self, n,m):
        #write you code here
        mod = 1000000007
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for j in range(m + 1):
            dp[0][j] = 1
        #print(dp)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod
        #print(dp)
        return dp[n][m]
        
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    x,y=list(map(int,input().split()))
    ob = Solution()
    print(ob.ways(x,y))
# } Driver Code Ends