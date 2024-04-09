//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class GfG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            int points[][] = new int[m][n];
            for (int i = 0; i < m; i++)
                for (int j = 0; j < n; j++) points[i][j] = sc.nextInt();
            Solution ob = new Solution();
            System.out.println(ob.minPoints(points, m, n));
        }
    }
}
// } Driver Code Ends

// User function Template for Java



class Solution {
    int f(int i, int j, int[][] a, int[][] dp) {
        int n = a.length;
        int m = a[0].length;
        
        // Base case: Reached the destination cell
        if (i == n - 1 && j == m - 1) {
            // Need at least 1 point to reach the destination cell
            return Math.max(1, 1 - a[i][j]);
        }
        
        // Base case: Out of bounds
        if (i >= n || j >= m) {
            return Integer.MAX_VALUE;
        }
        
        // If dp[i][j] has already been computed, return it
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        
        // Recursive calls for the right and bottom cells
        int right = f(i, j + 1, a, dp);
        int bottom = f(i + 1, j, a, dp);
        
        // Minimum points required to reach (i, j)
        // Need at least 1 point to move to the next cell
        int minPoints = Math.min(right, bottom) - a[i][j];
        // Ensure the minimum points is at least 1
        dp[i][j] = Math.max(1, minPoints);
        
        return dp[i][j];
    }
    
    public int minPoints(int[][] points, int m, int n) {
        int[][] dp = new int[m][n];
        
        // Initialize dp array with -1
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        
        // Call the recursive function starting from (0, 0)
        return f(0, 0, points, dp);
    }
}