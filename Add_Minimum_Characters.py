class Solution:
    def addMinChar (self, str1):
        # code here 
        l=0
        r=len(str1)-1
        res=0
        while (l<r) :
            if str1[l]==str1[r] :
                l +=1
                r -=1
            else :
                res +=1
                l=0
                r=len(str1)-res-1
        return res
