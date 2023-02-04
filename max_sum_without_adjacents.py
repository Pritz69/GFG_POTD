class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
        if n==1 :
            return arr[0]
        if n>=2 :
            arr[1]=max(arr[0],arr[1])
        for i in range(2,n) :
            arr[i]=max(arr[i-1],(arr[i-2]+arr[i]))
        return arr[n-1]
