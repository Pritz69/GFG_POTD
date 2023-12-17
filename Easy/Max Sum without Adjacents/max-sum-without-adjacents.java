//{ Driver Code Starts
//Initial Template for Java



import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            int n = Integer.parseInt(br.readLine().trim());
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            int ans = new Solution().findMaxSum(arr, n);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    int solve(int i,int n,int arr[],int dp[])
    {
        if (i>=n)
        {
            return 0;
        }
        if (dp[i]!=0)
        {
            return dp[i];
        }
        int tk=arr[i]+solve(i+2,n,arr,dp);
        int ntk=solve(i+1,n,arr,dp);
        dp[i]=Math.max(tk,ntk);
        return dp[i];
    }
    int findMaxSum(int arr[], int n) {
        // code here
        int dp[]=new int[n+1];
        return solve(0,n,arr,dp);
    }
    
}