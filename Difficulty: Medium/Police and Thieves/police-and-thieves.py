class Solution:
    def catchThieves(self, arr, k):
        #code  here
        n=len(arr)
        p,t,ans=0,0,0
        while p<n and t<n :
            while p<n and arr[p] !='P' :
                p +=1
            while t<n and arr[t] !='T' :
                t +=1
            if p<n and t<n and abs(p-t)<=k :
                ans +=1
                p +=1
                t +=1
            elif t<p :
                t+=1
            else :
                p+=1
                
        return ans