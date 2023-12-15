#User function Template for python3

class Solution:
	def nthPoint(self,n):
		# Code here
        a=0
        b=1
        mod=10**9 + 7
        for i in range(n):
            c=(a+b)%mod
            a=b
            b=c
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends