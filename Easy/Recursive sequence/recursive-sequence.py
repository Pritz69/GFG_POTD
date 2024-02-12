#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        s=0
        l=1
        mod=10**9 + 7
        for i in range(1,n+1) :
            p=1
            for j in range(l,l+i) :
                p=p*l
                l +=1
            s = (s+p)%mod
        return s
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends