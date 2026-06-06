class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        total = n * m * (n * m - 1)
        attacks = 4 * (n - 1) * (m - 2) + 4 * (n - 2) * (m - 1)
        return total - attacks