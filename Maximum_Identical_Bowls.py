from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        # code here
        s=sum(arr)
        l=[]
        for i in range(N,0,-1) :
            if s%i == 0:
                l.append(i)
        return l[0]
