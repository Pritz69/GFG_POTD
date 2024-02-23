from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        dp=[[[0]*3 for i in range(2)]for i in range(n+1)]
        
        for ind in range(n-1,-1,-1) :
            for buy in range(0,2) :
                for cap in range(1,3) :
                    if buy :
                        dp[ind][buy][cap]=max(dp[ind+1][0][cap]-price[ind],dp[ind+1][1][cap])
                    else :
                        dp[ind][buy][cap]=max(dp[ind+1][1][cap-1]+price[ind],dp[ind+1][0][cap])
        return dp[0][1][2]



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends