#User function Template for python3
from collections import defaultdict
class Solution:
    def kTop(self,a, N, K):
        #code here.
        ans=[]
        d=defaultdict(int)
        s=set()
        for i in range(N) :
            if a[i]==0:
                continue
            d[a[i]] +=1
            s.add(a[i])
            l=sorted(d.items(),key=lambda x:(-x[1],x[0]))
            #print(l)
            nl=[]
            if len(s) <= K :
                for x in l :
                    nl.append(x[0])
            else :
                for i in range(K) :
                    nl.append(l[i][0])
            ans.append(nl)
        return ans




#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    for line in ans:
        print(*line)



# } Driver Code Ends