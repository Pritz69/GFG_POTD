class Solution:
    def lcmTriplets(self, n):
        if n <= 2:
            return n
        if n & 1: # odd
            return n * (n - 1) * (n - 2)
        else:
            # even
            if n % 3:
                # 3 doesn't divide "n", can use "n - 3"
                return n * (n - 1) * (n - 3)
            else:
                return (n - 1) * (n - 2) * (n - 3)