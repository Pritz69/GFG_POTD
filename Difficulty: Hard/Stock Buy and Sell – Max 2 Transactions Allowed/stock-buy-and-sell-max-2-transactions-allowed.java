//{ Driver Code Starts
import java.io.*;
import java.util.*;

class Sorting {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int g = 0; g < t; g++) {
            String[] str = (br.readLine()).trim().split(" ");
            int arr[] = new int[str.length];
            for (int i = 0; i < str.length; i++) arr[i] = Integer.parseInt(str[i]);
            System.out.println(new Solution().maxProfit(arr));
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {
    static int maxProfit(int prices[]) {
        
        int n=prices.length;
        int dp[][][] = new int[n+1][2][2+1];
        for(int i=n-1;i>=0;i--)
        {
            for(int b=0;b<=1;b++)
            {
                for(int c=1;c<=2;c++)
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
        return dp[0][1][2];
    }
}
