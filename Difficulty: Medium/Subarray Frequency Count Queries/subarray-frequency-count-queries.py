from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:

    def freqInRange(self, arr, queries):

        mp = defaultdict(list)

        # store positions
        for i, val in enumerate(arr):
            mp[val].append(i)

        ans = []

        for a, b, c in queries:

            positions = mp[c]

            left = bisect_left(positions, a)

            right = bisect_right(positions, b)

            ans.append(right - left)

        return ans