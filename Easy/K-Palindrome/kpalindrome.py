#User function Template for python3

class Solution:
    def kPalindrome(self, str, n, k):
        # code here
        def lcs(s1,s2) :
            dp=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
            for i in range(1,len(s1)+1) :
                for j in range(1,len(s2)+1) :
                    if s1[i-1]==s2[j-1] :
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else :
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                        
            return dp[len(s1)][len(s2)]
        
        ans=lcs(str,str[::-1])
        return 1 if (n-ans) <= k else 0
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        n = int(arr[0])
        k = int(arr[1])
        str = input()

        ob = Solution()
        print(ob.kPalindrome(str, n, k))

# } Driver Code Ends