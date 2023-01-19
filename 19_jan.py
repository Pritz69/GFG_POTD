class Solution:
    def carpetBox(self, A,B,C,D):
        #code here
        def solve(A,B,C,D):
            ans=0
            while A > C or B > D :
                if A > C :
                    ans +=1
                    A = A//2
                if B > D :
                    ans +=1
                    B = B//2
            return ans
        return min(solve(A,B,C,D),solve(B,A,C,D))
