class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
        a=[-1,0,1,0]
        b=[0,1,0,-1]
        old=image[sr][sc]
        n=len(image)
        m=len(image[0])
        vis=[[0]*m for _ in range(n)]
        def dfs(sr,sc):
            vis[sr][sc]=1
            image[sr][sc]=newColor
            for i in range(4):
                nr=sr+a[i]
                nc=sc+b[i]
                if 0<=nr<n and 0<=nc<m and vis[nr][nc]==0 and image[nr][nc]==old:
                    dfs(nr,nc)
        dfs(sr,sc)
        return image


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends