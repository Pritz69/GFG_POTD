class Solution:
    def farMin(self, arr):
        # Code Here
        n = len(arr)
        res = [-1] * n
        
        suffix_min = [0] * n
        suffix_min[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i+1])
        
        for i in range(n-1):
            if suffix_min[i+1] >= arr[i]:
                res[i] = -1
                continue
            
            lo, hi = i+1, n-1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if suffix_min[mid] < arr[i]:
                    ans = mid
                    lo = mid + 1  # try to go farther right
                else:
                    hi = mid - 1
            res[i] = ans
        
        return res