#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        '''
        The series is 0, 1, 3, 8, 19, 43, 94 ...
        n = 2: 2 * 0  + 1 = 1
        n = 3: 2 * 1  + 1 = 3
        n = 4: 2 * 3  + 2 = 8
        n = 5: 2 * 8  + 3 = 19
        n = 6: 2 * 19 + 5 = 43
        n = 7: 2 * 43 + 8
        '''
        mod = 1e9+7
        
        prevPrev, prev, prevAns = 0, 1, 1
        
        for i in range(3, n+1):
            add = (prevPrev + prev)%mod
            
            prevAns = (2 * prevAns + add)%mod
            
            prevPrev = prev
            prev = add
        
        return int(prevAns)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends