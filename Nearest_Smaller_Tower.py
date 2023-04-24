#User function Template for python3

class Solution:
    def nearestSmallestTower(self,arr):
        #code here
        n = len(arr)
        pre, suf = [], []
        res = [-1] * n
        
        for i in range(n):
            while pre and arr[pre[-1]] >= arr[i]:
                pre.pop()
            
            if pre:
                res[i] = pre[-1]
            
            pre.append(i)
        
        for i in range(n-1, -1, -1):
            while suf and arr[suf[-1]] >= arr[i]:
                suf.pop()
                
            if suf:
                if res[i] != -1:
                    if abs(res[i] - i) == abs(suf[-1] - i):
                        if arr[res[i]] > arr[suf[-1]]:
                            res[i] = suf[-1]
                    elif abs(res[i] - i) > abs(suf[-1] - i):
                        res[i] = suf[-1]
                else:
                    res[i] = suf[-1]
            
            suf.append(i)
            
        return res
