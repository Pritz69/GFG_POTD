class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        ar1 = arr[n//2:]
        for i in range(n//2):
            arr.insert(2*i+1,ar1[i])
            arr.pop(-1)
        return arr

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends