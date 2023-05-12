from typing import List


class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        # code here
        if arr.count(0)==0 :
            return -1
        if arr.count(0)==n :
            return 0
        c=0
        for i in range(1,len(arr)):
            if arr[i-1]!=0 and arr[i]==0:
                c+=1
        if arr[-1]>0:
            c+=1
        return c





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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.arrayOperations(n, arr)
        
        print(res)
        

# } Driver Code Ends
