class Solution{
    
    private void dfs(int[][] mat,int i,int j,int n,int m,boolean[][] visited){
        if(i<0 || i>=n || j<0 || j>=m || visited[i][j])
            return;
        visited[i][j] = true;
        
        if(j+1 < m && mat[i][j+1] >= mat[i][j] && !visited[i][j+1]) // right
            dfs(mat,i,j+1,n,m,visited);
        if(i+1 < n && mat[i+1][j] >= mat[i][j] && !visited[i+1][j]) // down
            dfs(mat,i+1,j,n,m,visited);
        if(j-1 >= 0 && mat[i][j-1] >= mat[i][j] && !visited[i][j-1]) //left
            dfs(mat,i,j-1,n,m,visited);
        if(i-1 >= 0 && mat[i-1][j] >= mat[i][j] && !visited[i-1][j])// up
            dfs(mat,i-1,j,n,m,visited);
    }
    
	int water_flow(int [][] mat, int n, int m) {
		boolean[][] indianOcean = new boolean[n][m];
		boolean[][] arabianSea = new boolean[n][m];
		
		/** Indian ocean */
		for(int j=0;j<m;j++)
		    dfs(mat,0,j,n,m,indianOcean);

		for(int i=0;i<n;i++)
		    dfs(mat,i,0,n,m,indianOcean);
		
		/** Arabian Sea */
		for(int j=0;j<m;j++)
		    dfs(mat,n-1,j,n,m,arabianSea);
		
		for(int i=0;i<n;i++)
		    dfs(mat,i,m-1,n,m,arabianSea);
		
		
		int count = 0;
		for(int i=0;i<n;i++){
		    for(int j=0;j<m;j++){
		        if(indianOcean[i][j] && arabianSea[i][j])
		            count++;
		    }
		}
		return count;
	}
}
