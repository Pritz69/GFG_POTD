// Almost Same As LCS. 
// Base Condition modified from Striver's video.
class Solution
{
    public int lcs(String s,String t)
    {
        int n=s.length();
        int m=t.length();
        int dp[][]=new int[n+1][m+1];
        for (int rows[]:dp)
        {
            Arrays.fill(rows,-1);
        }
        for (int i=0;i<=n;i++)
        {
            for (int j=0;j<=m;j++)
            {
                if (i==0 || j==0)
                {
                    dp[i][j]=0;
                }
                else if ( (s.charAt(i-1)==t.charAt(j-1)) && i!=j )
                {
                    dp[i][j]= 1 + dp[i-1][j-1];
                }
                else
                {
                    dp[i][j]= 0 + Math.max(dp[i][j-1],dp[i-1][j]);
                }
            }
        }
        return dp[n][m];
    }
    public int LongestRepeatingSubsequence(String str)
    {
        // code here
        int ans=lcs(str,str);
        return ans;
    }
}
