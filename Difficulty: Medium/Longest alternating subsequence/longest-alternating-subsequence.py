#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       #code here
        if not arr:
            return 0
    
        # Initialize the lengths for alternating subsequences
        up = 1
        down = 1
        
        # Traverse the array
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up = down + 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
        
        # The result is the maximum length of the alternating subsequence
        return max(up, down)


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends