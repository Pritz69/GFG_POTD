class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        p=-1
        for i in range(n) :
            if arr[i]==1 :
                p=i
                break
        return p
