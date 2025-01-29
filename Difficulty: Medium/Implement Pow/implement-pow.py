#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        n=-e if e<0 else e
        x=b
        ans=1.0
        while n:
            if n&1:
                ans*=x
                n-=1
            else:
                x*=x
                n=n>>1
        if e<0:
            ans=1.0/ans
        return ans

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends