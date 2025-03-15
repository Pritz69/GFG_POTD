class Solution:
	def minCoins(self, coins, amount):
		# code here
        from functools import lru_cache
        coins=tuple(coins)
        
        @lru_cache(None)
        def helper(n,remaining_amt):
            if remaining_amt==0:
                return 0
            if remaining_amt<0 or n==0:
                return float('inf')
            
            # include
            include=helper(n,remaining_amt-coins[n-1])
            if include!=float('inf'):
                include+=1
            # exclude
            exclude=helper(n-1,remaining_amt)
            return min(include,exclude)
        
        res=helper(len(coins),amount)
        return res if res!=float('inf') else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends