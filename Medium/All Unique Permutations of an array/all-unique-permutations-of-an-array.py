#User function Template for python3
from collections import Counter
class Solution:
    def uniquePerms(self, arr, n):
        # code here 
        def rec() :
            if len(l)==n :
                a=l.copy()
                s.add(tuple(a))
                return
            else :
                for x in c :
                    if c[x] > 0 :
                        l.append(x)
                        c[x] -=1
                        rec()
                        l.pop()
                        c[x] +=1
        c=Counter(arr)
        s=set()
        l=[]   
        rec()     
        return sorted(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends