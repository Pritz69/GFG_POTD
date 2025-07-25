class Solution:
    def maxCircularSum(self, arr):
        # code here
            ##Your code here
        total = sum(arr)
        
        # Case 1: Standard Kadane (non-wrapping)
        max_end = 0
        max_sum = float('-inf')
        for x in arr:
            max_end = max(x, max_end + x)
            max_sum = max(max_sum, max_end)
        
        # Case 2: Min subarray sum
        min_end = 0
        min_sum = float('inf')
        for x in arr:
            min_end = min(x, min_end + x)
            min_sum = min(min_sum, min_end)
        
        if max_sum < 0:  # all elements are negative
            return max_sum
        
        return max(max_sum, total - min_sum)