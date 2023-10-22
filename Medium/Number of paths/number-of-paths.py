#User function Template for python3

class Solution:
    def numberOfPaths (self, M, n):
            path = 1
            MOD = 10**9 + 7
            for i in range(M - 1):
                path = (path * (i + n)) % MOD
                temp = pow(i + 1, MOD - 2, MOD)
                path = (path * temp ) % MOD
            return path




#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends