class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        p=1
        i,j=0,0
        ans=0
        while j<n :
            p=p*a[j]
            while p >=k and i<j:
                p=p//a[i]
                i +=1
            if p<k :
                ans += (j-i)+1
            j +=1
        return ans
