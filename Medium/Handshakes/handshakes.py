#User function Template for python3

class Solution:
    def count(self, N):
        # code here
        dp=[0]*(N+1)
        dp[0]=1
        for i in range(2,N+1,2) :
            for j in range(0,(N-2)+1,2) :
                dp[i] = dp[i] + dp[j]*dp[i-2-j]
        return dp[N]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.count(N))
# } Driver Code Ends