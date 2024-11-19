#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        """
        Rearranges numbers into the lexicographically next greater permutation of numbers.
        If such an arrangement is not possible, it must rearrange it as the lowest possible order.
        """
        n = len(arr)
        i = n - 2

        # Step 1: Find the first decreasing element from the end
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the next larger element to swap with arr[i]
            for j in range(n - 1, i, -1):
                if arr[j] > arr[i]:
                    # Swap the two elements
                    arr[i], arr[j] = arr[j], arr[i]
                    break

        # Step 3: Reverse the suffix starting at index i+1
        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends