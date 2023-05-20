#User function Template for python3
import heapq
class Solution:
    def isStraightHand(self, N, groupSize, hand):
        # Code here
        if len(hand)%groupSize :
            return False
        c={}
        for i in hand :
            c[i] = 1 + c.get(i,0)
        minh = list(c.keys())
        heapq.heapify(minh)
        while minh :
            st = minh[0]
            for i in range(st,st+groupSize) :
                if i not in c :
                    return False
                c[i] -=1
                if c[i] ==0 :
                    if i != minh[0] :
                        return False
                    heapq.heappop(minh)
        return True
