from typing import List
class Solution:
    
    def largestIsland(self, grid : List[List[int]]) -> int:
        
        vis=[] 
        for i in range(len(grid)):
            temp=[]
            for j in range(len(grid)):
                temp.append(-1)
            vis.append(temp)
    
        n=len(grid)   
        def dfs(i,j,typ,l):
            if i>=0 and j>=0 and i<n and j<n and grid[i][j]==1 and vis[i][j]==-1:
                l[0]+=1
                vis[i][j]=typ 
                dfs(i+1,j,typ,l)
                dfs(i-1,j,typ,l)
                dfs(i,j-1,typ,l)
                dfs(i,j+1,typ,l) 
        t=1 
        m={}
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1 and vis[i][j]==-1:
                    l=[0]
                    dfs(i,j,t,l)
                    m[t]=l[0]
                    t+=1 
                    if l[0]==n*n:
                        return l[0]
        def isvalid(i,j):
            if i>=0 and j>=0 and i<n and j<n and grid[i][j]==1:
                return 1 
            return 0 
        k=-1
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    s=set()
                    if isvalid(i+1,j):
                        s.add(vis[i+1][j])
                    if isvalid(i-1,j):
                        s.add(vis[i-1][j])
                    if isvalid(i,j+1):
                        s.add(vis[i][j+1])
                    if isvalid(i,j-1):
                        s.add(vis[i][j-1])
                    cur_sum=1 
                    for p in s:
                        cur_sum+=m[p]
                    k=max(k,cur_sum)
        return k




#{ 
 # Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
# } Driver Code Ends