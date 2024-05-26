#User function Template for python3
class Solution:
	def findMinCost(self, x, y, costX, costY):
		# code here
        def lcs(s1,s2) :
            n,m=len(s1),len(s2)
            dp=[[0]*(m+1) for _ in range(n+1)]
            for i in range(1,n+1) :
                for j in range(1,m+1) :
                    if s1[i-1]==s2[j-1] :
                        dp[i][j]=1+dp[i-1][j-1]
                    else :
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return dp[n][m]
        
        ans=lcs(x,y)
        cost= ((len(x)-ans)*costX) + ((len(y)-ans)*costY)
        return cost

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X, Y, costX, costY = input().split()
        costX = int(costX)
        costY = int(costY)
        ob = Solution()
        ans = ob.findMinCost(X, Y, costX, costY)
        print(ans)

# } Driver Code Ends