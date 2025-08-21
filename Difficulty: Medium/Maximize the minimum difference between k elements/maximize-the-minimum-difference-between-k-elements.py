class Solution:
    def canPlace(self,arr,k,d):
        n=len(arr)
        count=1
        last=arr[0]
        for i in range(1,n):
            if arr[i]-last>=d:
                count+=1
                last=arr[i]
            if count>=k:
                return True
        return False
    
    def maxMinDiff(self, arr, k):
        arr.sort()
        n=len(arr)
        l,h=0,arr[-1]-arr[0]
        ans=0
        while l<=h:
            mid=(l+h)//2
            if self.canPlace(arr,k,mid):
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans
