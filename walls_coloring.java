class Solution{
	int minCost(int [][] colors, int N){
        
        for(int i=N-2; i>=0; i--){
            
            colors[i][0] += Math.min( colors[i+1][1], colors[i+1][2] );
            colors[i][1] += Math.min( colors[i+1][0], colors[i+1][2] );
            colors[i][2] += Math.min( colors[i+1][0], colors[i+1][1] );
            
        }
        
        return Math.min( colors[0][0], Math.min( colors[0][1], colors[0][2] ) );
        
    }
}
