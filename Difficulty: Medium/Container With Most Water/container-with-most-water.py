
class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        l=0
        r=n-1
        ans=0
        while l < r :
            ans=max(ans,min(arr[r],arr[l])*(r-l))
            if arr[l] < arr[r] :
                l +=1
            else :
                r -=1
                
        return ans
#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends