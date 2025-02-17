import heapq
class Solution:
	def kLargest(self, arr, k):
		# Your code here
		h = []
        heapq.heapify(h)
        for x in arr:
            heapq.heappush(h, x)
            if len(h) > k:
                heapq.heappop(h)
        
        result = sorted(h, reverse=True)
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends