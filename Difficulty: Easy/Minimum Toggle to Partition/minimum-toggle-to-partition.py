class Solution:
    def minToggle(self, arr):
        # code here
        n = len(arr)

        # prefix1[i] = number of 1s from 0 to i
        prefix1 = [0] * n
        prefix1[0] = arr[0]

        for i in range(1, n):
            prefix1[i] = prefix1[i - 1] + arr[i]

        # suffix0[i] = number of 0s from i to n-1
        suffix0 = [0] * n
        suffix0[n - 1] = 1 if arr[n - 1] == 0 else 0

        for i in range(n - 2, -1, -1):
            suffix0[i] = suffix0[i + 1] + (1 if arr[i] == 0 else 0)

        ans = float('inf')

        # try every partition
        for i in range(n + 1):

            # 1s on left side
            left = prefix1[i - 1] if i > 0 else 0

            # 0s on right side
            right = suffix0[i] if i < n else 0

            ans = min(ans, left + right)

        return ans