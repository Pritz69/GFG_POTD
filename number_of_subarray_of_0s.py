class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        c=0
        ans=0
        for i in arr :
            if i==0 :
                c +=1
            else :
                ans += c*(c+1)//2 
                c=0
        if c !=0 :
            ans += c*(c+1)//2 
        return ans
        
