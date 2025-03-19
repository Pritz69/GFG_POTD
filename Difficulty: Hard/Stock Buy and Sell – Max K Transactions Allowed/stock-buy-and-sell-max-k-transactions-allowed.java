//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for (int t = 0; t < tc; t++) {
            String[] input = br.readLine().split(" ");
            int arr[] = new int[input.length];

            for (int i = 0; i < arr.length; i++) arr[i] = Integer.parseInt(input[i]);

            // Read the integer k
            int k = Integer.parseInt(br.readLine());

            // Call the solution function
            Solution obj = new Solution();
            System.out.println(obj.maxProfit(arr, k));
            System.out.println("~");
        }
    }
}
// } Driver Code Ends

class Solution {
    static int maxProfit(int prices[],int k) {
        
        int n=prices.length;
        int dp[][][] = new int[n+1][2][k+1];
        for(int i=n-1;i>=0;i--)
        {
            for(int b=0;b<=1;b++)
            {
                for(int c=1;c<=k;c++)
                {
                    if(b==1)
                    {
                        dp[i][b][c] = Math.max(-prices[i] + dp[i+1][0][c], 0 + dp[i+1][1][c]);
                    }
                    if(b==0) 
                    {
                        dp[i][b][c] = Math.max(+prices[i] + dp[i+1][1][c-1], 0 + dp[i+1][0][c]);
                    }
                }
            }
        }
        return dp[0][1][k];
    }
}
