#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        m=arr[0]
        for x in arr :
            if x < m :
                return x
        return m

#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends