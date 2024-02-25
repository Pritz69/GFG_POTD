#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        #your code here
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in [3,5,10]:
          for j in range(i,n+1):
            dp[j]+=dp[j-i]
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends