#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        ans = []
        low = 0
        high = 0
        total = 0
        while high < len(arr):
            total += arr[high]
            while total >target:
                total -= arr[low]
                low += 1
            if total == target:
                ans.append(low+1)
                ans.append(high+1)
                break
            high+=1

        if ans !=[]:
            return ans
        return [-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends