class Solution:
	def mergeOverlap(self, arr):
		#Code here
        arr.sort(key=lambda x: x[0])
        
        # Initialize an empty list to store merged intervals
        merged = []
        
        for interval in arr:
            # If merged is empty or no overlap with the last interval, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap exists, merge by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends