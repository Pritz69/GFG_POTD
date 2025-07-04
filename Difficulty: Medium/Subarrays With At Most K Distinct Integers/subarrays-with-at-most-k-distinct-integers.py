class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        ans=0
        d={}
        l,r=0,0
        n=len(arr)
        while r < n :
            d[arr[r]]=d.get(arr[r],0)+1
            while len(d) > k :
                d[arr[l]]=d.get(arr[l],0)-1
                if d[arr[l]]==0 :
                    d.pop(arr[l])
                l +=1
            ans += (r-l)+1
            r +=1
        return ans
        