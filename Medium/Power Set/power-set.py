#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		self.subsequence=[]
        def track(ind, cur):
            if ind>=len(s):
                if cur!="":
                    self.subsequence.append(cur)
                return
            track(ind+1,cur+s[ind])
            track(ind+1,cur)
        track(0,"")
        return sorted(self.subsequence)
#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends