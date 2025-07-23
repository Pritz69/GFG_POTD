class Solution:
    def subarraySum(self, arr):
        # code here 
        #formula--> d*(n-d+1)
        
        ans=0
        n=len(arr)
        for i in range(n) :
            c=(i+1)*(n-(i+1)+1)
            ans += c*arr[i]
        return ans
            