
class Solution():
    def solve(self, N, A):
        #your code here
        v=0
        for i in range(N-1,-1,-1) :
            if (A[i]+1) <= 9 :
                v=i
                break
            elif (A[i]+1) > 9 :
                continue
        return v+1
