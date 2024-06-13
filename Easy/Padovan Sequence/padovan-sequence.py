#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        # code here 
        mod = 10**9 + 7
        a,b,c=1,1,1
        if n<=2 :
            return 1
        for i in range(3,n+1) :
            d=(a+b)%mod
            a=b
            b=c
            c=d
        return d
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends