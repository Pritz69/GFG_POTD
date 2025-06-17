class Solution:
    def minimumCoins(self, A, k):
        
        A.sort()

        n = len(A)
        pre = [0]
        for x in A:
            pre.append(pre[-1] + x)

        res = pre[-1]
        j = 0

        for i in range(n):
            
            while j < n and A[j] <= A[i] + k:
                j += 1

            # Calculate cost to reduce all coins greater than A[i]+k
            if j < n:
                large = pre[-1] - pre[j] - (n - j) * (A[i] + k)
            else:
                large = 0

            # Total cost = sum of smaller/equal values + cost to reduce big ones
            res = min(res, pre[i] + large)

        return res