
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        low = 0
        high = n - 1
        closest = arr[0]
        
        while low <= high:
            mid = (low + high) // 2
            
            if abs(arr[mid] - k) < abs(closest - k) or (abs(arr[mid] - k) == abs(closest - k) and arr[mid] > closest):
                closest = arr[mid]
            
            if arr[mid] < k:
                low = mid + 1
            elif arr[mid] > k:
                high = mid - 1
            else :
                return arr[mid]
        
        return closest

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
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends