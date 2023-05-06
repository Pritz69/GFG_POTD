class Solution {
    public static boolean makeChanges(int N, int k, int target, int[] coins) {
        // code here
        boolean dp[][]=new boolean[k+1][target+1];
        dp[0][0] = true;
        for (int i=0;i<N;i++)
        {
            for (int j=1;j<k+1;j++)
            {
                for (int l=1;l<target+1;l++)
                {
                    if (coins[i]<=l && dp[j][l]==false)
                    {
                        dp[j][l]=dp[j-1][l-coins[i]];
                    }
                }
            }
        }
        return dp[k][target];
    }
}
