#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
        if len(arr) < 2 :
            return False
        arr.sort()
        i,j=0,len(arr)-1
        while i < j :
            if arr[i]+arr[j] == target :
                return True
            elif arr[i]+arr[j] > target :
                j -=1
            else :
                i +=1
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends