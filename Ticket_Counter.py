class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        # Code Here
        i=0
        j=N-1
        ans=0
        f=0
        while (True) :
            for x in range(K) :
                if i==j :
                    ans=i+1
                    f=1
                    break
                i +=1
            if f==1 :
                break
            for y in range(K) :
                if i==j :
                    ans=j+1
                    f=1
                    break
                j -=1
            if f==1 :
                break
        return ans
