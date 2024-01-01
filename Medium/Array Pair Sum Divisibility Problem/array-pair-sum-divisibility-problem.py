#User function Template for python3
from collections import defaultdict
class Solution:
	def canPair(self, nuns, k):
		# Code here
        d=defaultdict(int)
        for x in nuns :
            r=x%k
            if (k-r)%k in d :
                d[(k-r)%k] -=1
                if d[(k-r)%k]==0:
                    d.pop((k-r)%k)
            else :
                d[r]+=1
        return len(d)==0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends