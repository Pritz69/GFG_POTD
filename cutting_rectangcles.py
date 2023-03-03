import math
class Solution:
    def minimumSquares(self, L, B):
        # code here
        k=math.gcd(L,B)
        n=(L//k) * (B//k)
        return n,k
