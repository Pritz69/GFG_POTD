from collections import defaultdict

class Solution:

    def characterReplacement(self, s, k):

        c = defaultdict(int)

        res, maxcount = 0, 0

 

        for idx, val in enumerate(s):

            c[val] += 1

            maxcount = max(maxcount, c[val])

            if res - maxcount >= k:

                c[s[idx - res]] -= 1

            else:

                res += 1

        return res
