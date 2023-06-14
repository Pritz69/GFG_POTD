import heapq
class Solution:
    def maxDiamonds(self, A, N, K):
        # code here
        h=[]
        c=0
        for x in A :
            heapq.heappush(h,-x)
        while K != 0 :
            v= -1 * (heapq.heappop(h))
            c += v
            heapq.heappush(h,-(v//2))
            K -=1
        return c
