class Solution:
    def validGroups(self, s):
        # code here
        n = len(s)
        dp = {}
        def solve(i, prev_sum):
            if i == n:
                return 1

            if (i, prev_sum) in dp:
                return dp[(i, prev_sum)]

            ans = 0
            curr_sum = 0

            for j in range(i, n):

                curr_sum += int(s[j])

                if curr_sum >= prev_sum:

                    ans += solve(j + 1, curr_sum)

            dp[(i, prev_sum)] = ans

            return ans

        return solve(0, 0)
        