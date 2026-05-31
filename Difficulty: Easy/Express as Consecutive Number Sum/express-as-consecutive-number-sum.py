class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        # code here
        return not(n&(n-1)==0)