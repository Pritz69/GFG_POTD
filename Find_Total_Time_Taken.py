from typing import List


class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        # code here
        t=0
        s=set()
        for x in arr :
            if x in s :
                t += time[x-1]
            else :
                t +=1
                s.add(x)
        return t-1
