import heapq
class Solution:
    def minValue(self, s, k):
        #code here
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        max_heap = [-v for v in freq.values()]
        heapq.heapify(max_heap)

        while k > 0 and max_heap:
            top = -heapq.heappop(max_heap)
            top -= 1
            k -= 1
            if top > 0:
                heapq.heappush(max_heap, -top)

        return sum(x * x for x in max_heap)