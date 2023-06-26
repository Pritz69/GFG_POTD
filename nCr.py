class Solution:
    def nCr(self, n, r):
        # code here
        if r>n :
            return 0
        f=[1]*(1001)
        for i in range(2,1001) :
            f[i]= f[i-1]*i
        num=f[n]
        den=f[r]*f[n-r]
        return (num//den)%(10 **9 +7)
