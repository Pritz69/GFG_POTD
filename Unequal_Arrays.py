from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        A.sort()
        B.sort()
        cea,ceb,coa,cob=[],[],[],[]
        for x in A :
            if x%2==0 :
                cea.append(x)
            else :
                coa.append(x)
        for x in B :
            if x%2==0 :
                ceb.append(x)
            else :
                cob.append(x)
        if sum(A) != sum(B) :
            return -1
        if len(coa) != len(cob) :
            return -1
        ans=0
        for i in range(len(coa)) :
            ans += abs(coa[i]-cob[i])
        for i in range(len(cea)) :
            ans += abs(cea[i]-ceb[i])
        return (ans//4)
