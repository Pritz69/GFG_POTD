#User function Template for python3

class Solution:
    def numberSequence(self, m, n):
        # code here
        if n==1 :
            return m
        def rec(i,v) :
            if i==n :
                if v <= m :
                    return 1
                return 0
            if v > m :
                return 0
            if (i,v) in dp :
                return dp[(i,v)]
            tk=0
            for j in range(v*2,m+1) :
                tk=tk+rec(i+1,j)
            dp[(i,v)]=tk
            return dp[(i,v)]
        dp={}
        ans=0
        for i in range(1,m//2 +1):
            ans += rec(1,i)
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        arr = input().split()
        m = int(arr[0])
        n = int(arr[1])
        
        ob = Solution()
        print(ob.numberSequence(m, n))
# } Driver Code Ends