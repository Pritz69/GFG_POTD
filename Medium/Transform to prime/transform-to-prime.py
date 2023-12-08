#User function Template for python3
from math import sqrt


class Solution:
    def minNumber(self, arr,n):
        # code here
        s=sum(arr)
        t=s
        def prime(x) :
            if x==1 :
                return False
            if x==2 or x==3 :
                return True
            for i in range(2,int(sqrt(x))+2) :
                if x%i==0 :
                    return False
            return True
        if prime(s) :
            return 0
        c=0
        while c!=1 :
            s +=1
            if prime(s) :
                c=1
        return s-t

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends