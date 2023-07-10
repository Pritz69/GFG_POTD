class Solution:
    def maximumSumSubarray (self,k,arr,n):
        # code here 
        ma=float('-inf')
      	s=0
      	l=0
      	for i in range(n) :
      		s += arr[i]
      		if (i-l+1 ==k) :
      			ma = max(ma,s)
      			s -=arr[l]
      			l +=1
      	return ma
