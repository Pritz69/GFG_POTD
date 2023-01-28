#User function Template for python3
from collections import Counter
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str):
        if Counter(s1) != Counter(s2):
            return False
        if len(s1) == 1:
            return True
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False
