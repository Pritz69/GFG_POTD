class Solution:
    def topK(self, nums, k):
        #Code here
        d={}
        for x in nums :
            d[x] = d.get(x,0) + 1
        d=sorted(d.items(), key=lambda x:(x[1],x[0]),reverse=True)
        i=0
        ans=[]
        for x in d :
            ans.append(x[0])
            i +=1
            if i==k :
                break
        return ans
