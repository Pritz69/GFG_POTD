class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        arr.sort(key=lambda x : -x)
        ans=0
        i=0
        n=len(arr)
        while i < n :
            if i+1<n and arr[i]-arr[i+1] < k:
               ans +=arr[i]+arr[i+1]
               i+=2
            else :
                i+=1
        return ans
               