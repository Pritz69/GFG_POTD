from typing import List
from collections import defaultdict
class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        # code here
        d=defaultdict(int)
        for x in intervals :
            l=x[0]
            r=x[1]
            d[l] +=1
            d[r+1] -=1
        c=0
        m=-1
        f=False
        for x in sorted(d.keys()):
            c += d[x]
            if c >= k :
                f= True
                m=x
            elif f==True :
                m=x-1
                f=False
            else :
                f=False
        return m
