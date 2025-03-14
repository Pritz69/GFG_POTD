//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GfG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());

        while (t-- > 0) {
            String inputLine[] = read.readLine().trim().split(" ");
            int n = inputLine.length;
            int arr[] = new int[n];

            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            int sum = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.count(arr, sum));
            System.out.println("~");
        }
    }
}

// } Driver Code Ends


class Solution {
    public int count(int coins[], int sum) {
        int n = coins.length;
        Integer[][] memo = new Integer[n + 1][sum + 1];
        return countHelper(coins, 0, sum, memo);
    }
    
    private int countHelper(int[] coins, int index, int sum, Integer[][] memo) {
        if (index >= coins.length) {
            return 0;
        }
        
        if (sum == 0) {
            return 1;
        }
        
        if (memo[index][sum] != null) {
            return memo[index][sum];
        }
        
        int notTake = countHelper(coins, index + 1, sum, memo);
        
        int take = 0;
        if (sum - coins[index] >= 0) take = countHelper(coins, index, sum - coins[index], memo);
        
        return memo[index][sum] = take + notTake;
        
    }
}