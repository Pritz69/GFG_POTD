class Solution:
    def rearrange(self, arr, x):
        # code here
        nl=[]
        for i,e in enumerate(arr) :
            nl.append((abs(e-x),i))
        
        nl.sort()
        ans=[]
        i=0
        for x in nl :
            ans.append(arr[x[1]])
        
        for i in range(len(arr)) :
            arr[i]=ans[i]
        return arr
        
        