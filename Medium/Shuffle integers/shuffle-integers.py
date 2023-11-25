class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        a = 1
        b = n//2
        while b < n:
            arr.insert(a,arr.pop(b))
            a += 2 
            b += 1

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