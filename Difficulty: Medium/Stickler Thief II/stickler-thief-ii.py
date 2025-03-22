class Solution:
    def maxValue(self, ar) :
        # code here
        def f(i) :
            if i < 0 :
                return 0
            if i in dp :
                return dp[i]
            t,nt=0,0
            t=t+arr[i]+f(i-2)
            nt=nt+f(i-1)
            dp[i]=max(t,nt)
            return dp[i]
        
        n=len(ar)
        arr=ar[1:n]
        dp={}
        ans= f(len(arr)-1)
        
        arr=ar[:n-1]
        dp={}
        ans=max(ans, f(len(arr)-1))
        
        return ans
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends