
class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        
        lmax=[0 for i in range(n)]
        rmax=[0 for i in range(n)]
        
        lmax[0]=arr[0]
        rmax[-1]=arr[-1]
        
        
        for i in range(1,n):
            lmax[i]=max(lmax[i-1],arr[i])
        
        for i in range(n-2,-1,-1):
            rmax[i]=max(rmax[i+1],arr[i])
        
        ans=0
        for i in range(1,n-1):
            ans+=(min(lmax[i],rmax[i])-arr[i])
        
        return ans


#3333444
#4444422


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