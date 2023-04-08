from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        def is_different(a, b):
            return (a < 0 and b >= 0) or (a >= 0 and b < 0)
        stack = []
        for n in arr:
            if stack and is_different(stack[-1], n):
                stack.pop()
            else:
                stack.append(n)
            
        return stack
