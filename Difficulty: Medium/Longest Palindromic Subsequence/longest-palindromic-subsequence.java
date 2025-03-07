//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GfG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String s = sc.next();
            Solution obj = new Solution();
            System.out.println(obj.longestPalinSubseq(s));

            System.out.println("~");
        }
    }
}
// } Driver Code Ends




//User function Template for Java

class Solution
{
    public int lcs(String s1,String s2)
    {
        int n=s1.length();
        int m=s2.length();
        int [][]dp=new int[n+1][m+1];
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(i==0||j==0)
                {
                    dp[i][j]=0;
                }
                else if(s1.charAt(i-1) == s2.charAt(j-1))
                {
                    dp[i][j]= 1 + dp[i-1][j-1];
                }
                else
                {
                    dp[i][j]= Math.max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[n][m];
    }
    public int longestPalinSubseq(String S)
    {
        //code here
        StringBuilder sb=new StringBuilder();
        sb.append(S);
        sb.reverse();
        String x=sb.toString();
        int ans=lcs(S,x);
        return ans;
    }
}