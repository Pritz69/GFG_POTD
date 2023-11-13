#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, x, y, m, n):
        
        #code here
        dp=[[0]*(n+1) for i in range(m+1)]
        ans=0
        for i in range(1,m+1) :
            for j in range(1,n+1) :
                if x[i-1]==y[j-1] :
                    dp[i][j]=1 + dp[i-1][j-1]
                else :
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        ans += m-dp[m][n]
        ans += n-dp[m][n]
        ans += dp[m][n]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends