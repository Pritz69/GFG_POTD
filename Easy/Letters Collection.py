class Solution:
    direction_1=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    direction_2=[(0,2),(1,2),(2,2),(-1,2),(-2,2),(0,-2),(1,-2),(2,-2),(-1,-2),(-2,-2),(2,0),(2,1),(2,-1),(-2,0),(-2,1),(-2,-1)]
    
    def is_valid(self,x,y,n,m):
        return x>=0 and x<n and y>=0 and y<m
    
    def matrixSum(self, n, m, mat, q, queries):
        res=[]
        for i in range(q):
            q_sum=0
            direction=None
            if queries[i][0]==1:
                direction=self.direction_1
            else:
                direction=self.direction_2
            x=queries[i][1]
            y=queries[i][2]
            for dx,dy in direction:
                new_x=x+dx
                new_y=y+dy
                if self.is_valid(new_x,new_y,n,m):
                    q_sum+=mat[new_x][new_y]
            res.append(q_sum)
        return res
