class Solution:
    def maximumProfit(self, prices):
        # code here
        buy=prices[0]
        res=0
        for i in prices[1:]:
            if i<buy:
                buy=i
            else:
                res=max(res,i-buy)
        return res

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends