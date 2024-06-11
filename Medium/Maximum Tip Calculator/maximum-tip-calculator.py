
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        v = []
        for i in range(len(arr)):
            v.append((abs(arr[i] - brr[i]), arr[i], brr[i]))
        v.sort(reverse=True, key=lambda x: x[0])
    
        ans = 0
        for i in range(len(v)):
            if x == 0:
                ans += v[i][2]
            elif y == 0:
                ans += v[i][1]
            else:
                if v[i][1] > v[i][2]:
                    x -= 1
                    ans += v[i][1]
                else:
                    y -= 1
                    ans += v[i][2]
        return ans
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends