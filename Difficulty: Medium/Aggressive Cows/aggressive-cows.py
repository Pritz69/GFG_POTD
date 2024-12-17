#User function Template for python3

class Solution:

    def aggressiveCows(self, stalls, k):
        l,r=0,max(stalls)
        stalls.sort()
        
        def helper(m):
            count=1
            lcow=stalls[0]
            for i in stalls:
                if i-lcow>=m:
                    count+=1
                    if count==k:
                        return 1
                    lcow=i
            return 0
            
        while l<=r:
            m=l+(r-l)//2
            if helper(m):
                ans=m
                l=m+1
            else:
                r=m-1
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends