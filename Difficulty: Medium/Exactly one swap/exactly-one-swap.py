from collections import Counter
class Solution:
    def countStrings(self, s): 
        n = len(s)
        freq = Counter(s)
        total_swaps = n * (n - 1) // 2
        redundant = sum(f * (f - 1) // 2 for f in freq.values())
        res = total_swaps - redundant
        if redundant > 0:
            return res + 1
        return res