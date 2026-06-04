class Solution:
	def maxSubstring(self, s):
		# code here
		ans=-1
		cs=0
		for c in s :
		    if c=='0' :
		       cs +=1
		    elif c=='1' :
		        cs -=1
		    ans=max(ans,cs)
		    if cs < 0 :
		        cs = 0
	    return ans