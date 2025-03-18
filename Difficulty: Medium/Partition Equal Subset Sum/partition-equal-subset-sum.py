class Solution:
    def equalPartition(self, arr):
        # code here
        sm=sum(arr)
        dp = [[None] * (sm + 1) for _ in range(len(arr))]
        
        def f(i, s):
            if s == (sm-s):
                return True
            if i < 0 or s < 0:
                return False
            if dp[i][s] is not None:
                return dp[i][s]
            tk = f(i - 1, s - arr[i])
            ntk = f(i - 1, s)
            dp[i][s] = tk or ntk
            return dp[i][s]

        return f(len(arr) - 1, sm)  

#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends