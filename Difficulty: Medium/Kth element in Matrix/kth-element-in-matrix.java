class Solution
{
    private static int upperBound(int[] row, int value)
    {
        int low=0;
        int high=row.length;
        
        while(low<high)
        {
            int mid = low+(high-low)/2;
            if(row[mid]<=value)
            {
                low=mid+1;
            }
            else
            {
                high=mid;
            }
        }
        return low;
    }
    private static int countLessOrEqual(int[][] mat,int value)
    {
        int n=mat.length;
        
        int count=0;
        for(int i=0;i<n;i++)
        {
            int lb=upperBound(mat[i],value);
            count+=lb;
        }
        return count;
    }
    
    public static int kthSmallest(int[][]mat,int k)
    {
        //code here.
        int low = mat[0][0];
        int n=mat.length;
        int high = mat[n-1][n-1];
        
        while(low<high)
        {
            int mid = low+(high-low)/2;
            
            int count = countLessOrEqual(mat,mid);
            
            if(count<k)
            {
                low=mid+1;
            }
            else
            {
                high=mid;
            }
        }
        return low;
    }
}
