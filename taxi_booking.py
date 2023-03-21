from typing import List


class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        m=float('inf')
        ans=0
        for i in range(len(pos)) :
            ans=(abs(pos[i]-cur)) * time[i]
            m=min(m,ans)
        return m
