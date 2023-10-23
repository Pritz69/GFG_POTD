#User function Template for python3
class Solution:
	def maxSumIS(self, nums, n):
		# code here
        dp=[x for x in nums]
        m=float('-inf')
        for i in range(n) :
            for j in range(i) :
                if nums[j] < nums[i] :
                    dp[i]=max(dp[i],nums[i]+dp[j])
            m=max(m,dp[i])
        #print(dp)
        return m
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends