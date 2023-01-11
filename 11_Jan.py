
class Solution:
    def minIncrements(self, arr, N): 
        # Code here
        arr.sort()
        val =arr[0]
        ans=0
        for x in arr:
            if (x>val):
                val=x+1;
            else:
                ans+=val-x;
                val+=1;
        return ans
