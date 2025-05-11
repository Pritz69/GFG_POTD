from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        ans=[]
        n = len(arr)
        for i in range(n):
            for j in range(i, n):
                subarray = arr[i:j+1]
                ans.append(sum(subarray))
        ans.sort()
        return ans[-k]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends