class Solution:
    def isPossible(self,arr,val,k):
        count,curr=1,0
        for pages in arr:
            curr+=pages
            if curr>val:
                curr=pages
                count+=1
            if count>k or pages>val:
                return False
        return True
    
    def findPages(self, arr, k):
        if len(arr)<k:
            return -1
        l,h,ans=0,sum(arr),-1
        while l<=h:
            mid=(l+h)//2
            if self.isPossible(arr,mid,k):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
