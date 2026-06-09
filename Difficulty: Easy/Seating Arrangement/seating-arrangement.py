class Solution:
    def canSeatAllPeople(self, k, seats):
        # code here
        n=len(seats)
        for i in range(n-1) :
            if seats[i]==1 and seats[i+1]==1 :
                return False
        
        for i in range(n) :
            l=False
            r=False
            if i==0 or seats[i-1]==0 :
                l=True
            if i==n-1 or seats[i+1]==0 :
                r=True
            
            if l and r and seats[i]==0 :
                k -=1
                seats[i]=1
            if k==0:
                break
        
        return k==0