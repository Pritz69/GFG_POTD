#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos = []
        neg = []
        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        # Result array
        ans = []
        i, j = 0, 0
        toggle = True  # Start with positive
        
        # Fill alternatively from pos and neg lists
        while i < len(pos) and j < len(neg):
            if toggle:
                ans.append(pos[i])
                i += 1
            else:
                ans.append(neg[j])
                j += 1
            toggle = not toggle

        # Add remaining elements from pos list
        while i < len(pos):
            ans.append(pos[i])
            i += 1

        # Add remaining elements from neg list
        while j < len(neg):
            ans.append(neg[j])
            j += 1

        # Modify the original array
        for k in range(len(arr)):
            arr[k] = ans[k]

        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends