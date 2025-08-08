class Solution:
	def getLPSLength(self, s):
		# code here
		n=len(s)
        ch=s[n-1]
        for i in range(n-2,-1,-1):
            if ch==s[i] and s[:i+1]==s[n-i-1:]:
                return i+1
        return 0