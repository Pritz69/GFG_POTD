class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        dp = [[None] * (sum + 1) for _ in range(len(arr))]

        def f(i, s):
            if s == 0:
                return True
            if i < 0 or s < 0:
                return False
            if dp[i][s] is not None:
                return dp[i][s]
            tk = f(i - 1, s - arr[i])
            ntk = f(i - 1, s)
            dp[i][s] = tk or ntk
            return dp[i][s]

        return f(len(arr) - 1, sum)        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends