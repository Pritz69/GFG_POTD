#User function Template for python3

class Solution:
	def TotalWays(self, N):
		# Code here
        a=1
        b=1
        c=0
        for i in range(N) :
            c=(a+b)%(10**9 +7)
            a=b
            b=c
        return (c*c)%(10**9 +7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends