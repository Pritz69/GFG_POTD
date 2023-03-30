from typing import List
import math
class Solution:
    def minimumInteger(self, n : int, arr : List[int]) -> int:
        s=sum(arr)
        req=math.ceil(s/n)
        ans=10**9 
        for item in arr:
            if item >= req:
                ans=min(ans,item)
        return ans 
