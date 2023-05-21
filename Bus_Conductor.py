#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def findMoves(self,n,chairs,passengers):
        #code here
        chairs.sort()
        passengers.sort()
        moves = 0
        for i in range(n):
            diff = abs(chairs[i] - passengers[i])
            moves += diff
        return moves

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        a=[int(i) for i in input().split()]
        b=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.findMoves(n,a,b))
        
# } Driver Code Ends
