class Solution:
    def minSoldiers(self, arr, k):
        # code here
        n=len(arr)
        if n%2==0 :
            req=n//2
        else :
            req=(n+1)//2
        re=[]
        c=0
        for x in arr :
            if x%k==0 :
                c +=1
            else :
                re.append(k-(x%k))
        re.sort()
        if c >=req :
            return 0
        else :
            ans=0
            i=0
            while c < req :
                ans += re[i]
                i +=1
                c +=1
        return ans
        
        
        #1 4 6 8 8 8 9 9 9 10