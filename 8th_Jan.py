class Solution:
    def countPairs (self, n, arr, k):
        # code here
        ans=0
        mp=dict()
        for ele in arr:
            if ele%k in mp:
                ans+=mp[ele%k]
                mp[ele%k]+=1
            else:
                mp[ele%k]=1
        return ans
