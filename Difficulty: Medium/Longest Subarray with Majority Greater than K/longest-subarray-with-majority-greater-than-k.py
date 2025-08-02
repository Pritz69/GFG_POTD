class Solution:
    def longestSubarray(self, arr, k):
        pre, res, idx = 0, 0, {0: -1}
        for i, val in enumerate(arr):
            pre += 1 if val > k else -1
            if pre > 0:
                res = i + 1
            elif pre - 1 in idx:
                res = max(res, i - idx[pre - 1])
            idx.setdefault(pre, i)
        return res

