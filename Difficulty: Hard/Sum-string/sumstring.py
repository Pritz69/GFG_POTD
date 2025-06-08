class Solution:
    def isSumString (self, s):
        # code here 
        def is_valid(a: str, b: str, remaining: str) -> bool:
            if (a.startswith('0') and len(a) > 1) or (b.startswith('0') and len(b) > 1):
                return False
            sum_str = str(int(a) + int(b))
            if not remaining.startswith(sum_str):
                return False
            if remaining == sum_str:
                return True
            return is_valid(b, sum_str, remaining[len(sum_str):])

        n = len(s)
        # Try all possible pairs (i, j) for first and second numbers
        for i in range(1, n):
            for j in range(i + 1, n):
                if is_valid(s[:i], s[i:j], s[j:]):
                    return True
        return False