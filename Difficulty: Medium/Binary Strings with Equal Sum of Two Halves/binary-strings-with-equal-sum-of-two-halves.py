from math import factorial as fact

class Solution:
    def computeValue(self, n):
        return (fact(2 * n) // (fact(n) ** 2)) % (10 ** 9 + 7)