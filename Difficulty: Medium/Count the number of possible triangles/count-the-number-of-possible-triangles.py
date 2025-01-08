#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n = len(arr)
        count = 0

        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends