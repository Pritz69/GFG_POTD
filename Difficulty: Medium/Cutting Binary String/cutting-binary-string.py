class Solution:
    def cuts(self, s):
        # code here
        powers_of_5 = set()
        val = 1
        while val < (1 << 31):  # Since len(s) ≤ 30, 2^31 is a safe limit
            powers_of_5.add(bin(val)[2:])
            val *= 5

        n = len(s)
        dp = {}

        def solve(i):
            if i == n:
                return 0  # No cuts needed at the end
            if s[i] == '0':
                return float('inf')  # Skip substrings with leading zero
            if i in dp:
                return dp[i]

            min_cuts = float('inf')
            for j in range(i, n):
                substr = s[i:j+1]
                if substr in powers_of_5:
                    res = solve(j + 1)
                    if res != float('inf'):
                        min_cuts = min(min_cuts, 1 + res)

            dp[i] = min_cuts
            return dp[i]

        result = solve(0)
        return result if result != float('inf') else -1