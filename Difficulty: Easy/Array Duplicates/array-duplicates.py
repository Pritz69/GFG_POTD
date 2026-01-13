class Solution:
    def findDuplicates(self, arr):
        # code here
        d={}   # {2:2,3:2,1:1}
        for x in arr :
            d[x]=d.get(x,0)+1
        #print(d)
        result=[]
        for x in d :
            if d[x]==2:
                result.append(x)
        
        return result