//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

class GFG {
  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    while (T-- > 0) {
      int n = sc.nextInt();
      int a[] = new int[n];
      for(int i=0;i<n;i++){
        a[i]=sc.nextInt();
      }
      Solution obj = new Solution();
      int ans = obj.maxCoins(n,a);
      System.out.println(ans);
    }
  }
}

// } Driver Code Ends


//User function Template for Java

class Solution {

    public static int fun(int [] arr, int i, int j, int [][] dp){

        if(i > j) return 0;

        int max = Integer.MIN_VALUE;

        if(dp[i][j] != -1) return dp[i][j];

        for(int ind = i; ind <= j; ind++){

            int cost = arr[ind]*arr[i-1]*arr[j+1] + fun(arr, i, ind-1, dp) + fun(arr, ind+1, j, dp);

            max = Math.max(max, cost);

        }

        return dp[i][j]= max;

    }

    public static int maxCoins(int N, int[] arr) {

        int [] a = new int[N+2];

        int [][] dp = new int[N+1][N+1];

        for(int i=0; i< dp.length; i++){

            for(int j=0; j< dp[0].length; j++) dp[i][j] = -1;

        }

        a[0] = 1;

        for(int i=1; i< a.length-1; i++){

            a[i] = arr[i-1];

        }

        a[a.length-1] = 1;

        return fun(a, 1, arr.length, dp);

 

  }

}
     
