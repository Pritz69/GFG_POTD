class Solution:

    def nextLargerElement(self, arr):

        n = len(arr)
        res = [-1] * n
        stack = []  
        
        for i in range(2 * n):
            num = arr[i % n]
            # Resolve any indices whose next-greater is num
            while stack and arr[stack[-1]] < num:
                idx = stack.pop()
                res[idx] = num
            # Only push the index in the first pass
            if i < n:
                stack.append(i)

        return res