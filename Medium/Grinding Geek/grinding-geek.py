
from typing import List
import math

class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        # code here
        memo = [[-1] * (total + 1) for _ in range(n)]

        def rec(i, remaining_budget):
            if i == n:
                return 0
    
            if memo[i][remaining_budget] != -1:
                return memo[i][remaining_budget]
    
            # Buy the current course
            take_course = 0
            if remaining_budget >= cost[i]:
                refunded_amount = int(0.9 * cost[i])
                take_course = 1 + rec(i + 1, remaining_budget - cost[i] + refunded_amount)
    
            # Skip the current course
            not_take_course = rec(i + 1, remaining_budget)
    
            memo[i][remaining_budget] = max(take_course, not_take_course)
            return memo[i][remaining_budget]
    
        return rec(0, total)





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
        
        
        total = int(input())
        
        
        cost=IntArray().Input(n)
        
        obj = Solution()
        res = obj.max_courses(n, total, cost)
        
        print(res)
        

# } Driver Code Ends