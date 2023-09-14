#User function Template for python3
class Solution:
    def perfectSum(self, arr, n, sum):
        # code here
        dp=dict()
        mod=10**9 + 7
        def rec(i,tar) : 
            if i==n :
                if tar==0 :
                    return 1
                else :
                    return 0         
            if (i,tar) in dp :
                return dp[(i,tar)]  
            tk=0
            if (arr[i] <= tar) :
                tk= rec(i+1,tar-arr[i]) % mod
                
            ntk= rec(i+1,tar) % mod
            dp[(i,tar)] = (tk + ntk) % mod 
            return dp[(i,tar)]
        return rec(0,sum)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends
