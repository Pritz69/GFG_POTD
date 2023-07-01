class Solution:
	def setBits(self, N):
		# code here
		c=0
		while (N>0) :
		    x=N%2
		    N = N//2
		    if x==1 :
		        c +=1
		return c
