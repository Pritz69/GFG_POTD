class Solution():
    def solve(self, a, b, c):
        #your code goes here
        if ((a >(2*b + 2*c +2)) or (b >(2*a + 2*c +2)) or (c >(2*a + 2*b +2))):
            return -1
        return (a+b+c)
