class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        n=len(prices)
        prices.sort()
        mi,ma=0,0
        l,r=0,n-1
        while l <= r :
            mi += prices[l]
            l +=1
            r -=k
        l,r=0,n-1
        while l <= r :
            ma += prices[r]
            r -=1
            l +=k
        return [mi,ma]
        
        
        #1 2 3 4 5 6 7 8
        