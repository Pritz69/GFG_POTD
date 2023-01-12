import heapq
class Solution:
    def minimizeSum(self, N, arr):
        # Code here
        s=0
        ans=0
        h=[x for x in arr]
        heapq.heapify(h)
        while N>1 :
            s =heapq.heappop(h)
            s +=h[0]
            heapq.heappop(h)
            heapq.heappush(h,s)
            ans +=s
            N -=1
        return ans
