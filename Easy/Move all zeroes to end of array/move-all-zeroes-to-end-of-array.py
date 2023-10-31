#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
        r=0
        l=0
        while r<n :
            if arr[r] !=0 :
                arr[l]=arr[r]
                l +=1
            r +=1
        while l<n :
            arr[l]=0
            l +=1
        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends