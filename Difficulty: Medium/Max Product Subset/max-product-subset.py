class Solution:
    def findMaxProduct(self, arr):
        
        arr.sort()
        le = 1
        maxi = 1
        is_first = True
        for i in arr:
            t = le * i
            le = maxi * i 
            maxi = max(i, i if is_first else maxi, le, t)
            is_first = False

        return maxi % (10**9 + 7) if maxi > 0 else maxi