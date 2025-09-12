class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        res = arr[-1] - arr[0]
        small = arr[0] + k
        big = arr[-1] - k
        for i in range(1, len(arr)):
            if(arr[i] - k < 0):
                continue
            mini = min(small, arr[i] - k)
            maxi = max(big, arr[i-1] + k)
            res = min(res, maxi - mini)
        return res