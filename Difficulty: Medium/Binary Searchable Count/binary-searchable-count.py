class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        ans = 0

        for target in range(n):
            l, r = 0, n - 1
            x = arr[target]
            ok = True

            while l <= r:
                mid = (l + r) // 2

                if mid == target:
                    break

                if mid < target:
                    if arr[mid] > x:
                        ok = False
                        break
                    l = mid + 1
                else:
                    if arr[mid] < x:
                        ok = False
                        break
                    r = mid - 1

            if ok:
                ans += 1

        return ans