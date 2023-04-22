from typing import List

class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        # code here
        d=dict()
        a=arr.copy()
        a.sort()
        s=0
        ans=[]
        for i in range(n):
            if a[i] not in d:
                d[a[i]]=s
            s+=a[i]
        for i in arr:
            ans.append(d[i])
        return ans
