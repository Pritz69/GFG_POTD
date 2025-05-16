import heapq

class Solution:
    def findSmallestRange(self, arr):
        # code here
        k = len(arr)
        n = len(arr[0])
        
        min_heap = []
        max_value = float('-inf')
        
        for i in range(k):
            heapq.heappush(min_heap, (arr[i][0], i, 0))
            max_value = max(max_value, arr[i][0])
            
        range_start, range_end = float('-inf'), float('inf')
        
        while True:
            min_value, row, col = heapq.heappop(min_heap)
            
            if max_value - min_value < range_end - range_start:
                range_start, range_end = min_value, max_value
                
            if col + 1 == n:
                break
            
            next_value = arr[row][col + 1]
            heapq.heappush(min_heap, (next_value, row, col + 1))
            max_value = max(max_value, next_value)
            
        return [range_start, range_end]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split())))
    r = Solution().findSmallestRange(arr)
    print(r[0], r[1])
    print("~")

# } Driver Code Ends