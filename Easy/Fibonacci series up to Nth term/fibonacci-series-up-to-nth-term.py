#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        if n==1 :
            return [0,1]
        if n==2 :
            return [0,1,1]
        a,b=0,1
        l=[0,1]
        for i in range(n-1) :
            c=(a+b)%(10**9+7)
            l.append(c)
            a=b
            b=c
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends