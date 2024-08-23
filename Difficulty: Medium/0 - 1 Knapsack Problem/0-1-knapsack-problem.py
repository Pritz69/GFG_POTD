#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
       
        # code here
        def rec(i,w) :
            if i < 0 or w <= 0 :
                return 0
            if (i,w) in dp :
                return dp[(i,w)]
            t=0
            nt=0
            if w >= wt[i] :
                t=val[i]+rec(i-1,w-wt[i])
            nt=rec(i-1,w)
            dp[(i,w)]=max(nt,t)
            return dp[(i,w)]
        dp={}
        return rec(len(wt)-1,W)
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends