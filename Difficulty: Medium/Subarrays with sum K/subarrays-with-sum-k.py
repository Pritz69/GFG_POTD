from collections import defaultdict
class Solution:
    def cntSubarrays(self, arr, k):
        dic=defaultdict(int)
        ans=0
        sums=0
        dic[0]+=1
        for i in arr:
            sums+=i
            find=sums-k
            ans+=dic[find]
            dic[sums]+=1
        return ans
        
 