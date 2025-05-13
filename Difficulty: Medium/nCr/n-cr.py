#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        if r > n :
            return 0
        def f(x) :
            if x==0 :
                return 1
            p=1
            for i in range(1,x+1) :
                p=p*i
            return p
        ans=f(n)//(f(n-r)*f(r))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends