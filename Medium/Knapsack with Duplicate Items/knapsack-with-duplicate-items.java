//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            String line1[] = in.readLine().trim().split("\\s+");
            int N = Integer.parseInt(line1[0]);
            int W = Integer.parseInt(line1[1]);
            String line2[] = in.readLine().trim().split("\\s+");
            int val[] = new int[N];
            for(int i = 0;i < N;i++)
                val[i] = Integer.parseInt(line2[i]);
            String line3[] = in.readLine().trim().split("\\s+");
            int wt[] = new int[N];
            for(int i = 0;i < N;i++)
                wt[i] = Integer.parseInt(line3[i]);
                
            Solution ob = new Solution();
            System.out.println(ob.knapSack(N, W, val, wt));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    static int knapSack(int N, int W, int val[], int wt[])
    {
        int[][]dp=new int[N+1][W+1];
        for(int []arr : dp)
        {
            Arrays.fill(arr,-1);
        }
        return res(N-1,W,val,wt,dp);
    }
    public static int res(int n, int w, int val[], int wt[],int[][]dp){
        if(n<0)
        {
            return 0;
        }
        if(dp[n][w]!=-1)
        {
            return dp[n][w];
        }
        int includeItem=0;
        int excludeItem=0;
        if(w>=wt[n])
        {
            includeItem = res(n, w - wt[n], val, wt,dp) + val[n];
        }
        excludeItem = res(n - 1, w, val, wt,dp);
        return dp[n][w] = Math.max(includeItem, excludeItem);
    }
}