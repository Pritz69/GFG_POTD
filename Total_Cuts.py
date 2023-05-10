from typing import List


class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        # code here
        l=[0]*N
        r=[0]*N
        l[0]=A[0]
        r[N-1]=A[N-1]
        ans=0
        for i in range(1,N) :
            l[i]=max(l[i-1],A[i])
        for i in range(N-2,-1,-1) :
            r[i]=min(r[i+1],A[i])
        for i in range(1,N) :
            if l[i-1]+r[i] >= K :
                ans +=1
        return ans
