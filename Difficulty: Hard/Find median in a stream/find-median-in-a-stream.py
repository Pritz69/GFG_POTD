import heapq

class Solution:
    def getMedian(self, arr):
        # Min-heap for larger half and max-heap (inverted values) for smaller half
        min_heap = []  # Min-heap
        max_heap = []  # Max-heap (using negative values for inversion)
        result = []
        
        for num in arr:
            # Add the number to the appropriate heap
            if len(max_heap) == 0 or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            
            # Balance the heaps
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            
            # Calculate the median
            if len(max_heap) == len(min_heap):
                median = (-max_heap[0] + min_heap[0]) / 2.0
            else:
                median = -max_heap[0] / 1.0
            
            # Append the current median to the result list
            result.append(median)
        
        return result




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends