class Solution:
    def coin(self, arr):
        # code here
        if len(arr)==1 :
            return arr[0]
        l=0
        r=len(arr)-1
        while l < r :
            if l<r and arr[l] >= arr[r] :
                l +=1
            else :
                r -=1
        return arr[l]