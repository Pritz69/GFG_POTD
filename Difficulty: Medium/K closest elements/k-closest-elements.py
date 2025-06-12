import heapq
class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        heap = []
        
        for num in arr:
            if num == x:
                continue
            heapq.heappush(heap, (abs(num - x), -num))
        
        result = []
        for _ in range(k):
            _, neg_num = heapq.heappop(heap)
            result.append(-neg_num)
        
        return result