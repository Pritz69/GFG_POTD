#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    #code here
        curr_reach, max_reach, jump_count = 0, 0, 0
        for i in range(len(arr) - 1):
            max_reach = max(max_reach, i + arr[i])
            if curr_reach == i:
                if max_reach == i:
                    # We cannot jump any further
                    return -1
                jump_count += 1
                curr_reach = max_reach
        return jump_count

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends