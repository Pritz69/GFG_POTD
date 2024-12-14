#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        i = 0
        n = len(arr)
        j = n - 1

        while i <= j:
            mid = (i + j) // 2
            if arr[mid] == key:
                return mid
            if arr[mid] < arr[j]:
                if arr[mid] <= key <= arr[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if arr[i] <= key <= arr[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends