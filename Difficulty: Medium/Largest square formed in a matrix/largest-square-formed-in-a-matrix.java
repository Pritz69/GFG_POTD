//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int mat[][] = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mat[i][j] = sc.nextInt();
                }
            }
            Solution ob = new Solution();
            System.out.println(ob.maxSquare(n, m, mat));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    static int maxSquare(int n, int m, int mat[][]) {
        // code here
    
    if(n==0 || m==0)
        return 0;
        
    int [][] dp = new int[n][m];
    int maxSide =0;
    
    for(int i=0; i<n; i++){
        dp[i][0] = mat[i][0];
        maxSide = Math.max(maxSide, dp[i][0]);
    }
    
    for(int j=0; j<m; j++){
        dp[0][j] = mat[0][j];
        maxSide = Math.max(maxSide, dp[0][j]);
    }
    
    for(int i=1; i<n; i++){
        for(int j=1; j<m; j++){
            if(mat[i][j] ==1){
                dp[i][j] = Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1])) + 1;
                maxSide = Math.max(maxSide, dp[i][j]);
            }
            else{
                dp[i][j] =0;
            }
        }
    }
    return maxSide;
        
    }
}