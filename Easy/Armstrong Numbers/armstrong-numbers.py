#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        ans=0
        t=n
        while t > 0 :
            d=t%10
            ans += d**3
            t=t//10
        return "true" if ans==n else "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends