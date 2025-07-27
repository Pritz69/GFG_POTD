class Solution:
    def upperBound(self, arr, target):
        # code here
        n=len(arr)
        l=0
        h=n-1
        ans=n
        while l <=h :
            m=(l+h)//2
            if arr[m] > target :
                ans=m
                h=m-1
            else :   #<=
                l=m+1
        return ans