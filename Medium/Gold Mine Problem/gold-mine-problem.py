# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        dp={}
        def func(i,j) :
            if i<0 or j<0  or i==n or j==m :
                return 0
            if (i,j) in dp :
                return dp[(i,j)]
            c=0
            c=c+M[i][j]+max(func(i-1,j+1),max(func(i,j+1),func(i+1,j+1)))
            dp[(i,j)]=c
            return c
            
        mx=0
        for i in range(n) :
            mx=max(mx,func(i,0))
        return mx

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends