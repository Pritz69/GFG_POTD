class Solution:
    def kSubstr(self, s, k):
        n = len(s)

        if n % k != 0:
            return False

        freq = {}
        blocks = n // k

        for i in range(0, n, k):
            part = s[i:i + k]
            freq[part] = freq.get(part, 0) + 1

        return max(freq.values()) >= blocks - 1