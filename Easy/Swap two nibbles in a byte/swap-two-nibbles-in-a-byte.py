#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here 
        s=""
        while n :
            s=str(n%2)+s
            n=n//2
        s="0"*(8-len(s))+s
        ns=s[4:]+s[:4]
        ans=0
        p=0
        for i in range(7,-1,-1) :
            ans += (2**p)*int(ns[i])
            p+=1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends