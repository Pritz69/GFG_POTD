#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		ans=-1
		for i in range(1,len(arr)) :
		    if arr[i] < arr[i-1] :
		        ans=arr[i-1]
		        break
		if ans==-1 :
		    ans=arr[len(arr)-1]
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends