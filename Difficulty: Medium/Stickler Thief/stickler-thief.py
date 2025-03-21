class Solution:  
    def findMaxSum(self,arr):
        # code here
        def f(i) :
            if i < 0 :
                return 0
            if i in dp :
                return dp[i]
            t,nt=0,0
            t=t+arr[i]+f(i-2)
            nt=nt+f(i-1)
            dp[i]=max(t,nt)
            return dp[i]
        
        n=len(arr)
        dp={}
        return f(n-1)

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends