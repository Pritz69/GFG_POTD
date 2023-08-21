

//User function Template for Java

class Solution
{
    public boolean check(int [][]matrix,int i,int j)
    {
        int nr[]={-1,-1,-1,0,0,1,1,1};
        int nc[]={-1,0,1,-1,1,-1,0,1};
        int n=matrix.length;
        int m=matrix[0].length;
        int cnt=0;
        for(int k=0;k<8;k++)
        {
            int r=i+nr[k];
            int c=j+nc[k];
            if(r>=0 && r<n && c>=0 && c<m && matrix[r][c]==0)
            {
                cnt +=1;
            }
        }
        if(cnt>0 && cnt%2==0)
        {
            return true;
        }
        return false;
    }
    public int  Count(int[][] matrix)
    {
        // code here
        int c=0;
        for(int i=0;i<matrix.length;i++)
        {
            for(int j=0;j<matrix[0].length;j++)
            {
                if(matrix[i][j]==1)
                {
                    if(check(matrix,i,j)==true)
                    {
                        c +=1;
                    }
                }
            }
        }
        return c;
    }
}
