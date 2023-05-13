from typing import List


class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        # code here
        l=0
        r=n-1
        c=0
        while l < r :
            if arr[l]!=arr[r] :
                x=arr[l]^arr[r]
                c +=1
                arr[l]=x
                arr[r]=x
            l +=1
            r -=1
        return c//2 if c%2==0 else c//2 + 1
