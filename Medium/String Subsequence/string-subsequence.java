//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            String s1;
            s1 = br.readLine();

            String s2;
            s2 = br.readLine();

            Solution obj = new Solution();
            int res = obj.countWays(s1, s2);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends



class Solution {
    int mod = (int) 1e9 + 7;
    
    // Recursion + Memoization
    int solve(int i, int j, int n, int m, String s1, String s2, int [][]dp) {
        if(j == m) {
            j = 0;
            return 1;
        }
        
        if(i == n)
            return 0;
            
        if(dp[i][j] != -1)
            return dp[i][j];
            
        int count = 0;
        if(s1.charAt(i) == s2.charAt(j)) // take + notTake
            count = (count + solve(i + 1, j + 1, n, m, s1, s2, dp) + solve(i + 1, j, n, m, s1, s2, dp)) % mod;
        else 
            count = (count + solve(i + 1, j, n, m, s1, s2, dp)) % mod;
            
        return dp[i][j] = count % mod;
    } 

    int countWays(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        int dp[][] = new int[n][m];
        
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                dp[i][j] = -1;
        
        return solve(0, 0, n, m, s1, s2, dp);
    }
}
