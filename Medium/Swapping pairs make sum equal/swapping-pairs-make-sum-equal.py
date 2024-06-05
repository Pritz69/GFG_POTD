class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        firstarraysum = sum(a)
        secondarraysum = sum(b)
        
        if firstarraysum == secondarraysum:
            return 1
        
        botharrayssum = firstarraysum + secondarraysum
        if botharrayssum % 2 != 0:
            return -1
        
        equalsum = botharrayssum // 2
        difference = secondarraysum - equalsum
        
        a.sort()
        b.sort()
        
        i, j = 0, 0
        
        while i < n and j < m:
            if b[j] - a[i] > difference:
                i += 1
            elif b[j] - a[i] < difference:
                j += 1
            else:
                return 1
        
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends