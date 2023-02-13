#User function Template for python3

class Solution:
    def inSequence(self, A, B, C):
    # code here
        if C==0:
            return 1 if A==B else 0
        n= (B-A)//C + 1
        return 1 if B==A+(n-1)*C and n>0 else 0
