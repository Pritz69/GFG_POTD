class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here 
        l=[]
        ans=-1
        cnt=0
        for i in range(N) :
            c=0
            for j in range(N) :
                if arr[j][i]==0:
                    c +=1
            if c > cnt :
                cnt=c
                ans=i
        return ans
