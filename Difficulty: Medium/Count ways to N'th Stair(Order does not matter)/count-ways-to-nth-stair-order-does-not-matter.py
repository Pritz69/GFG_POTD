#User function Template for python3

class Solution:
	def nthStair(self,n):
		return (n//2)+1

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
		ans = ob.nthStair(n)
		print(ans)
# } Driver Code Ends