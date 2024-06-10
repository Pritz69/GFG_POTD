#User function Template for python3

class Solution:
    def shortestPath(self, x, y): 
        # code here
        c=0
        while x!=y :
            if x>y :
                x =x//2
            else :
                y =y//2
            c +=1
        return c
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		x,y = map(int,input().strip().split())
		ob = Solution()
		print(ob.shortestPath(x,y))
# } Driver Code Ends