from typing import List


class Solution:
    def maximumProfit(self, price) -> int:
        # code here
        n=len(price)
        profit = 0
        for i in range(1, n):
            if price[i] > price[i - 1]:
                profit += price[i] - price[i - 1]
        return profit

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends