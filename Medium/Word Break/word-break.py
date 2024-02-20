#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        nn=len(s)
        dp=[0]*(nn+1)
        dp[nn]=1
        for i in range(nn-1,-1,-1) :
            for w in dictionary :
                if i+len(w) <= nn and s[i:i+len(w)] == w :
                    dp[i]=dp[i+len(w)]
                if dp[i] :
                    break
        return dp[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends