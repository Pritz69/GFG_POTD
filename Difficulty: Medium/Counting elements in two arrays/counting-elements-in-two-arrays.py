class Solution:
    def countLessEq(self, a, b):
        def func(t):
            l, r = 0, len(b) - 1
            ans = len(b)
            while l <= r:
                m = (l + r) // 2
                if b[m] > t:
                    ans = m
                    r = m - 1
                else:
                    l = m + 1
            return ans

        b.sort()
        r = []
        for x in a:
            i = func(x)
            r.append(i)
        return r
