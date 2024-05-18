#User function Template for python3
from typing import List

class Solution:
	def findPeakElement(self, a):
		# Code here
        l,h=0,len(a)-1
        ans=0
        while l <= h :
            m=(l+h)//2
            ans=max(ans,a[m])
            if m+1 < len(a) and a[m] < a[m+1] :
                l=m+1
            else :
                h=m-1
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends