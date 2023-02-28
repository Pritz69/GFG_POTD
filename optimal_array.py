from typing import List


class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        # code here
        ans =[0]
        sum1 = 0
        sum2 = 0
        for i in range(1,n):
            if((i+1)%2 == 0):
                sum1+=a[i//2]
                sum2+=a[i]
            else:
                sum2+=(a[i]-a[i//2])
            ans.append(sum2-sum1)
        return ans
