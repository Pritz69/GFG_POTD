class Solution
{
    public int[][] searchWord(char[][] grid, String word)
    {
        int n = grid.length; 
        int m = grid[0].length;
        int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
        int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};
        List<List<Integer>> ans = new ArrayList<>();
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(grid[i][j] == word.charAt(0))
                {
                    for(int k=0; k<8; k++)
                    {
                        if(dfs(grid, n,m, word, 0, i,j, dx[k], dy[k]))
                        {
                            List<Integer> position = new ArrayList<>();
                            position.add(i);
                            position.add(j);
                            ans.add(position);
                            break;
                        }
                        
                    }
                }
            }
        }
        int res[][] = new int[ans.size()][2];
        int k=0;
        for(List<Integer> x : ans)
        {
            res[k][0] = x.get(0); 
            res[k][1] = x.get(1);
            k++;
        }
        return res;
    }
    boolean dfs(char[][] grid, int n, int m,  String word, int idx, int x, int y, int nei_x, int nei_y)
    {
        if (idx == word.length())
        return true; // we find the entire word
        
        //check in bound
        if(x>=0 && x<n && y>=0 && y<m && word.charAt(idx) == grid[x][y])
        {
            return dfs(grid, n, m, word, idx+1, x+nei_x, y+nei_y,nei_x, nei_y);
        }
        return false;
    }
}
