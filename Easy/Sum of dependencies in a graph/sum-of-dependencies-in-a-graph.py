
class Solution:
    def sumOfDependencies(self,adj,V):
        #code here
        s=0
        for x in adj :
            s += len(x)
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[[] for i in range(N)]
        s=list(map(int,input().strip().split()))
        for i in range(0,2*M,2):
            x=s[i]
            y=s[i+1]
            a[x].append(y)
        ob=Solution()
        print(ob.sumOfDependencies(a,N))
        


# } Driver Code Ends