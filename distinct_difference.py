from typing import List


class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        # code here
        l=[0]*N
        r=[0]*N
        sl=set()
        sr=set()
        for i in range(N) :
            l[i]= len(sl)
            sl.add(A[i])
        for j in range(N-1,-1,-1) :
            r[j]= len(sr)
            sr.add(A[j])
        ans=[0]*N
        for i in range(len(A)) :
            ans[i]=l[i]-r[i]
        return ans
