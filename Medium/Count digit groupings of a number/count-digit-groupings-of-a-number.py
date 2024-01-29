#User function Template for python3

class Solution:
	def TotalCount(self, s):
		# Code here
		n=len(s)
        def rec(i,su) :
            if i==n :
                return 1
            if (i,su) in dp :
                return dp[(i,su)]
            ans=0
            currs=0
            for j in range(i,n) :
                currs += int(s[j])
                if currs >= su :
                    ans = ans + rec(j+1,currs)
            dp[(i,su)]=ans
            return ans
        dp={}
        return rec(0,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends