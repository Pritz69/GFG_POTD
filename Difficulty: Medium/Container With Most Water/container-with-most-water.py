
class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        l=0
        r=n-1
        ans=0
        while l < r :
            ans=max(ans,min(arr[r],arr[l])*(r-l))
            if arr[l] < arr[r] :
                l +=1
            else :
                r -=1
                
        return ans
