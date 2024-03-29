#User function Template for python3

class Solution:
        
    def kPalindrome(self, str, n, k):
        # code here
        def isKPalDP(str1, str2, m, n):
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    if not i :
                        dp[i][j] = j  
                    elif not j :
                        dp[i][j] = i   
                    elif (str1[i - 1] == str2[j - 1]):
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j],  
                                          (dp[i][j - 1])) 
            return dp[m][n]
        rev=str[::-1]
        return (1 if isKPalDP(str,rev,n,n) <= (2*k) else 0)
