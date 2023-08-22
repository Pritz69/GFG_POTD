


class Solution {
    public static int findMinOperation(int n, int[][] Matrix) {
        // code here
        int mac=Integer.MIN_VALUE;
        int mar=Integer.MIN_VALUE;
        for(int i=0;i<n;i++)
        {
            int rs=0;
            int cs=0;
            for(int j=0;j<n;j++)
            {
                rs += Matrix[i][j];
                cs += Matrix[j][i];
            }
            mar=Math.max(mar,rs);
            mac=Math.max(mac,cs);
        }
        int ans=Math.max(mar,mac);
        int c=0;
        for(int i=0;i<n;i++)
        {
            int rs=0;
            for(int j=0;j<n;j++)
            {
                rs += Matrix[i][j];
            }
            c+=Math.abs(ans-rs);
        }
        return c;
    }
}
        
