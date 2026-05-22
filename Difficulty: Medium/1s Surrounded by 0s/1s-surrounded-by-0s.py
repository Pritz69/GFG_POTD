class Solution:
    def cntOnes(self, grid):
        # code here
        cnt=0
        r,c=len(grid),len(grid[0])
        s=set()
        def dfs(x,y):
            if x <0 or x >= r or y<0 or y >= c or grid[x][y]==0 or (x,y) in s:
                return 
            s.add((x,y))
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x-1,y)
            dfs(x+1,y)
            
            
        for i in range(r) :
            if grid[i][0]==1 :
                dfs(i,0)
            if grid[i][c-1]==1 : 
                dfs(i,c-1)
                
        
        for i in range(c) :
            if grid[0][i]==1 :
                dfs(0,i)
            if grid[r-1][i]==1 :
                dfs(r-1,i)
        
        
        for x in range(r) :
            for y in range(c) :
                if grid[x][y]==1 and (x,y) not in s :
                    cnt +=1
        
        return cnt
        